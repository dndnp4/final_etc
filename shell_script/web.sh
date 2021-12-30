#!/bin/bash

# set apache
yum update -y
yum install -y httpd git

cat > /etc/httpd/conf.d/final.conf << EOF
<Directorymatch "^/.*/\.git/">
  Order 'deny,allow'
  Deny from all
</Directorymatch>
<VirtualHost *:80>
  ProxyPassMatch /(signup|signin|game|result|uploader)$ http://localhost:5000/$1
  ProxyPassReverse / http://localhost:5000/
</VirtualHost>
EOF

# set html
git clone https://github.com/dndnp4/final_apache.git temp
mv temp/* /var/www/html
rm -rf temp
touch /var/www/html/health.html

systemctl restart httpd
systemctl enable httpd

yum install -y automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel
git clone https://github.com/s3fs-fuse/s3fs-fuse.git ~/s3fs-fuse
cd ~/s3fs-fuse
./autogen.sh
./configure
make
make install

# cat > ~/.passwd-s3fs << EOF
# AKIAUZCKHZ5Q7TKM4LSG:Cz0T7nqaq9xsSVfSqP/w16XPY37+XZx/DoFLYC+8
# EOF

# touch ~/.passwd-s3fs
# chmod 600 ~/.passwd-s3fs
mkdir /mnt/s3-mount
echo PATH=$PATH:/usr/local/bin >> ~/.bashrc
source ~/.bashrc
s3fs "test-web-mount123" /mnt/s3-mount -o iam_role=auto -o allow_other -o umask=000