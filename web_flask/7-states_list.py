#!/usr/bin/python3

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def hello_HBNB():
    dicty = {}
    all_states = storage.all(State)
    for state_id, state in all_states.items():
        list2 = state_id.split(".")[1]
        list1 = state.name
        dicty.update({list1: list2})

    list1 = []
    list2 = []
    for key in sorted(dicty):
        list1.append(key)
        list2.append(dicty[key])
    return render_template('7-states_list.html', dicty=zip(list1, list2))


@app.teardown_appcontext
def home_teradown(exit):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
