#/anaconda3/envs/gym/lib/python3.5/site-packages/my_gym_envs/mujoco/assets/cellrobot
# -*- coding: utf-8 -*-
import paramiko
import datetime
import os


def upload(local_dir, remote_dir, hostname, port, username, pkey):
    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, pkey=pkey)
        sftp = paramiko.SFTPClient.from_transport(t)
        print('upload file start %s ' % datetime.datetime.now())
        for root, dirs, files in os.walk(local_dir):
            print('[%s][%s][%s]' % (root, dirs, files))
            for filespath in files:
                local_file = os.path.join(root, filespath)
                print(11, '[%s][%s][%s][%s]' % (root, filespath, local_file, local_dir))
                a = local_file.replace(local_dir, '').replace('\\', '/').lstrip('/')
                print('01', a, '[%s]' % remote_dir)
                remote_file = os.path.join(remote_dir, a).replace('\\', '/')
                print(22, remote_file)
                try:
                    sftp.put(local_file, remote_file)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file, remote_file)
                    print("66 upload %s to remote %s" % (local_file, remote_file))
            for name in dirs:
                local_path = os.path.join(root, name)
                print(0, local_path, local_dir)
                a = local_path.replace(local_dir, '').replace('\\', '/').lstrip('/')
                print(1, a)
                print(1, remote_dir)
                # remote_path = os.path.join(remote_dir, a).replace('\\', '/')
                remote_path = remote_dir + a
                print(33, remote_path)
                try:
                    sftp.mkdir(remote_path)
                    print(44, "mkdir path %s" % remote_path)
                except Exception as e:
                    print(55, e)
        print('77,upload file success %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(88, e)


if __name__ == '__main__':
    # 选择上传到那个服务器
    servers_list =[0]

    hostname = ['2402:f000:6:3801:ee1c:d67d:4f92:55ad' ]
    username = ['drl']
    port = [22]
    for num in servers_list:
     
        key_path = '/home/ubuntu/.ssh/id_rsa_dl'
        key = paramiko.RSAKey.from_private_key_file(key_path)
        #dir_list = ['Sep_08GA_CPG_Exp11', 'Sep_08PSO_CPG_Exp2']
        dir_list = ['Sep_08GA_CPG_Exp10']
        for exp_group_dir in dir_list:
            local_dir = '/home/ubuntu/jerry/projects/CR_CPG/log-files/'+exp_group_dir+'/'
            remote_dir = '/home/drl/PycharmProjects/DeployedProjects/CR_CPG/Hyper_lab/log-files/AWS_logfiles/'+exp_group_dir+'/'
            print('Uploading server No.{}...'.format(num))
            upload(local_dir, remote_dir, hostname=hostname[num], port=port[num], username=username[num],
                   pkey=key)
