#!/usr/bin/python3

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hello_HBNB(id=None):
    """     all_states = storage.all(State)
    states = list(all_states.values())
    result = None

    if id is not None:
        state = "State.{}".format(id)
        if (state in all_states):
            states = [all_states[state]]
            result = all_states[state].name
    """
    return render_template('10-hbnb_filters.html')


@app.teardown_appcontext
def home_teradown(exit):
    storage.close()


if __name__ == '__main__':
    app.run(debug=True)
