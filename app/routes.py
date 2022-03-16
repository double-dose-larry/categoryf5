from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    return "<h1>Category F5</h2>"