# -*- coding: utf-8 -*-

from sqlalchemy import create_engine,text
from sqlalchemy.orm import scoped_session, sessionmaker

# 数据库连接字符串
DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/archemytest'

# 创建数据库引擎
engine = create_engine(DATABASE_URI, echo=True)
try:
    with engine.connect() as connection:
        # 执行一个简单的SQL查询，例如查询数据库的版本
        result = connection.execute(text("SELECT 1"))
        print("连接成功！")
        for row in result:
            print("数据库返回的结果是:", row)
except Exception as e:
    print(f"连接失败: {e}")
# 创建一个scoped session，它会在每个请求中使用线程局部模式
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# 导出Session和engine
__all__ = ['Session', 'engine']