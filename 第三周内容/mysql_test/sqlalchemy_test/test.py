# -*- coding: utf-8 -*-

# 导入必要的模块
from sqlalchemy import create_engine,text
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root:root@localhost:3306/archemytest')

                    
# 尝试连接数据库
try:
    with engine.connect() as connection:
        # 执行一个简单的SQL查询，例如查询数据库的版本
        result = connection.execute(text("SELECT 1"))
        print("连接成功！")
        for row in result:
            print("数据库返回的结果是:", row)
except Exception as e:
    print(f"连接失败: {e}")
 

# 创建一个基类，用于定义数据模型的基本结构
Base = declarative_base()
 
# 定义一个数据模型类，对应数据库中的 'users' 表
class User(Base):
    # 定义表名
    __tablename__ = 'users'
 
    # 定义列：id，是整数类型，主键（primary_key=True），并使用 Sequence 生成唯一标识
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
 
    # 定义列：name，是字符串类型，最大长度为50
    name = Column(String(50))
 
    # 定义列：age，是整数类型
    age = Column(Integer)
    
#Base.metadata.create_all(engine)


# 导入创建会话的模块
from sqlalchemy.orm import sessionmaker
 
# 使用 sessionmaker 创建一个会话类 Session，并绑定到数据库引擎（bind=engine）
Session = sessionmaker(bind=engine)
 
# 创建一个实例化的会话对象 session
session = Session()
 
# 创建一个新的 User 实例，即要插入到数据库中的新用户
new_user = User(name='John Doe', age=30)
 
# 将新用户添加到会话中，即将其添加到数据库操作队列中
session.add(new_user)
 
# 提交会话，将所有在此会话中的数据库操作提交到数据库
session.commit()


# 使用查询语句
result = engine.execute('SELECT * FROM users')
for row in result:
   print(f"Core查询结果: {row}")
# 使用ORM查询接口
users = session.query(User).all()
for user in users:
    print(f"ORM查询结果: {user.id}, {user.name}") 
session.close()
Session.remove()