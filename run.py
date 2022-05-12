"""Application Flask server"""
from flask import Flask
from app.models import connect_to_db
import jinja2

app = Flask(__name__)

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


if __name__=="__main__":

  connect_to_db(app)
  app.run(debug=True, host="0.0.0.0")