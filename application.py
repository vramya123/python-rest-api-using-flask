from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} : {self.description}'

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def getdrinks():
    output = []
    drinks = Drink.query.all()
    for d in drinks:
        drink = {'name' : d.name,
                 'description' : d.description}
        output.append(drink)
    return {"drinks":output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {'name':drink.name, 'description':drink.description}

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return { 'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {'error':'Drink does not exist'}
    db.session.delete(drink)
    db.session.commit()
    return {'message':'Item deleted successfully'}