from flask import Flask, request
app = Flask(__name__)
from config import password
import mysql.connector
import json
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=password,
  database="pin2pre"
)
mycursor = mydb.cursor()

@app.route('/')
def hello_world():
    cache = file
    if cache:
        return
    else:
        io = fileasdasd
        
    return 'Hello, World!'

@app.route('/products')
def getAllProducts():
    resultList = []
    result = {}
    mycursor.execute("SELECT name, quantity FROM product")
    myresult = mycursor.fetchall()
    for x in myresult:
        result['name'] = x[0]
        result['quantity'] = x[1]
        resultList.append(result)
    return json.dumps({'products': resultList})

@app.route('/products/<productId>', methods=['GET', 'POST'])
def product(productId):
    if request.method == 'GET':
        cache
            return
        else 
            mycursor.execute("SELECT name, quantity FROM product where id='" + productId + "'")
            myresult = mycursor.fetchone()
        result = {
            "name": myresult[0],
            "quantity": myresult[1]
        }
        return json.dumps({'result': result})
    else:
        mycursor.execute("SELECT quantity FROM product where id='" + productId + "'")
        myresult = mycursor.fetchone()
        productQuantity = myresult[0]
        body = request.get_json()
        user = body['name']
        orderQuantity = body['quantity']
        newQuantity = productQuantity - orderQuantity 
        mycursor.execute("UPDATE product set quantity='" + str(newQuantity) + "' where id=" + str(productId))
        mycursor.execute("INSERT into transaction (user, productId, quantity) values ('"  + user + "', "+ str(productId) +", " + str(orderQuantity) +")")
        mydb.commit()
        # print(body)
        return 'completed'
