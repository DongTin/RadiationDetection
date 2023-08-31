from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from config.database import settings

USER = settings.USER
PWD = settings.PASSWORD
DB_NAME = settings.DATABASE

print(USER, PWD, DB_NAME)

SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{USER}:{PWD}@localhost:3306/{DB_NAME}?charset=utf8&auth_plugin=mysql_native_password'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

db = SessionLocal()


async def reset_db_state():
    # 重置数据库连接的状态
    engine.dispose()
    engine.connect()


# 连接测试
if __name__ == '__main__':
    db = SessionLocal()
    print('数据库连接成功')
    db.close()
    print('数据库关闭成功')