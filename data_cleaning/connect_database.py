# -*- coding: utf-8 -*-


from sqlalchemy import create_engine,text
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager

# 数据库连接字符串
DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/DAIR_V2X'

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
    
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

@contextmanager
def session_scope():
    """提供一个事务的会话范围。"""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()  # 发生异常时回滚
        raise
    finally:
        session.close()  # 确保最后关闭 session

# 导出Session和engine
__all__ = [ 'engine','session_scope']