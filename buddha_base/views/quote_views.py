import flask

from infrastructure.view_modifiers import response
#import services.package_service

blueprint = flask.Blueprint('quote',__name__, template_folder='templates')


@blueprint.route('/quotes/<quote_id>')
#@response(template_file='/home/about.html')
def quote_detailed(quote_id):
  return "The Quotes ID is {}".format(quote_id)


#TODO: Use the rank method for the url and return the most saved quote.
@blueprint.route('/quotes/<quote_id>')
#@response(template_file='/home/about.html')
def quote_detailed(quote_id):
  return "The Quotes ID is {}".format(quote_id)

