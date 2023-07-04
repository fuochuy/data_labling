import datetime
from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime


class Project(Base):
    projectId = Column(Integer, primary_key=True, index=True)
    projectName = Column(String, unique=True, nullable=False, index=True)
    projectType = Column(String, nullable=False, unique=True)
    created_user = Column(String, nullable=False, unique=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    updated_user = Column(String, nullable=False, unique=True)
    updated_date = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String, nullable=False, unique=True)
    status = Column(String)
