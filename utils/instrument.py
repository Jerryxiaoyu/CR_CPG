import os
import re
import subprocess
import base64
import os.path as osp
import pickle as pickle
import inspect
import hashlib
import sys
from contextlib import contextmanager

import errno


#from io import StringIO  # python 3
#from StringIO import StringIO  # python 2
import datetime
import dateutil.tz
import json
import time
import numpy as np

import collections


class IO:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def to_pickle(self, obj):
        with open(self.file_name, 'wb') as output:
            pickle.dump(obj, output, protocol=pickle.HIGHEST_PROTOCOL)
    
    def read_pickle(self):
        with open(self.file_name, 'rb') as input_:
            obj = pickle.load(input_)
        return obj
    
class StubBase(object):
    def __getitem__(self, item):
        return StubMethodCall(self, "__getitem__", args=[item], kwargs=dict())

    def __getattr__(self, item):
        try:
            return super(self.__class__, self).__getattribute__(item)
        except AttributeError:
            if item.startswith("__") and item.endswith("__"):
                raise
            return StubAttr(self, item)

    def __pow__(self, power, modulo=None):
        return StubMethodCall(self, "__pow__", [power, modulo], dict())

    def __call__(self, *args, **kwargs):
        return StubMethodCall(self.obj, self.attr_name, args, kwargs)

    def __add__(self, other):
        return StubMethodCall(self, "__add__", [other], dict())

    def __rmul__(self, other):
        return StubMethodCall(self, "__rmul__", [other], dict())

    def __div__(self, other):
        return StubMethodCall(self, "__div__", [other], dict())

    def __rdiv__(self, other):
        return StubMethodCall(BinaryOp(), "rdiv", [self, other], dict())  # self, "__rdiv__", [other], dict())

    def __rpow__(self, power, modulo=None):
        return StubMethodCall(self, "__rpow__", [power, modulo], dict())

 


class StubAttr(StubBase):
    def __init__(self, obj, attr_name):
        self.__dict__["_obj"] = obj
        self.__dict__["_attr_name"] = attr_name

    @property
    def obj(self):
        return self.__dict__["_obj"]

    @property
    def attr_name(self):
        return self.__dict__["_attr_name"]

    def __str__(self):
        return "StubAttr(%s, %s)" % (str(self.obj), str(self.attr_name))
 
class StubClass(StubBase):
    def __init__(self, proxy_class):
        self.proxy_class = proxy_class

    def __call__(self, *args, **kwargs):
        if len(args) > 0:
            # Convert the positional arguments to keyword arguments
            spec = inspect.getargspec(self.proxy_class.__init__)
            kwargs = dict(list(zip(spec.args[1:], args)), **kwargs)
            args = tuple()
        return StubObject(self.proxy_class, *args, **kwargs)

    def __getstate__(self):
        return dict(proxy_class=self.proxy_class)

    def __setstate__(self, dict):
        self.proxy_class = dict["proxy_class"]

    def __getattr__(self, item):
        if hasattr(self.proxy_class, item):
            return StubAttr(self, item)
        raise AttributeError

    def __str__(self):
        return "StubClass(%s)" % self.proxy_class


class StubObject(StubBase):
    def __init__(self, __proxy_class, *args, **kwargs):
        if len(args) > 0:
            spec = inspect.getargspec(__proxy_class.__init__)
            kwargs = dict(list(zip(spec.args[1:], args)), **kwargs)
            args = tuple()
        self.proxy_class = __proxy_class
        self.args = args
        self.kwargs = kwargs

    def __getstate__(self):
        return dict(args=self.args, kwargs=self.kwargs, proxy_class=self.proxy_class)

    def __setstate__(self, dict):
        self.args = dict["args"]
        self.kwargs = dict["kwargs"]
        self.proxy_class = dict["proxy_class"]

    def __getattr__(self, item):
        # why doesnt the commented code work?
        # return StubAttr(self, item)
        # checks bypassed to allow for accesing instance fileds
        if hasattr(self.proxy_class, item):
            return StubAttr(self, item)
        raise AttributeError('Cannot get attribute %s from %s' % (item, self.proxy_class))

    def __str__(self):
        return "StubObject(%s, *%s, **%s)" % (str(self.proxy_class), str(self.args), str(self.kwargs))

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class VariantDict(AttrDict):
    def __init__(self, d, hidden_keys):
        super(VariantDict, self).__init__(d)
        self._hidden_keys = hidden_keys

    def dump(self):
        return {k: v for k, v in self.items() if k not in self._hidden_keys}


