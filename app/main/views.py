from flask import render_template, redirect, url_for, jsonify, request, make_response, send_from_directory, flash
from ..models import *
from . import main
from .forms import NameForm
import time
import os


def sel_label(tag):
    labels = Label.query.filter_by(tag_id=Tag.query.filter_by(content=tag).first().id)
    # tag_list = [tag]
    # print(Tag.query.filter(Tag.content.in_(tag_list)))
    # labels = Label.query.filter_by(tag_id=Tag.query.filter(Tag.content.in_(tag_list)).first().id)
    return labels


# @main.route('/tag', methods=['GET', 'POST'])
# def tag():
#     tags = request.form.get('tag')
#     return jsonify({"data": ["domain", "gender", "age", tags]})


@main.route('/', methods=['GET', 'POST'])
def index(page=None):
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    tags = Tag.query.all()
    tag_data = {tag.content: sel_label(tag.content) for tag in tags}
    if request.form:
        list1 = [request.form.getlist(tag.content) for tag in tags if request.form.getlist(tag.content) != []]
        print(list1)
        txt_id_list = []
        for labels in list1:
            labels_id = [Label.query.filter_by(content=label).first().id for label in labels]
            # print(labels_id)
            # print([relation.txt_id for relation in TxtLabel.query.filter(TxtLabel.label_id.in_(labels_id)).all()])
            txt_id_list = ([relation.txt_id for relation in TxtLabel.query.filter(TxtLabel.label_id.in_(labels_id)).all()]
            if txt_id_list ==[] else list(set(txt_id_list) & set([relation.txt_id for relation in TxtLabel.query.filter(TxtLabel.label_id.in_(labels_id)).all()])))
        print(txt_id_list)
        paginate = Txt.query.filter(Txt.id.in_(txt_id_list)).paginate(page=page, per_page=per_page)
        page_data = paginate.items
        return render_template('index.html', page_data=page_data, paginate=paginate, tags=tag_data)
    paginate = Txt.query.paginate(page=page, per_page=per_page)
    page_data = paginate.items
    return render_template('index.html', page_data=page_data, paginate=paginate, tags=tag_data)


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


@main.route('/addtag/', methods=['POST'])
def add_tag():
    tag_name = request.form.get('add_tag')
    new_tag = Tag(content=tag_name)
    db.session.add(new_tag)
    flash('添加成功')
    return redirect(url_for('main.index'))


@main.route('/addlabel/', methods=['POST'])
def add_label():
    label_name = request.form.get('add_label')
    new_tag = Tag(content=label_name)
    db.session.add(new_tag)
    flash('添加成功')
    return redirect(url_for('main.index'))

