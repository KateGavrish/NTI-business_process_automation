import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class QuanForDron(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'quantity_for_dron'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_dron = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("cost_dron.name_dron"))
    name_det = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("detail_category.name_det"))
    quantity = sqlalchemy.Column(sqlalchemy.Integer)