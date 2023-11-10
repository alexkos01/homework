from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///data.db')
Base = declarative_base()
class User(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    profession = Column(String)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


user_1 = User(id=1, name='Александр', profession='менеджер', age=25)
user_2 = User(id=2, name='Максим', profession='учитель', age=30)
user_3 = User(id=3, name='Олег', profession='строитель', age=32)
for i in [user_1, user_2, user_3]:
    session.add(i)
    session.commit()
session.close()
