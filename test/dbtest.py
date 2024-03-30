from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建 SQLite 数据库连接
engine = create_engine('sqlite:///example.db', echo=True)

# 创建基类
Base = declarative_base()

# 定义数据模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# 创建数据表
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Alice', age=30)
session.add(new_user)

# 添加数据
new_user = User(name='tom', age=33)
session.add(new_user)
# 添加数据
new_user = User(name='tom1', age=36)
session.add(new_user)
session.commit()
# 查询数据
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# 更新数据
user_to_update = session.query(User).filter_by(name='Alice').first()
user_to_update.age = 31
session.commit()

