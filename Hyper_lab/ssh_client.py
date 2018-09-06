import paramiko

# ip = '2600:1f16:e7a:a088:51b:4369:e4e3:6ff8'
# name ='ubuntu'
# key_path='/home/drl/Jerry/tool/aws_ohio.pem'
#
# key=paramiko.RSAKey.from_private_key_file(key_path )
#
# #建立一个加密的管道
# scp=paramiko.Transport((ip,22))
#
#
# #建立连接
# scp.connect(username=name,pkey=key)
# #建立一个sftp客户端对象，通过ssh transport操作远程文件
# sftp=paramiko.SFTPClient.from_transport(scp)
# #Copy a remote file (remotepath) from the SFTP server to the local host
# sftp.get('/home/ubuntu/README','log-files/')
# # #Copy a local file (localpath) to the SFTP server as remotepath
# # sftp.put('/root/crash-6.1.6.tar.gz','/tmp/crash-6.1.6.tar.gz')
# scp.close()
# #2402:f000:6:3801:2d55:548f:d03c:ccad/64

import paramiko,datetime,os
import socket
hostname='2600:1f16:e7a:a088:51b:4369:e4e3:6ff8'
username='ubuntu'
password='361way'

key_path='/home/drl/Jerry/tool/aws_ohio.pem'

key=paramiko.RSAKey.from_private_key_file(key_path )


port=22
local_dir='/home/drl/PycharmProjects/DeployedProjects/CR_CPG/Hyper_lab/tmp'
remote_dir='/home/ubuntu/.mujoco/mjpro150'
# try:
#     t=paramiko.Transport((hostname,port))
#     t.connect(username=username,  pkey=key)
#     sftp=paramiko.SFTPClient.from_transport(t)
#     #files=sftp.listdir(dir_path)
#     files=sftp.listdir(remote_dir)
#     for f in files:
#         print('')
#         print( '#########################################')
#         print('Beginning to download file from %s %s ' % (hostname,datetime.datetime.now()) )
#         print( 'Downloading file:',os.path.join(remote_dir,f))
#         sftp.get(os.path.join(remote_dir,f),os.path.join(local_dir,f))#下载
#
#
#         #sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))#上传
#         print ('Download file success %s ' % datetime.datetime.now())
#         print ('')
#         print ('##########################################')
#     t.close()
#
#
#
# except Exception:
#     print ("connect error!")

import paramiko
import os
from stat import S_ISDIR as isdir


def down_from_remote(sftp_obj, remote_dir_name, local_dir_name):
    """远程下载文件"""
    remote_file = sftp_obj.stat(remote_dir_name)
    if isdir(remote_file.st_mode):
        # 文件夹，不能直接下载，需要继续循环
        check_local_dir(local_dir_name)
        print('开始下载文件夹：' + remote_dir_name)
        for remote_file_name in sftp.listdir(remote_dir_name):
            sub_remote = os.path.join(remote_dir_name, remote_file_name)
            sub_remote = sub_remote.replace('\\', '/')
            sub_local = os.path.join(local_dir_name, remote_file_name)
            sub_local = sub_local.replace('\\', '/')
            down_from_remote(sftp_obj, sub_remote, sub_local)
    else:
        # 文件，直接下载
        print('开始下载文件：' + remote_dir_name)
        sftp.get(remote_dir_name, local_dir_name)


def check_local_dir(local_dir_name):
    """本地文件夹是否存在，不存在则创建"""
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)


if __name__ == "__main__":
    """程序主入口"""
    # 服务器连接信息
    host_name = hostname
    user_name = username
    
    port = 22
    # 远程文件路径（需要绝对路径）
    remote_dir =  remote_dir
    # 本地文件存放路径（绝对路径或者相对路径都可以）
    local_dir = local_dir

    # 连接远程服务器
    t = paramiko.Transport((host_name, port))
    t.connect(username=user_name, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)

    # 远程文件开始下载
    down_from_remote(sftp, remote_dir, local_dir)

    # 关闭连接
    t.close()