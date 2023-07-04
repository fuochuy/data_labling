from sqlalchemy import Column, Integer

from db.base_class import Base


class UserProject(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    project_id = Column(Integer)
