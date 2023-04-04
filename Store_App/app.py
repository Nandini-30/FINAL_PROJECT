import os
from flask import Flask
from flask import render_template,redirect,request,url_for,jsonify,json
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
import sqlite3

app = Flask(__name__)

# databaseConn
project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir,"Inventory.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.app_context().push()


class Inventory(db.Model):
    __tablename__="MyStore" #table name
    itemname=db.Column(db.Text(), unique=True, nullable=False, primary_key=True)
    quantorderd=db.Column(db.Integer(), unique=True, nullable=False)
    quantremain=db.Column(db.Integer(), unique=True, nullable=False)
    vendorname=db.Column(db.Text(), unique=True, nullable=False)
    purchase_price=db.Column(db.Integer(), unique=True, nullable=False)
    selling_price=db.Column(db.Integer(), unique=True, nullable=False)
    dateAdded=db.Column(db.Text(),default=datetime.now())
    dateUpdated=db.Column(db.Text(),default=datetime.now())

    def __init__(self,itemname,quantorderd,quantremain,vendorname,purchase_price,selling_price,dateAdded,dateUpdated):
        self.itemname = itemname
        self.quantorderd = quantorderd
        self.quantremain = quantremain
        self.vendorname = vendorname
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.dateAdded = dateAdded
        self.dateUpdated = dateUpdated

        def __repr__(self):
            return f"{self.itemname},{self.quantorderd},{self.quantremain},{self.vendorname},{self.purchase_price},{self.selling_price},{self.dateAdded},{self.dateUpdated}"


class User(db.Model):
    uid = db.Column(db.Integer(), unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def __repr__(self):
           return f"{self.username},{self.email},{self.password}"

# Register

@app.route('/register' , methods = ['POST'])
def register():
    if request.method=='POST':

        if not request.form["email"] or not request.form["username"] or not request.form["password"]:
            print("Please enter correct details")
            return redirect("/register")

        else:
            print(request.form["username"])
            print(request.form["email"])
            print(request.form["password"])
            user = User(request.form["username"],request.form["email"],request.form["password"])
            db.session.add(user)
            db.session.commit()
            return redirect("/")

    return render_template("login/register.html")


# Login
check_email=""
@app.route('/login' , methods=['GET', 'POST'])
def login():
    print("check")
    global check_email
    if request.method=='POST':
        print(request.form["email"])
        print(request.form["psw"])
        if not request.form["email"] or not request.form["psw"]:
            print("Please enter correct details")
        

        else:

            email = request.form["email"]
            user = user.query.filter_by(email=email).first()
            print(user.email)
            print(user.password)
            if(user.password==request.form["psw"]):
                print("Login Successfull")
                check_email = user.email
                return redirect("/")
            
    
    return render_template("register/login.html")

 
@app.route('/table')
def get_all_data():
    all_data = Inventory.query.all() # fetch all data from database
    result = [] # create an empty list to store results
    for data in all_data:
        # create a dictionary to store each data object
        data_dict = {
            'itemname': data.itemname,
            'quantorderd': data.quantorderd,
            'quantremain': data.quantremain,
            'vendorname': data.vendorname,
            'purchase_price': data.purchase_price,
            'selling_price' : data.selling_price,
            'dateAdded' : data.dateAdded,
            'dateUpdated' : data.dateUpdated

        }
        result.append(data_dict) # append the dictionary to the result list
    return jsonify(result)
    

    
#connect to the database
def addInventoryIntoTable(itemname,quantorderd,quantremain,vendorname,purchase_price,selling_price,dateAdded,dateUpdated):
    try:
        sqliteConnection = sqlite3.connect('Inventory.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_query="""INSERT INTO inventory
                (itemname,quantorderd,quantremain,vendorname,purchase_price,
                selling_price,dateAdded,dateUpdated) 
                VALUES (?,?,?,?,?,?,?,?)"""
        data_tuple = (itemname,quantorderd,quantremain,vendorname,purchase_price,selling_price,dateAdded,dateUpdated)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_MyStore table")

        cursor.close()
        return "Success"
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
        return error
    
@app.route('/add',methods=['POST'])
def addInventory(): 
    if request.method == 'POST':              
        itemname = request.form['itemname']
        quantorderd = request.form['quantorderd']
        quantremain = request.form['quantremain']
        vendorname = request.form['vendorname']
        purchase_price = request.form['purchase_price']
        selling_price = request.form['selling_price']
        dateAdded = request.form['dateAdded']
        dateUpdated = request.form['dateUpdated']
        item = Inventory(itemname,quantorderd,quantremain,vendorname,purchase_price,selling_price,dateAdded,dateUpdated)
                
        db.session.add(item)
        db.session.commit()
        return ({"message":"Item has been Added successfully"})



@app.route('/update',methods=['PUT'])
def updateInventory():
    if request.method == 'PUT':
        try:
            Inventory.query.filter(Inventory.itemname == request.form['itemname'])
            itemname = request.form['itemname']
            item = Inventory.query.filter_by(itemname=itemname).first()
            item.quantorderd = request.form['quantorderd']
            item.quantremain = request.form['quantremain']
            item.vendorname = request.form['vendorname']
            item.purchase_price = request.form['purchase_price']
            item.selling_price = request.form['selling_price']
            db.session.commit()
            return jsonify({"message":"Item has been Updated Successfully"})
        except:
            return jsonify({"message":"not found"})


@app.route('/delete',methods=['DELETE'])
def deleteInventory():
    if request.method == 'DELETE':
        itemname = request.form['itemname']
        item = Inventory.query.filter_by(itemname=itemname).first()
        db.session.delete(item)
        return jsonify({"message":"Item has been Deleted Successfully"})

# @app.route('/clear_database')
# def clear_database():
#     db.session.query(User).delete()
#     db.session.commit()
#     return 'User table has been cleared!'


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)