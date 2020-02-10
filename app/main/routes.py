from flask import render_template, request, flash, Blueprint
from app.main.forms import SignupForm

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('index.html')


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Signup requested for {}'.format(form.username.data))
    return render_template('signup.html', form=form)
