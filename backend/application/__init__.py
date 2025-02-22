from flask import Flask
from flask_cors import CORS
import nltk
import ssl

from .extensions import jwt
from .main import main
from .resources.study_compass.study_compass import study_compass
from .resources.e3_selector.e3_selector import e3_selector
from .resources.project_finder.project_finder import project_finder
from .resources.intogen.intogen import intogen
from .resources.student_connector.student_connector import student_connector
from .resources.study_soon.study_soon import study_soon


def create_app(config_object="application.settings"):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config_object)

    jwt.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(study_compass, url_prefix="/studycompass")
    app.register_blueprint(e3_selector, url_prefix="/e3selector")
    app.register_blueprint(project_finder, url_prefix="/projectfinder")
    app.register_blueprint(intogen, url_prefix="/intogen")
    app.register_blueprint(student_connector, url_prefix="/studentconnector")
    app.register_blueprint(study_soon, url_prefix="/studysoon")

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('sentiwordnet')

    return app
