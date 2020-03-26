import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Balance(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'balance'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_det = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("detail_category.name_det"))
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    date = sqlalchemy.Column(sqlalchemy.Date)
