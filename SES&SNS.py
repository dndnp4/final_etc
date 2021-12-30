import boto3
from botocore.exceptions import ClientError

SENDER = "AWS5  <rlaghdrud94@naver.com>"
RECIPIENT = "rlaghdrud94@naver.com"
CONFIGURATION_SET = "zzaeha-test"
AWS_REGION = "ap-northeast-2"
SUBJECT = "AWS5-Project-Signup!"
BODY_TEXT = ("Player Sign-up!"
            )
BODY_HTML = """<html>
<head></head>
<body>
  <h1>AWS5-Project player Sign-up</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>AWS SES</a>
    using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>
      from AWS5 Team.</p>
</body>
</html>
            """
CHARSET = "UTF-8"
client = boto3.client('ses',region_name=AWS_REGION)
try:
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        ConfigurationSetName=CONFIGURATION_SET,
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])

client = boto3.client(
"sns",
aws_access_key_id="AKIAUN43WGHHHXMUSOEJ",
aws_secret_access_key="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",
region_name="ap-northeast-1" # 도쿄
)

# 주제나 구독자를 정하지 않으면 다음과 같이 간단하게 구현 가능
client.publish(
PhoneNumber="+8201026168709",
Message="회원이 추가되었습니다.+1"
)





