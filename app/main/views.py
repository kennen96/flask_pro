from flask import render_template, session, redirect, url_for, current_app, jsonify
from .. import db
from ..models import User
from . import main
from .forms import NameForm, TtForm


@main.route('/', methods=['GET', 'POST'])
def index():
    # form = NameForm()
    form = TtForm()

    return render_template('index.html', form=form)


@main.route('/tag', methods=['GET', 'POST'])
def tag():
    return jsonify({"data": ["domain", "gender", "age"]})