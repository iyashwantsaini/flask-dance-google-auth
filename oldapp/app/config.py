class Config(object):
    SECRET_KEY = "supersekrit"
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # GOOGLE_OAUTH_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    GOOGLE_OAUTH_CLIENT_ID = '611115857552-35jvgiq7ugd2dmdpj6kimnpeetn1549c.apps.googleusercontent.com'
    # GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
    GOOGLE_OAUTH_CLIENT_SECRET = 'bG9GaeOr763E6ZBWuFjJhVEZ'