import flask
import os

import data.db_session as db_session
from infrastructure.view_modifiers import response
#import services.package_service

app = flask.Flask(__name__)

def main():
  register_blueprints()
  setup_db()
  app.run(debug=True)

def setup_db():
  db_file = os.path.join(
    os.path.dirname(__file__),
    'db',
    'buddha_base.sqlite'
  )

  db_session.global_init(db_file)

def register_blueprints():
  from views import home_views
  from views import quote_views
  app.register_blueprint(home_views.blueprint)
  app.register_blueprint(quote_views.blueprint)


if __name__ == '__main__':
  main()