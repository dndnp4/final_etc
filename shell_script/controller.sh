#!/bin/bash

sudo su
yum install gcc openssl-devel bzip2-devel libffi-devel -y
cd /root
wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz
tar xzf Python-3.8.1.tgz
cd Python-3.8.1
./configure --enable-optimizations
make install
pip3.8 install ansible
pip3.8 install boto3

echo -e "\nPATH=\$PATH:/usr/local/bin" >> ~/.bashrc
source ~/.bashrc

mkdir ~/ansible
cd ~/ansible
cat > aws_ec2.yml << EOF
plugin: aws_ec2
regions:
  - ap-northeast-2
keyed_groups:
 - key: tags.Role
filters:
  instance-state-name: running
compose:
  ansible_host: private_ip_address
EOF

# copy from s3.......

cat > ~/.ssh/id_rsa << EOF
{key}
EOF

cat > ansible.cfg << EOF
[defaults]
host_key_checking = False
inventory = /root/ansible/aws_ec2.yml
interpreter_python = auto_silent
private_key_file = /root/.ssh/id_rsa
remote_user=ec2-user

[privilege_escalation]
become = true
become_method = sudo
become_user = root
become_ask_pass = false
EOF

chmod 400 ~/.ssh/id_rsa

yum install -y automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel
git clone https://github.com/s3fs-fuse/s3fs-fuse.git ~/s3fs-fuse
cd ~/s3fs-fuse
./autogen.sh
./configure
make
make install

mkdir /mnt/s3-mount
s3fs "bucket-name" /mnt/s3-mount -o iam_role=auto -o allow_other -o umask=000
