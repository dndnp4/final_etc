from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

#업로드 html 랜더링
@app.route('/upload')
def render_file():
  return render_template('aws5_upload.html')

#파일 업로드 처리
@app.route('/uploader', methods=['GET','POST'])
def uploader_file():
  if request.method == 'POST':
    f = request.files['file']
    #저장할 경로 + 파일명
    f.save('./upload/' + secure_filename(f.filename))
    return 'uploads 디렉토리 -> 파일 업로드 성공!'

if __name__=='__main__':
  app.run(debug = True)