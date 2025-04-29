from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    level = request.args.get('level', default=1, type=int)
    return render_template('map.html', active_level=level)

@app.route('/info')
def info():
    level = request.args.get('level', default=1, type=int)
    info = request.args.get('info', default=1, type=str)
    return render_template('place.html', active_level=level, info_place=info)


if __name__ == '__main__':
    app.run(debug=True)