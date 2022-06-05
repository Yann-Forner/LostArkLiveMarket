import json
from flask import Flask, render_template
from Model import Market as M

app = Flask(__name__)


region = "Europe Central"
cat = json.load(open("Model/categories.json"))
#req = M.getByCat(region, "Enhancement Material", "Honing Materials")

#print(json.dumps(req, indent=4, sort_keys=True))

@app.route('/')
def index():
    return render_template("index.html", cat=cat)


@app.route('/send/<cat>')
def getData(cat):
    return json.dumps(M.getByCat(region, cat))

@app.route('/sendId/<id>')
def getDataId(id):
    return json.dumps(M.getById(region, id))

@app.route('/history/<id>')
def getHistoryId(id):
    return json.dumps([M.getById(region,id),M.getMarketHistoryById(region,id)])


app.run(host='0.0.0.0', port=81)