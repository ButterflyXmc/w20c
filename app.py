from flask import Flask,request
import json
from dbhelpers import run_statement

app = Flask(__name__)

@app.get('/api/get_animals')
def get_animals():
    # SELECT names FROM animals;
    result = run_statement("CALL get_animals()")
    if(type(result) == list):
        return json.dumps(result, default=str)
    else:
        return "Something went wrong"
    
@app.post('/api/add_animal')
def post_animal():
    # this is what my api expects as a params
    name_input = request.json.get('animalName')
    if name_input == None:
        return "You must enter animalName!"
	# INSERT INTO animals (names) VALUES (names_input)
    result = run_statement("CALL add_animal(?)", [name_input])
    if result == None:
        return "Animal added Successfully"
    else:
        return "Something went wrong!"

@app.patch('/api/update_animal')
def patch_animal():
    name_input = request.json.get('animalName')
    id_input = request.json.get('animalId')
    if name_input == None:
        return "You must enter the animal name you want to update!"
    if id_input == None:
        return "You must enter the animal ID you want to update!"
        # UPDATE animals SET names = names_input WHERE id = id_input; 
    result = run_statement("CALL patch_animal(?,?)", [name_input, id_input])
    if result == None:
        return "Animal updated Successfully"
    else:
        return "Something went wrong!"
    
@app.delete('/api/delete_animal')
def delete_animal():
    id_input = request.json.get('animalId')
    if id_input == None:
        return "You must enter a valid animal ID and its name!"
    # DELETE FROM animals WHERE id = id_input;
    result = run_statement("CALL delete_animal(?)", [id_input])
    if result == None:
        return "Animal deleted Successfully"
    else:
        return "Something went wrong!"

app.run(debug = True)