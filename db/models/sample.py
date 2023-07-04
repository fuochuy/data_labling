from datetime import datetime

from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Sample(Base):
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    sample = Column(String)
    label = Column(String)
    status = Column(Boolean(), default=False, index=True)
    created_user = Column(Integer)
    updated_user = Column(Integer)
    created_at = Column(datetime)
    updated_at = Column(datetime)
