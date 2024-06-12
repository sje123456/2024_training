# -*- coding: utf-8 -*-

# 导入 SQLAlchemy 中所需的模块
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from database import engine
# 创建一个基类，用于定义数据模型的基本结构
Base = declarative_base()
 
# 定义数据模型类 User，对应数据库中的 'users' 表
class User(Base):
    __tablename__ = 'users'
    
    # 定义列：id，是整数类型，作为主键
    id = Column(Integer, primary_key=True)
    
    # 定义列：username，是字符串类型，最大长度为50，唯一且不可为空
    username = Column(String(50), unique=True, nullable=False)
    
    # 定义列：email，是字符串类型，最大长度为100，唯一且不可为空
    email = Column(String(100), unique=True, nullable=False)
    
 
# 定义数据模型类 Post，对应数据库中的 'posts' 表
class Post(Base):
    __tablename__ = 'posts'
    
    # 定义列：id，是整数类型，作为主键
    id = Column(Integer, primary_key=True)
    
    # 定义列：title，是字符串类型，最大长度为100，不可为空
    title = Column(String(100), nullable=False)
    
    # 定义列：content，是文本类型，不可为空
    content = Column(Text, nullable=False)
    
    # 定义列：user_id，是整数类型，外键关联到 'users' 表的 id 列
    user_id = Column(Integer, ForeignKey('users.id'))
    
   
 
# 定义数据模型类 Comment，对应数据库中的 'comments' 表
class Comment(Base):
    __tablename__ = 'comments'
    
    # 定义列：id，是整数类型，作为主键
    id = Column(Integer, primary_key=True)
    
    # 定义列：text，是文本类型，不可为空
    text = Column(Text, nullable=False)
    
    # 定义列：user_id，是整数类型，外键关联到 'users' 表的 id 列
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # 定义列：post_id，是整数类型，外键关联到 'posts' 表的 id 列
    post_id = Column(Integer, ForeignKey('posts.id'))
    
  

from sqlalchemy.ext.declarative import declarative_base

#Base.metadata.create_all(engine)
