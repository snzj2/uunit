from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    level = request.args.get('level', default=1, type=int)
    return render_template('map.html', active_level=level)


if __name__ == '__main__':
    app.run(debug=True)