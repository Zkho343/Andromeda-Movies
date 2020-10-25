from flask import Blueprint, render_template, session

from movie.util.constants import HOME_BP

home_blueprint = Blueprint(HOME_BP, __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home.html',
        title='ANDROMEDA GALAXY MOVIES',
        username=session.get('username', "User")
    )
