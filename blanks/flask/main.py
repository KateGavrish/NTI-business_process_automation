from flask import Flask, render_template, redirect
from data import db_session
from data.details import DetailCategory
from data.drons_cost import DronCost
from data.receipt_of_components import ReceiptOfComponents
from data.count_for_dron import QuanForDron
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



@app.route('/inventarisation', methods=['GET', 'POST'])
def reqister():
    combo_box_options = []
    db_session.global_init('db/drons1.sqlite')
    session = db_session.create_session()
    for user in session.query(DetailCategory):
        combo_box_options.append((user.name_det, 0))
    params = dict()
    params['list_of_sub'] = combo_box_options
    return render_template('table_inv.html', title='Регистрация', params=params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')