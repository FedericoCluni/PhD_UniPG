from flask import Flask, render_template, request

from urllib.parse import quote

from model import InputForm
from compute import compute

app = Flask(__name__)

default = True

@app.route('/retta', methods=['GET', 'POST'])
def index():
    global default
    form = InputForm(request.form)
    if default or (request.method == 'POST' and form.validate()):
        for field in form:
            # Make local variable (name field.name)
            exec('global %s; %s = %s' % (field.name, field.name, field.data))
        figure, I = compute(m, b, x1, x2)
        I=round(I,3)
        figure=quote(figure)
    else:
        I = None
        figure = None
    default = False
    return render_template('view.html', form=form, figure=figure, I=I)


if __name__ == '__main__':
    app.run(debug=True) # https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode
