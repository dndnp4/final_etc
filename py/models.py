import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() # SQLAlchemy를 인스턴스화

class Users(db.Model):

    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    user_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(20))
    pw = db.Column(db.String(100))
    salt = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=datetime.now().replace(microsecond=0))

    def __init__(self,user_id, id, pw, salt, date):
        self.user_id = user_id
        self.id = id
        self.pw = pw
        self.salt = salt
        self.date = date

    def search_events_by_id(id, get):
    
        if get == 'json' : 
            result = Users.query.filter_by(id=id).all()
        else : result = Users.query.filter_by(id=id).first()

        return result

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

    def __repr__(self):
    
        data = {
            'user_id' : self.user_id,
            'id' : self.id,
            'pw' : self.pw,
            'salt' : self.salt,
            'date' : str(self.date)
        }
        json_data = json.dumps(data, indent = 4)

        return json_data
        # return 'user_id : %s, id : %s, pw : %s, salt : %s, date : %s' % (self.user_id, self.id, self.pw, self.salt, self.date)

class Game_Result(db.Model):

    __tablename__ = 'game_result'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    game_id = db.Column(db.String(40), primary_key=True)
    user_id = db.Column(db.Integer)
    file_id = db.Column(db.Integer)
    rou = db.Column(db.Integer)
    state = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, game_id, user_id, file_id, rou, state, date):
        self.game_id = game_id
        self.user_id = user_id
        self.file_id = file_id
        self.rou = rou
        self.state = state
        self.date = date

    def search_events_by_game_id(game_id, get):
    
        if get == 'json' : 
            result = Game_Result.query.filter_by(game_id=game_id).all()
        else : result = Game_Result.query.filter_by(game_id=game_id).first()
        
        return result

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

    def __repr__(self):

        data = {
            'game_id' : self.game_id,
            'user_id' : self.user_id,
            'file_id' : self.file_id,
            'rou' : self.rou,
            'state' : self.state,
            'date' : str(self.date)
        }
        json_data = json.dumps(data)

        return json_data
        # return 'game_id : %s, user_id : %s, file_id : %s, round : %s, state : %s, date : %s' % (self.game_id, self.user_id, self.file_id, self.round, self.state, self.date)

class File(db.Model):

    __tablename__ = 'file'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    file_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(20))
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, file_id, name, type, date):
        self.file_id = file_id
        self.name = name
        self.type = type
        self.date = date

    def search_events_by_file_id(file_id, get):

        if get == 'json' : 
            result = File.query.filter_by(file_id=file_id).all()
        else : 
            result = File.query.filter_by(file_id=file_id).first()
        
        return result

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

    def __repr__(self):

        data = {
            'file_id' : self.file_id,
            'name' : self.name,
            'type' : self.type,
            'date' : str(self.date)
        }
        json_data = json.dumps(data)

        return json_data
         # return 'file_id : %s, name : %s, type : %s, date : %s' % (self.file_id, self.name, self.type, self.date)
    