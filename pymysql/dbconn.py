from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:123456@localhost/tarena?charset=utf8',
    encoding='utf8', echo=True
)

Base = declarative_base()
Session = sessionmaker(bin=engine)


class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return '[部门ID：%s, 部门名称：%s]' % (self.dep_id, self.dep_name)


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(6))
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '员工：%s' % self.name


if __name__ == '__main__':
    Base.metadata.create_all(engine)
