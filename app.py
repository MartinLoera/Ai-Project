from flask import Flask, request, jsonify
import json
import sqlite3
import torch
import argparse
import io
from PIL import Image

app = Flask(__name__)
model = torch.hub.load('./yolov5', 'custom', path='./weigths/best.pt', source='local')
fake_ai_response = ["a", "b"]

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    return jsonify({'error': 'data not found'})

@app.route('/', methods=['POST'])
def response_img():

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        results = model(img)
        #results = results.pandas().xyxy[0].to_json(orient="records")     
        results = results.pandas().xyxy[0]
        results = results.to_dict()
        results = list(results['name'].values())
        
        con = sqlite3.connect("./databases/recipes.db")
        query = "SELECT * FROM recipe WHERE ingredients LIKE "
        query_two = " LIMIT 10"
        f_query = ""
        lenght = len(results)
        for index in range(lenght):
            
            if index == 0:
                q = f"'%{results[index]}%' "    
                f_query = query + q
            else:
                q = f"OR ingredients LIKE '%{results[index]}%' "
                f_query += q 

        f_query += query_two
        resp = con.execute(f_query).fetchall()
        con.close()
        return jsonify(resp)
        
    return "Need a img"


app.run(debug=True)