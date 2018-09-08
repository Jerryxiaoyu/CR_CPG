from utils.instrument import VariantGenerator, variant, IO
import os
from datetime import datetime
import shutil
import glob
import paramiko
import utils.ssh as ssh
class VG(VariantGenerator):
    
    @variant
    def env_name(self):
        return ['CellrobotSnakeEnv-v0', ]  #   'CellrobotEnv-v0' , 'Cellrobot2Env-v0', 'CellrobotSnakeEnv-v0'  , 'CellrobotSnake2Env-v0','CellrobotButterflyEnv-v0', 'CellrobotBigdog2Env-v0'
    @variant
    def pop_size(self):
        return [300]
    
    
    @variant
    def max_gen(self):
        return [ 40 ]

    @variant
    def CXPB(self):
        return [0.8]
    
    @variant
    def MUTPB(self):
        return [ 0.1 ]

    @variant
    def gain_max(self):
        return [ 1 ]

    @variant
    def bias_max(self):
        return [0.0]

    @variant
    def phase_max(self):
        return [90.0]
    
    @variant
    def task_mode(self):
        return [ '2_sin', '5_sin' ]#  '2' ,'3', '4', '5', '2_sin', '5_sin'
    @variant
    def max_time(self):
        return [ 10.0 ]

    @variant
    def fitness_mode(self):
        return [  4 ]
 
ssh_FLAG = True
exp_id = 8
EXP_NAME ='GA_CPG'
group_note ="************ABOUT THIS EXPERIMENT****************\n" \
            "测试所有环境是否可用!" \
            "只针对Bigsnake 不同的fitness"
        #    "测试不同CPG权重对进化过程的影响[1 1 -1 -1 1] fitness 不同"
            
            
variants = VG().variants()
num=0
for v in variants:
    num +=1
    print('exp{}: '.format(num), v)

# save gourp parms
exp_group_dir = datetime.now().strftime("%b_%d")+EXP_NAME+'_Exp{}'.format(exp_id)
group_dir = os.path.join('log-files', exp_group_dir)
os.makedirs(group_dir)

filenames = glob.glob('*.py')  # put copy of all python files in log_dir
for filename in filenames:  # for reference
    shutil.copy(filename, group_dir)

variants = VG().variants()
num = 0
param_dict = {}
for v in variants:
    num += 1
    print('exp{}: '.format(num), v)
    parm = v
    parm = dict(parm, **v)
    param_d = {'exp{}'.format(num): parm}
    param_dict.update(param_d)

IO('log-files/' + exp_group_dir + '/exp_id{}_param.pkl'.format(exp_id)).to_pickle(param_dict)
print(' Parameters is saved : exp_id{}_param.pkl'.format(exp_id))
# save args prameters
with open(group_dir + '/readme.txt', 'wt') as f:
    print("Welcome to Jerry's lab\n", file=f)
    print(group_note, file=f)
    
num_exp =0

seed =1

# SSH Config
hostname = '2402:f000:6:3801:2d55:548f:d03c:ccad'#'2600:1f16:e7a:a088:805d:16d6:f387:62e5'
username = 'drl'
key_path = '/home/ubuntu/.ssh/id_rsa_dl'

port = 22


for v in variants:
    num_exp += 1
    print(v)
    # load parm
    env_name = v['env_name']
    pop_size = v['pop_size']
    max_gen = v['max_gen']
    CXPB = v['CXPB']
    MUTPB = v['MUTPB']
    gain_max = v['gain_max']
  
    task_mode = v['task_mode']
    max_time = v['max_time']
    fitness_mode = v['fitness_mode']
    bias_max = v['bias_max']
    phase_max = v['phase_max']
    

    os.system("python3 -m scoop GA_examples/GA_main.py " +
              " --seed " + str(seed) +
              " --env_name " + str(env_name) +
              " --pop_size " + str(pop_size) +
              " --max_gen " + str(max_gen) +
              " --CXPB " + str(CXPB) +
              " --MUTPB " + str(MUTPB) +
              " --gain_max " + str(gain_max) +
              " --task_mode " + str(task_mode) +
              " --max_time " + str(max_time) +
              " --fitness_mode " + str(fitness_mode) +
              " --phase_max " + str(phase_max) +
              " --bias_max " + str(bias_max) +
              " --exp_group_dir " + str(exp_group_dir)
              )
    if ssh_FLAG:
        local_dir = os.path.abspath(group_dir)
        remote_dir = '/home/drl/PycharmProjects/DeployedProjects/CR_CPG/Hyper_lab/log-files/AWS_logfiles/'+exp_group_dir+'/'
        ssh.upload(local_dir, remote_dir, hostname=hostname , port=port , username=username ,
                   pkey_path=key_path)
     