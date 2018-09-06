import paramiko,datetime,os

port=22

hostname='2600:1f16:e7a:a088:805d:16d6:f387:62e5'
username='ubuntu'


key_path='/home/drl/Jerry/tool/aws_ohio.pem'
key=paramiko.RSAKey.from_private_key_file(key_path )


def upload(local_dir,remote_dir):
    try:
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,pkey=key)
        sftp=paramiko.SFTPClient.from_transport(t)
        print('upload file start %s ' % datetime.datetime.now() )
        for root,dirs,files in os.walk(local_dir):
            for filespath in files:
                local_file = os.path.join(root,filespath)
                a = local_file.replace(local_dir,'')
                remote_file = os.path.join(remote_dir,a)
                try:
                    sftp.put(local_file,remote_file)
                except:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file,remote_file)
                print("upload %s to remote %s" % (local_file,remote_file))
            for name in dirs:
                local_path = os.path.join(root,name)
                a = local_path.replace(local_dir,'')
                remote_path = os.path.join(remote_dir,a)
                try:
                    sftp.mkdir(remote_path)
                    print("mkdir path %s" % remote_path)
                except Exception as e:
                    print(e)
        print ('upload file success %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(e)
if __name__=='__main__':
    local_dir='/home/drl/PycharmProjects/DeployedProjects/CR_CPG/Hyper_lab/tmp/model'
    remote_dir='/home/ubuntu/jerry/examples/tmp'
    upload(local_dir,remote_dir)