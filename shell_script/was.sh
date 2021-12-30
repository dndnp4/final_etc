#!/bin/bash

yum update -y
yum install -y git
git clone https://github.com/dndnp4/final_flask.git ~/final_flask
pip3 install -r ~/final_flask/requirements.txt

cat > ~/final_flask/config.py << EOF
class FlaskConfig:
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:wlstjd11!@test.cenvguenpdcx.ap-northeast-2.rds.amazonaws.com:3306/test?charset=utf8" 
  SQLALCHEMY_ECHO = False
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = 'final'
  DEBUG = True

class AWSConfig:
  AWS_ACCESS_KEY = 'AKIAUZCKHZ5Q7TKM4LSG'
  AWS_SECRET_KEY = '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'
  ORIGIN_BUCKET_NAME = 'js-download'
  ORIGIN_BUCKET_DOMAIN = 'https://js-download.s3.ap-northeast-2.amazonaws.com'
  TUMB_BUCKET_NAME = 'js-download-resized'
  TUMB_BUCKET_DOMAIN = 'https://js-download-resized.s3.ap-northeast-2.amazonaws.com'

class CommonConfig:
  SALT_LENGTH = 32
  HASH_NAME = 'sha256'
  DK_LEN = 10000
EOF

python3 ~/final_flask/app.py