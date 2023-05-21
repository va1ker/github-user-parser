from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import User

DATABASE_NAME = "users.sqlite"

engine = create_engine(f"sqlite:///{DATABASE_NAME}")
session = Session(bind=engine)


class UserCRUDService:
    @classmethod
    def exist_user_with_that_login(cls, user_login):
        return session.query(User.login).filter(User.login == user_login).first()

    @classmethod
    def create_user(cls, user):
        if cls.exist_user_with_that_login(user_login=user["login"]):
            return None

        user_db = User(
            login=user["login"],
            user_id=user["id"],
            node_id=user["node_id"],
            avatar_url=user["avatar_url"],
            followers_url=user["followers_url"],
            starred_url=user["starred_url"],
            repos_url=user["repos_url"],
            role=user["type"],
            site_admin=user["site_admin"],
        )
        session.add(user_db)
        session.commit()

    @staticmethod
    def get_last_user_id():
        user_db = session.query(User.user_id).order_by(User.user_id.desc()).first()
        return user_db.user_id if user_db else 0
