#!/usr/bin/python3

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def hello_HBNB():
    all_states = storage.all(State)
    states = list(all_states.values())

    all_amenities = storage.all(Amenity)
    amenities = list(all_amenities.values())

    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def home_teradown(exit):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
