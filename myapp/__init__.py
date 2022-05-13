from flask import Flask
import jinja2
from myapp.views import inventory as inventory_views

app = Flask(__name__)

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

app.add_url_rule('/', view_func=inventory_views.index)
app.add_url_rule('/create', view_func=inventory_views.create_inventory)
app.add_url_rule('/edit', view_func=inventory_views.edit_inventory)
