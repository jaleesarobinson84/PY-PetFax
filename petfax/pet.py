from flask import (Blueprint, render_template) 
import json

pets = json.loads(open('pets.json').read())
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

# routes
@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<pet_id>')
def show(id):
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)
