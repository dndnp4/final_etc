import os
import json
from models import db, Users, Game_Result, File
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__) 

# mapping class에 정의된 테이블들이 DB와 연결
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:Cloud12345@a5-db.cyhobl9qzike.ap-northeast-2.rds.amazonaws.com:3306/a5?charset=utf8" 
# 터미널에 진행 과정 출력
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
app.config['SECRET_KEY'] = 'asdf'

# db set 
db.init_app(app) 
db.app = app
db.create_all()

def Users_SELECT_id(id, get='all') :
  result = Users.search_events_by_id(id, get)
  if result != None :
    if get == 'user_id' :
      result = result.user_id
    elif get == 'id' :
      result = result.id 
    elif get == 'pw' :
      result = result.pw
    elif get == 'salt' :
      result = result.salt
    elif get == 'date' :
      result = result.date
    elif get == 'json' :
      result = result[0]

  return result

def Users_INSERT(user_id, id, pw, salt) :

  if id == Users_SELECT_id(id, 'id') :
    return False

  record = Users(user_id, id, pw, salt ,datetime.now().replace(microsecond=0))
  db.session.add(record)
  db.session.commit()

def Game_Result_SELECT_game_id(game_id, get='all') :
  result = Game_Result.search_events_by_game_id(game_id, get)
  if result != None :
    if get == 'game_id' :
      result = result.game_id
    elif get == 'user_id' :
      result = result.user_id
    elif get == 'file_id' :
      result = result.file_id
    elif get == 'rou' :
      result = result.rou
    elif get == 'state' :
      result = result.state
    elif get == 'date' :
      result = result.date
    elif get == 'json' :
      result = result[0]

  return result

def Game_Result_INSERT(game_id, user_id, file_id, rou, state) :

  if game_id == Game_Result_SELECT_game_id(game_id, 'game_id') :
    return False

  record = Game_Result(game_id, user_id, file_id, rou, state ,datetime.now().replace(microsecond=0))
  db.session.add(record)
  db.session.commit()

def File_SELECT_file_id(file_id, get='all') :
  result = File.search_events_by_file_id(file_id, get)
  if result != None :
    if get == 'file_id' :
      result = result.file_id
    elif get == 'name' :
      result = result.name
    elif get == 'type' :
      result = result.type
    elif get == 'date' :
      result = result.date
    elif get == 'json' :
      result = result[0]

  return result

def File_INSERT(file_id, name, type) :

  if file_id == File_SELECT_file_id(file_id, 'file_id') :
    return False

  record = File(file_id, name, type ,datetime.now().replace(microsecond=0))
  db.session.add(record)
  db.session.commit()


if __name__ == '__main__':
  pass

  
  
