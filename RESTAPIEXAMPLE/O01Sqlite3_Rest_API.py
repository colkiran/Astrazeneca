import sqlite3
from flask import Flask, jsonify, request
import threading
from flask_restful import Resource

app = Flask(__name__)

conn = sqlite3.connect("productsdb.sqlite3", check_same_thread=False)
lock = threading.Lock()

cursor = conn.cursor()
@app.route("/products/<prodid>", methods=['GET'])
def get_by_id(prodid):
    res = {}
    query = f"select * from products where prodid = {prodid}"
    cursor.execute(query)
    for rec in cursor.fetchall():
        res[rec[0]] = rec
    return res

@app.route("/products", methods=['GET'])
def get_products():
    res = []
    query = "select * from products"
    cursor.execute(query)
    for rec in cursor.fetchall():
        res.append({'prodid':rec[0], 'prodname':rec[1], 'qty': rec[2], 'prodtype':rec[3]})
    return jsonify(res)

@app.route("/products", methods=['POST'])
def create_prod():
    data = request.json
    query = f"insert into products values ('{data.get('prodid')}', '{data.get('prodname')}', {data.get('qty')}, '{data.get('prodtype')}')"
    cursor.execute(query)
    conn.commit()
    return {'message': 'product created successfully', 'pid': data.get('prodid')}, 201

@app.route("/products/<prodid>", methods=['PUT'])
def update_prod(prodid):
    data = request.json
    query = (f"update products set prodname = '{data.get('prodname')}', qty = '{data.get('qty')}', prodtype = '{data.get('prodtype')}' where prodid = '{data.get('prodid')}'")
    cursor.execute(query)
    conn.commit()
    return {'message': 'prod update successfully', 'pid': data.get('prodid')}, 200

@app.route('/products/<prodid>', methods=['DELETE'])
def delete_prod(prodid):
        query = f"delete from products where prodid = '{prodid}'"
        print('-' * 60)
        print(query)
        print('-' * 60)
        cursor.execute(query)
        conn.commit()
        return {'message': 'prod deleted successfully', 'pid': prodid}, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
