pipeline {
agent any
stages {
stage ('Build') {
steps {
sh '''#!/bin/bash
python3.8 -m venv test1
source test1/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
'''
}
}
stage ('test') {
steps {
sh '''#!/bin/bash
source test1/bin/activate
pip install pytest
py.test --verbose --junit-xml test-reports/results.xml
'''
}
post{
always {
junit 'test-reports/results.xml'
}
}
}
stage ('Clean') {
steps {
sh '''#!/bin/bash
if [[ $(ps -aux | grep -i "gunicorn" | tr -s " " | head -n 1 | cut -d " " -f 2) != 0 ]]
then
ps aux | grep -i "gunicorn" | tr -s " " | head -n 1 | cut -d " " -f 2 > pid.txt
kill $(cat pid.txt)
exit 0
fi
'''
}
}
stage ('Deploy') {
steps {
keepRunning {
sh '''#!/bin/bash
pip install -r requirements.txt
pip install gunicorn
export test1=joetyi77
python3.8 -m gunicorn -w 4 application:app -b 0.0.0.0 --daemon
'''
}
}
}
}
}
