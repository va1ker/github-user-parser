from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String)
    user_id = Column(Integer)
    node_id = Column(String)
    avatar_url = Column(String)
    followers_url = Column(String)
    starred_url = Column(String)
    repos_url = Column(String)
    role = Column(String)
    site_admin = Column(Boolean)
