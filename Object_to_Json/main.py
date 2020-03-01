#!env/bin/python
import json
from flask import Flask

app = Flask(__name__)

class Person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):        
        return f'Id:{str(self.id)}, Name: {self.name}, Age: {str(self.age)}'

person = Person(id=1,name='ze',age=30)

person_json = json.dumps(person.__dict__, indent = 4) #serialize the object #parse from object to json
print(person_json)  # return a json in the screen

@app.route('/')
def index():
    return 'Minha primeira pagina'


@app.route('/person') # retorna um json 
def person_return():
    return person_json


app.run(
    host="0.0.0.0",
    port=8080,
    debug=True
)
