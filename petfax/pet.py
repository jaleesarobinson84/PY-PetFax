from flask import (Blueprint, render_template) 
import json

pets = json.loads(open('pets.json').read())
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

# routes
@bp.route('/')
def index(): 
    return render_template('show.html', pets=pets)

@bp.route('/<int:pet_id>')
def show(pet_id: int):
    if pet_id <= 0 or pet_id > len(pets):
        return "Invalid pet ID", 404  # Return 404 if pet ID is invalid
    pet = pets[pet_id - 1]
    return render_template('pets/show.html', pet=pet)