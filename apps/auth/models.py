from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(32), nullable=False)

    def to_dict(self):
        return dict(user_id=self.id)