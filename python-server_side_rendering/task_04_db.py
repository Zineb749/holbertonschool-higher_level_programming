from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)

def jsonfile(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)




@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id', type=int)

    if source == 'json':
        products = jsonfile('products.json')
    elif source == 'csv':
        products = []
        with open('products.csv', 'r') as f:
            csvFile = csv.DictReader(f)
            for lines in csvFile:
                lines['id'] = int(lines['id'])
                lines['price'] = float(lines['price'])
                products.append(lines)
    elif source == 'sql':
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        db = cursor.fetchall()
        products = []
        for d in db:
            product =   {
                          'id' : d[0],
                          'name' : d[1],
                          'category' : d[2],
                          'price' : d[3]
                        }
            products.append(product)
            
        conn.close()

    else:
        return "Wrong source"
    
    if id:
        products = [product for product in products if product.get('id') == id]
        if not products:
            return "Product not found"
    else:
        products = products

    return render_template('product_display.html', products=products)



if __name__ == '__main__':
    app.run(debug=True)


    