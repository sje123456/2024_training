# 从database模块导入Session和engine
from database import Session, engine
from models import User,Post,Comment


session = Session()


# 创建一个新用户对象并设置其属性
user1 = User(username='john_doe', email='john@example.com')
 
# 将新用户对象添加到会话，表示要进行数据库插入操作
session.add(user1)
 
# 提交会话，将所有在此会话中的数据库操作提交到数据库
session.commit()
 
# 创建一篇新文章对象并设置其属性
post1 = Post(title='Introduction to SQLAlchemy', content='SQLAlchemy is a powerful ORM for Python.')
 
# 将文章的作者关联到之前创建的用户
post1.author = user1
 
# 将新文章对象添加到会话，表示要进行数据库插入操作
session.add(post1)
 
# 提交会话，将所有在此会话中的数据库操作提交到数据库
session.commit()
 
 
# 查询用户名为 'john_doe' 的用户，并打印其所有文章及评论
user = session.query(User).filter_by(username='john_doe').first()
print(f"User: {user.username}")
 