from flask import Flask, render_template, jsonify, request
import json
from data import db_session
from data.place import Place
from sqlalchemy import func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ruslan-key'

@app.route('/')
def index():
    level = request.args.get('level', default=1, type=int)
    return render_template('map.html', active_level=level)

@app.route('/info')
def info():
    db_sess = db_session.create_session()
    level = request.args.get('level', default=1, type=int)
    info = request.args.get('info', default=1, type=str)

    place = db_sess.query(Place).all()
    for i in place:
        if i.title.strip() == info.strip():
            k = i
            break



    return render_template('place.html', active_level=level, info_place=k.description, image=k.image)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')