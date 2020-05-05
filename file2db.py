import yaml
import json
import subprocess as sp
import logging
import xml.etree.ElementTree as ET
import pandas as pd

# create logger with 'spam_application'
logger = logging.getLogger('file2db.py')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('file2db.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')

'''
# https://janakiev.com/blog/python-shell-commands/
ssh = sp.Popen(['ssh', 'dylan@192.168.0.10'],
                stdin =sp.PIPE,
                stdout=sp.PIPE,
                stderr=sp.PIPE,
                universal_newlines=True,
                bufsize=0)

#send ssh commans to stdin
ssh.stdin.write('uname -a¥n')
ssh.stdin.write('uptime¥n')
ssh.stdin.close()

#fetch output
print(ssh.stderr)
for line in ssh.stderr:
    print(line)
for line in ssh.stdout:
    print(line.strip())
# ----------------------------
'''
# ssh without Pseudo-terminal 
#ssh = sp.runPopen(['ssh', '-tt', 'dylan@192.168.0.10', 'bash -s', "<<< '/bin/ls > ls.log'"],
#str_script = "<<< '/bin/ls > ls.log'"
# str_script = "<<< 'uname -a'"
script = """ '
    uname -a;
    uptime;
    date;
   ' """
#print('script:' + script.strip('\n'))
args_ = ['scp dylan@192.168.0.10:/home/dylan/test_ftp/2020* ./test_ftp/']
#sh = sp.run(['ssh', 'dylan@192.168.0.10', 'bash -s', '<<<', script],
sh = sp.run(['scp', 'dylan@192.168.0.10:/home/dylan/test_ftp/2020*', './test_ftp/']
                ,capture_output=True
                ,text=True
                ,timeout=5)
                #,bufsize=0)
#ssh.stdin.close()
#logger.info(sh.args)
logger.info(sh)
#if(sh.returncode != 0)
for line in sh.stderr.splitlines():
    logger.info(line.strip())
for line in sh.stdout.splitlines():
    logger.info(line.strip())

# for line in sh.stderr:
#     logger.error(line.strip())
    
# for line in sh.stdout:
#     logger.info(line.strip())
#sp.run(['ls', '-l'])
print('------------')

sh = sp.Popen(['scp','dylan@192.168.0.10:/home/dylan/test_ftp/2020*', './test_ftp/'],
                stdin =None,
                stdout=sp.PIPE,
                stderr=sp.PIPE,
                universal_newlines=True,
                bufsize=0)


for line in sh.stderr:
    logger.error(line.strip())
    
for line in sh.stdout:
    logger.info(line.strip())

'''
def xml2df(xml_data):
    root = ET.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    df = pd.DataFrame(all_records)
    return df

# load XML to dataframe (gotta be small)
xml_data = open('./test_ftp/data001.xml').read()
df = xml2df(xml_data)
print(df)
df.to_csv('test_ftp/data001.csv')
'''

# date '+%Y-%m-%d %H:%M:%S_%N' > $(date +"%Y-%m-%d-%H:%M:%S_%N").log

# 1. job001: get files from sftp server
# 2. job002: put files to web server and move to uploaded directory
# 3. job003: download files as zip from web server
# 4. job004: extract files from zip
# 5. job005: put fils to sftp server
# 6. feedback to 

