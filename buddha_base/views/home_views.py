import flask

from infrastructure.view_modifiers import response
import services.package_service

blueprint = flask.Blueprint('home',__name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
  quotes = services.package_service.get_latest_packages()
  return {'quotes':quotes}

@blueprint.route('/home/about')
@response(template_file='/home/about.html')
def about():
  return {}