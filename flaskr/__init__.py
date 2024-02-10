import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Init Flask application as an instance from the Flask class using factory pattern
def create_app(test_config=None):

    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Development configs
    app.config.from_mapping(
        SECRET_KEY='SECRET KEY!',
        DATABASE_URL=os.environ.get('DATABASE_URL')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Register the blueprints for the app
    #from . import auth
    #app.register_blueprint(auth.bp)


    # A simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # A root page that says hello
    @app.route('/')
    def root():
        return '<h1>Root Page</h1>'

    # Return the created app
    return app