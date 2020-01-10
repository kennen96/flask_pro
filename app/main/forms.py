from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from ..models import *
from . import main


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


def selcity(city):
    # conn = MySQLdb.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     passwd='a821200725',
    #     db='webjob',
    #     charset='utf8'
    # )
    # sql="select litcity from Bigcity where city='"+city+"'"
    # cur=conn.cursor()
    # cur.execute(sql)
    # result=cur.fetchone()
    # results=result[0]
    return ['domain', 'gender', 'ageee']


# class TtForm(FlaskForm):
#     # tags = ['domain', 'gender', 'age']
#     tags = Txt.query.all()
#     # tag1 = {'domain': selcity('domain'),
#     #         'gender': ['domain', 'gender', 'age'],
#     #         'age': ['domain', 'gender', 'age']}
#     tag1 = {tag: selcity(tag) for tag in tags}
#     tags = [RadioField(tag, choices=[x for x in enumerate(label)], render_kw={"class": "radio-inline"})
#             for tag, label in tag1.items()]
#
#     for i, s in enumerate(tags):
#         locals()['field' + str(i)] = s
#     del locals()['s']
#     submit = SubmitField('Submit')



