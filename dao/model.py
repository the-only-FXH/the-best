#!/usr/bin/env python3
# coding = utf-8

import sys
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, String, Boolean, Text, TIMESTAMP
sys.path.append("..")
from config import configfile


engine = create_engine(
    configfile.getConfig("database","DATABASE_URL"),
    encoding='utf-8',
    echo=False)
Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

BaseModel = declarative_base()


class User(BaseModel):
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    __tablename__ = 'user'
    openid = Column(String(50), primary_key=True)
    username = Column(String(45))
    password = Column(String(45))
    # 是否绑定
    flag = Column(Boolean, nullable=False, default=True)


class Scores(BaseModel):
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    __tablename__ = 'score'
    openid = Column(String(50), primary_key=True)
    termStr = Column(String(15), primary_key=True)
    score = Column(Text)
    updateTime = Column(TIMESTAMP(True), nullable=False)


class KeyWord(BaseModel):
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8mb4'}
    __tablename__ = 'keyword'
    wordID = Column(String(20),primary_key=True)
    type = Column(String(20))
    result = Column(Text)


BaseModel.metadata.create_all(engine)
