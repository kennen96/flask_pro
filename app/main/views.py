from flask import render_template, redirect, url_for, jsonify, request, make_response, send_from_directory
from .. import db
from ..models import *
from . import main
from .forms import NameForm, TtForm
import json
import time
import os

# @main.route('/', methods=['GET', 'POST'])
# def index():
#     form = TtForm()
#
#     return render_template('index.html', form=form)


@main.route('/tag', methods=['GET', 'POST'])
def tag():
    tags = request.form.get('tag')

    # return jsonify({"data": ["domain", "gender", "age"]})
    return jsonify({"data": ["domain", "gender", "age", tags]})


@main.route('/', methods=['GET', 'POST'])
def index(page = None):
    form = TtForm()
    if page is None:
        page = 1
    page_data = Txt.query.all()#.paginate(page=page, per_page=30)
    return render_template('index.html', page_data=page_data, form=form)


@main.route('/leadout/', methods=['GET', 'POST'])
def lead_out():
    txt = request.form.getlist('fid')
    if request.form.get('firstid'):
        start = request.form.get('firstid')
    else:
        start = 1
    print(start)
    file_path = r'E:\v-junlia\tts_temp_file\lead_out'
    file_name = '{}.txt'.format(time.time())
    full_path = os.path.join(file_path, file_name)
    with open(full_path, 'w') as f:
        f.write('\n'.join(['{}\t{}'.format(str(x[0]).zfill(10), x[1]) for x in list(enumerate(txt, start=10))]))
    return redirect(url_for('main.downloadfile', filename=full_path))


@main.route('/downloadfile/', methods=['GET', 'POST'])
def downloadfile():
    if request.method == 'GET':
        fullfilename = request.args.get('filename')
        fullfilenamelist = fullfilename.split('\\')
        filename = fullfilenamelist[-1]
        # filepath = fullfilename.replace('/%s'%filename, '')
        filepath = r'E:\v-junlia\tts_temp_file\lead_out'
        #普通下载
        response = make_response(send_from_directory(filepath, filename, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(filepath.encode().decode('latin-1'))
        return send_from_directory(filepath, filename, as_attachment=True)
