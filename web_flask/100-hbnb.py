#!/usr/bin/python3

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hello_HBNB():
    all_states = storage.all(State)
    states = list(all_states.values())

    all_amenities = storage.all(Amenity)
    amenities = list(all_amenities.values())

    all_places = storage.all(Place)
    places = list(all_places.values())

    all_users = storage.all(User)
    users = list(all_users.values())
   

    return render_template('100-hbnb.html',
                           states=states, amenities=amenities,
                           places=places, users=users)


@app.teardown_appcontext
def home_teradown(exit):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
