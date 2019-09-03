#!/usr/bin/python3

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def hello_HBNB():
    all_states = storage.all(State)
    for state_id, state in all_states.items():
        print(state_id)
        print(state)
    return 'Hello HBNB!'

@app.teardown_appcontext
def teardown_db():
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
