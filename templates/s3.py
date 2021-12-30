from connection import s3_connection
from config import BUCKET_NAME

s3 = s3_connection()
#s3.put_object(
 # Bucket = 'aws-py'
 # Body = '01.jpg'
 # Key = 's3://aws5-py/aws5-py/'
 # )
  
file_name = '(./upload/01.jpg)'
bucket = 'aws5-py'
key = '01.jpg'
res = s3.upload_file(file_name, bucket, key)