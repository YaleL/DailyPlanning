import os

from flask import Flask


def create_app(test_config=None):
    # create/configure the app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        #load instance config when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load the test config
        app.config.from_mapping(test_config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #A simple page
    @app.route('/hello/')
    def hello():
        return 'Hello World!'

    @app.route('/index/')
    def index():
        return 'This is the index.'

    from . import db
    app.logger.debug(' ready to initialize database ')
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
