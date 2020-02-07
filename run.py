from flask import render_template, request, flash, Flask
from app.main.forms import SignupForm

app = Flask(__name__)
app.secret_key = 'kkY51-_QyYzxnj9k9z0yzw'
app.template_folder = 'app/templates'
app.static_folder = 'app/static'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Signup requested for {}'.format(form.username.data))
    return render_template('signup.html', form=form)
