import csv
from flask import Flask,jsonify

with open('final.csv',encoding='UTF-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articals = data[1:]

liked_articals = []
unliked_articals = []

app = Flask(__name__)

@app.route("/like")
def like_artical():
    artical = all_articals[0]
    liked_articals.append(artical)
    return jsonify({
        "status":'success'
    }),201

@app.route("/unlike")
def like_artical():
    artical = all_articals[0]
    unliked_articals.append(artical)
    return jsonify({
        "status":'success'
    }),201

if __name__ == "__main__":
    app.run()