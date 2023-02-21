from flask import Flask
from flask_cors import CORS
from config import config
from migraciones import migracion
from routes import Authors
import os
app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:9300"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Rutas
    app.register_blueprint(Authors.main, url_prefix='/authors')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host='0.0.0.0', port=os.getenv('SERVER_PORT'))
    