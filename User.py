from __future__ import annotations

from marshmallows import Schema, fields, validate, ValidationError, types, post_load, post_dump
from collections import OrderedDict
import datetime as dt
class User:
    def __init__(self, id, passwd, nickname = None):
        self.userID = id
        self.userPW = passwd
        self.userNN = nickname
        self.created_at = dt.datetime.now() # 유저 정보 생성 시간을 저장한다.
        
    def __repr__(self):
        return "<User(name={self.userNN!r})>".format(self=self)
    
def is_alnum(value): # value에 특수문자와 공백이 존재하면 에러 발생 
    if not value.isalnum():
        raise ValidationError("특수문자와 공백은 사용할 수 없습니다.")
    
validator = validate.And(validate.And(validate.Length(min=4, max=8), is_alnum)) # 입력되는 데이터의 길이가 4~8이 아니거나 특수문자나 공백을 보유하면 에러 발생
class UserSchema(Schema):
    # userID = fields.Str(validate=validate.Length(min=4, max=8))
    userID = fields.Str(validate=validator)
    userPW = fields.Str(validate=validator)
    userNN = fields.Str(validate=validator)
    created_at = fields.DateTime()
    class Meta:
        ordered = True # 직렬화 시 데이터의 순서를 선언한 순서대로 정렬해준다. 대신 OrderedDict의 형태로 반환.
         
    @post_dump
    def make_dict(self, data, **kwargs):
        return dict(OrderedDict(data)) # Meta클래스에서 ordered를 선언해 OrderedDict의 형태로 반환하기 때문에 Dict형식으로 변경하는 전처리함수이다.
    