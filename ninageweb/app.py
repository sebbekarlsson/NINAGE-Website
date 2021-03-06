from flask import Flask
from ninageweb.views.index import bp as index_bp
from ninageweb.views.quickstart import bp as quickstart_bp


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(index_bp)
app.register_blueprint(quickstart_bp)
