import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class ReceiptOfComponents(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'receipt_of_components'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_det = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("detail_category.name_det"))
    serial_number = sqlalchemy.Column(sqlalchemy.String)
    quantity = sqlalchemy.Column(sqlalchemy.Integer)
    person = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.Date)



db_session.global_init('sql/db/drons1.sqlite')
session = create_session()
for user in session.query(User).filter(User.address == 'module_1'):
    print(user)