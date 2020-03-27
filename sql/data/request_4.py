import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class RequestDron(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'request_dron'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    number = sqlalchemy.Column(sqlalchemy.Integer)
    date_create = sqlalchemy.Column(sqlalchemy.Date)
    date_close = sqlalchemy.Column(sqlalchemy.Date)
    date_change = sqlalchemy.Column(sqlalchemy.Date, default=datetime.date.today())
    buyer = sqlalchemy.Column(sqlalchemy.String)
    state = sqlalchemy.Column(sqlalchemy.String)


class DronsToReq(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'request_dron_quan'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    num = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("request_dron.number"))
    dron_name = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("cost_dron.name_dron"))
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
