import boto3
from botocore.exceptions import ClientError

#E-mail 전송 with SES
SENDER = "AWS5 <rlaghdrud94@naver.com>"
RECIPIENT = "rlaghdrud94@naver.com"
CONFIGURATION_SET = "SES-SNS"
AWS_REGION = "ap-northeast-2"
SUBJECT = "BTC Worldcup player added!"
BODY_TEXT = ("BTC Worldcup player added!"
            )
BODY_HTML = """<html>
<head></head>
<body>
  <h1>BTC Worldcup player Sign-up</h1>
  <p>This email was sent with AWS SES
    using the AWS SDK for Python(Boto3)
      from AWS5 Team.</p>
    <h3>User has been added.+1<h3>
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

#SMS 전송 with SNS
client = boto3.client(
"sns",
region_name="ap-northeast-1" # 도쿄
)

client.publish(
PhoneNumber="+8201026168709",
Message="회원이 추가되었습니다.+1"
)