class VariantGenerator(object):
    """
    Usage:

    vg = VariantGenerator()
    vg.add("param1", [1, 2, 3])
    vg.add("param2", ['x', 'y'])
    vg.variants() => # all combinations of [1,2,3] x ['x','y']

    Supports noncyclic dependency among parameters:
    vg = VariantGenerator()
    vg.add("param1", [1, 2, 3])
    vg.add("param2", lambda param1: [param1+1, param1+2])
    vg.variants() => # ..
    """

    def __init__(self):
        self._variants = []
        self._populate_variants()
        self._hidden_keys = []
        for k, vs, cfg in self._variants:
            if cfg.get("hide", False):
                self._hidden_keys.append(k)

    def add(self, key, vals, **kwargs):
        self._variants.append((key, vals, kwargs))

    def _populate_variants(self):
        methods = inspect.getmembers(
            self.__class__, predicate=lambda x: inspect.isfunction(x) or inspect.ismethod(x))
        methods = [x[1].__get__(self, self.__class__)
                   for x in methods if getattr(x[1], '__is_variant', False)]
        for m in methods:
            self.add(m.__name__, m, **getattr(m, "__variant_config", dict()))

    def variants(self, randomized=False):
        ret = list(self.ivariants())
        if randomized:
            np.random.shuffle(ret)
        return list(map(self.variant_dict, ret))

    def variant_dict(self, variant):
        return VariantDict(variant, self._hidden_keys)

    def to_name_suffix(self, variant):
        suffix = []
        for k, vs, cfg in self._variants:
            if not cfg.get("hide", False):
                suffix.append(k + "_" + str(variant[k]))
        return "_".join(suffix)

    def ivariants(self):
        dependencies = list()
        for key, vals, _ in self._variants:
            if hasattr(vals, "__call__"):
                args = inspect.getargspec(vals).args
                if hasattr(vals, 'im_self') or hasattr(vals, "__self__"):
                    # remove the first 'self' parameter
                    args = args[1:]
                dependencies.append((key, set(args)))
            else:
                dependencies.append((key, set()))
        sorted_keys = []
        # topo sort all nodes
        while len(sorted_keys) < len(self._variants):
            # get all nodes with zero in-degree
            free_nodes = [k for k, v in dependencies if len(v) == 0]
            if len(free_nodes) == 0:
                error_msg = "Invalid parameter dependency: \n"
                for k, v in dependencies:
                    if len(v) > 0:
                        error_msg += k + " depends on " + " & ".join(v) + "\n"
                raise ValueError(error_msg)
            dependencies = [(k, v)
                            for k, v in dependencies if k not in free_nodes]
            # remove the free nodes from the remaining dependencies
            for _, v in dependencies:
                v.difference_update(free_nodes)
            sorted_keys += free_nodes
        return self._ivariants_sorted(sorted_keys)

    def _ivariants_sorted(self, sorted_keys):
        if len(sorted_keys) == 0:
            yield dict()
        else:
            first_keys = sorted_keys[:-1]
            first_variants = self._ivariants_sorted(first_keys)
            last_key = sorted_keys[-1]
            last_vals = [v for k, v, _ in self._variants if k == last_key][0]
            if hasattr(last_vals, "__call__"):
                last_val_keys = inspect.getargspec(last_vals).args
                if hasattr(last_vals, 'im_self') or hasattr(last_vals, '__self__'):
                    last_val_keys = last_val_keys[1:]
            else:
                last_val_keys = None
            for variant in first_variants:
                if hasattr(last_vals, "__call__"):
                    last_variants = last_vals(
                        **{k: variant[k] for k in last_val_keys})
                    for last_choice in last_variants:
                        yield AttrDict(variant, **{last_key: last_choice})
                else:
                    for last_choice in last_vals:
                        yield AttrDict(variant, **{last_key: last_choice})


def variant(*args, **kwargs):
    def _variant(fn):
        fn.__is_variant = True
        fn.__variant_config = kwargs
        return fn

    if len(args) == 1 and isinstance(args[0], collections.Callable):
        return _variant(args[0])
    return _variant


def stub(glbs):
    # replace the __init__ method in all classes
    # hacky!!!
    for k, v in list(glbs.items()):
        # look at all variables that are instances of a class (not yet Stub)
        if isinstance(v, type) and v != StubClass:
            glbs[k] = StubClass(v)  # and replaces them by a the same but Stub


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


exp_count = 0
now = datetime.datetime.now(dateutil.tz.tzlocal())
timestamp = now.strftime('%Y_%m_%d_%H_%M_%S')
remote_confirmed = False
