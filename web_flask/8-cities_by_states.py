#!/usr/bin/python3

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def hello_HBNB():
    all_states = storage.all(State)
    states = list(all_states.values())
#    states = sorted(states, key=lambda x: x.name)

    return render_template('8-cities_by_states.html', dicty=states)


@app.teardown_appcontext
def home_teradown(exit):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
