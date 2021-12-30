#!/bin/bash

yum install -y automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel
git clone https://github.com/s3fs-fuse/s3fs-fuse.git ~/s3fs-fuse
cd ~/s3fs-fuse
./autogen.sh
./configure
make
make install

mkdir /mnt/s3-mount
echo PATH=$PATH:/usr/local/bin >> ~/.bashrc
source ~/.bashrc
s3fs "test-web-mount123" /mnt/s3-mount -o iam_role=auto -o allow_other -o umask=000