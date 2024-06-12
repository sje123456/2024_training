import redis
import time
# 创建Redis连接
r = redis.Redis(host='localhost', port=6379, db=0)

# 数据类型示例

# 字符串
r.set('user:1', 'John Doe')
user_name = r.get('user:1')
print(f"User name: {user_name.decode('utf-8')}")

# 列表
r.rpush('todo:1', 'buy milk', 'call mom', 'go for a run')
next_task = r.lpop('todo:1')
print(f"Next task: {next_task.decode('utf-8')}")

# 集合
r.sadd('favorite_colors:1', 'blue', 'green', 'red')
favorite_colors = r.smembers('favorite_colors:1')
print(f"Favorite colors: {favorite_colors}")

# 有序集合
r.zadd('ranked_tasks:1', {'task1': 1, 'task2': 2, 'task3': 3})
ranked_score = r.zscore('ranked_tasks:1', 'task1')
print(f"Ranked score: {ranked_score}")

# 哈希
r.hset('user_info:1', 'name', 'John Doe')
r.hset('user_info:1', 'age', '30')
user_info = r.hgetall('user_info:1')
print(f"User info: {user_info}")

# 事务示例
trans = r.pipeline(transaction='True')
trans.multi()
trans.set('trans_key', 'trans_value')
trans_result = trans.execute()
print(trans_result)

# 管道示例
p = r.pipeline(transaction=False)
p.set('pipeline_key', 'pipeline_value')
p.rpush('pipeline_list', 'buy milk', 'call mom', 'go for a run')
p.sadd('pipeline_set', 'blue', 'green', 'red')
p.zadd('pipeline_zset', {'task1': 1, 'task2': 2, 'task3': 3})
result = p.execute()
print(result)

# 设置过期时间示例

# 创建Redis连接
r.setex('session_key:1', 2, 'This session key will expire in 2 seconds')

# 当场获取结果
session_key_value = r.get('session_key:1')
print(f"Session key value (before delay): {session_key_value.decode('utf-8')}")

# 暂停2秒
time.sleep(2)

# 再次获取结果
session_key_value_after_delay = r.get('session_key:1')
print(f"Session key value (after 2 seconds delay): {session_key_value_after_delay.decode('utf-8')}")

