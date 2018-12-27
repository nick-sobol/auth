from sqlalchemy import Column, Integer, String

from exceptions import BadRequest
from database import Base, session_factory


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(32), nullable=False)

    def to_dict(self):
        return dict(user_id=self.id)

    @staticmethod
    def get_user(data, session=None):
        if not session:
            session = session_factory()

        db_user = (
            session.query(User).filter(
                User.username == data['username']
            ).first()
        )

        return db_user