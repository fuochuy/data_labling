import datetime
from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime


class Project(Base):
    projectId = Column(Integer, primary_key=True, index=True)
    projectName = Column(String, nullable=False, index=True)
    projectType = Column(String, nullable=False)
    created_user = Column(String, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    updated_user = Column(String, nullable=False)
    updated_date = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String, nullable=False)
    status = Column(String)
