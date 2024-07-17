from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class News(Base):
    __tablename__ = "news"

    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String(64), nullable=False)
    description = Column(String(255), nullable=False)
    source = Column(String(64), nullable=False)
    url = Column(String(64), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    my_news = relationship("MyNews", back_populates="news")
