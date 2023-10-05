from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect

client = SSHClient()

client.load_system_host_keys()
client.load_host_keys('/home/ubuntu/.ssh/known_hosts')

client.set_missing_host_key_policy(AutoAddPolicy())

client.connect("54.224.42.177", username="ubuntu")

stdin, stdout, stderr = client.exec_command('''sudo apt update
                                            sudo apt install -y software-properties-common
                                            sudo add-apt-repository -y ppa:deadsnakes/ppa
                                            sudo apt install -y python3.7
                                            sudo apt install -y python3.7-venv
                                            python3.7 -m venv test
                                            source test/bin/activate
                                            git clone https://github.com/kura-labs-org/c4_deployment-5.git
                                            cd c4_deployment-5
                                            pip install -r requirements.txt
                                            pip install gunicorn
                                            python database.py
                                            python load_data.py
                                            python -m gunicorn app:app -b 0.0.0.0 --deamon
                                            ''')

#print(stdout.read().decode("utf-8"))
print(stderr.read().decode("utf-8"))
