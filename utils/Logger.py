import numpy as np

import os

import shutil
import glob
import csv
from datetime import datetime
import pandas as pd


def configure_log_dir(logname, txt='', copy = False, log_group=None, No_time = False):
    """
    Set output directory to d, or to /tmp/somerandomnumber if d is None
    """
    if log_group is not None:
        root_path = os.path.join('log-files', log_group)
    else:
        root_path = os.path.join('log-files' )
    
    if No_time:
        path = os.path.join(root_path, logname,   txt)
    else:
        now = datetime.now().strftime("%b-%d_%H:%M:%S")
        path = os.path.join(root_path, logname, now +txt)
    if not os.path.isdir(path):
        os.makedirs(path)  # create path
    if copy:
        filenames = glob.glob('*.py')  # put copy of all python files in log_dir
        for filename in filenames:  # for reference
            shutil.copy(filename, path)
    return path


class LoggerCsv(object):
    """ Simple training logger: saves to file and optionally prints to stdout
    V1.0 可以实时存储
    """
    
    def __init__(self, logdir, csvname='log'):
        """
        Args:
            logname: name for log (e.g. 'Hopper-v1')
            now: unique sub-directory name (e.g. date/time string)
        """
        self.path = os.path.join(logdir, csvname + '.csv')
        self.write_header = True
        self.log_entry = {}
        self.f = open(self.path, 'w')
        self.writer = None  # DictWriter created with first call to write() method
        self.open_flag = True
    
    def write(self, display=True):
        """ Write 1 log entry to file, and optionally to stdout
        Log fields preceded by '_' will not be printed to stdout

        Args:
            display: boolean, print to stdout
        """
        if display:
            self.disp(self.log_entry)
        
        if self.open_flag:
            if self.write_header:
                fieldnames = [x for x in self.log_entry.keys()]
                self.writer = csv.DictWriter(self.f, fieldnames=fieldnames)
                self.writer.writeheader()
                self.write_header = False
        
        else:
            self.f = open(self.path, 'a+')
            self.open_flag = True
            fieldnames = [x for x in self.log_entry.keys()]
            self.writer = csv.DictWriter(self.f, fieldnames=fieldnames)
        
        self.writer.writerow(self.log_entry)
        self.log_enbtry = {}
        self.close()
    
    @staticmethod
    def disp(log):
        """Print metrics to stdout"""
        log_keys = [k for k in log.keys()]
        log_keys.sort()
        '''
        print('***** Episode {}, Mean R = {:.1f} *****'.format(log['_Episode'],
                                                               log['_MeanReward']))
        for key in log_keys:
            if key[0] != '_':  # don't display log items with leading '_'
                print('{:s}: {:.3g}'.format(key, log[key]))
        '''
        print('log writed!')
        print('\n')
    
    def log(self, items):
        """ Update fields in log (does not write to file, used to collect updates.

        Args:
            items: dictionary of items to update
        """
        self.log_entry.update(items)
    
    def close(self):
        """ Close log file - log cannot be written after this """
        
        self.open_flag = False
        self.f.close()
    
    def log_table2csv(self, data, header=True):
        df = pd.DataFrame(data)
        df.to_csv(self.path, index=False, header=header)
    
    def log_csv2table(self):
        data = pd.read_csv(self.path, header=0, encoding='utf-8')
        return np.array(data)


import pickle

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