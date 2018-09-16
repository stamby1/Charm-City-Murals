import os
from flask import Flask, request, render_template, jsonify
app = Flask(__name__, static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024

@app.route("/discover")
def canvas():
    return render_template("canvas.html")

@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/")
def index():
    return render_template("index.html")

# Out API
@app.route("/api", methods=["POST"])
def api():
    # data = request.form['data']
    meta = {"name": "The awesome mural", "artist": "Hop Hacks Dream Team", "date": "09/15/2018", "bounding_box":[(100, 100),(300, 30),(250, 220),(90, 250)]}
    return jsonify(meta)

#if (__name__ == '__main__'):
# Bind to PORT if defined, otherwise default to 80.
#    port = int(os.environ.get('PORT', 8000))
#    app.run(host='0.0.0.0', port=port)
