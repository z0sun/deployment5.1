from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect

client = SSHClient()

client.load_system_host_keys()

client.set_missing_host_key_policy(AutoAddPolicy())

client.connect("54.224.42.177", username="ubuntu")

stdin, stdout, stderr = client.exec_command('''cd c4_deployment-5
                                            chmod 700 Pkill.sh
                                            ./Pkill.sh
                                            python -m gunicorn app:app -b 0.0.0.0 --deamon
                                            ''')

#print(stdout.read().decode("utf-8"))
print(stderr.read().decode("utf-8"))
