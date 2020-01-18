import gearman
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser

home = expanduser('~')
pkeyfilepath = ""
mypkey = paramiko.RSAKey.from_private_key_file(home + "/" + pkeyfilepath)
sql_hostname = ''
sql_username = ''
sql_password = ''
sql_main_database = ''
sql_port = 3306
ssh_host = ''
ssh_user = 'ubuntu'
ssh_port = 22
sql_ip = '1.1.1.1.1'
print(home + "/" + pkeyfilepath)
server = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=mypkey,
        remote_bind_address=(sql_hostname, sql_port)
        )
server.start()

print( "connect at : 127.0.0.1:{}".format(server.local_bind_port))
gm_worker = gearman.GearmanWorker(['localhost:4730'])


def task_listener_reverse(gearman_worker, gearman_job):
    print ('reporting status')
    return reversed(gearman_job.data)

gm_worker.set_client_id('your_worker_client_id_name')
gm_worker.register_task('reverse', task_listener_reverse)
gm_worker.work()



# if you want to use ssh password use - ssh_password='your ssh password', bellow


    

    
    #  define method to handled 'reverse' work
    
