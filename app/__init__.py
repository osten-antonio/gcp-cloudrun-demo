from flask import Flask
import os
from dotenv import load_dotenv


load_dotenv()


def create_app():

    # templates/ and static/ live at the repository root; compute absolute paths so Flask can find them
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_dir = os.path.join(repo_root, 'templates')
    static_dir = os.path.join(repo_root, 'static')

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    # session secret for flashes and lightweight UI feedback
    app.secret_key = os.environ.get('FLASK_SECRET', 'dev-flask-secret')
    from .routes import bp
    app.register_blueprint(bp)
    return app
