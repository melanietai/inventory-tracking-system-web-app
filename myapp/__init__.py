from flask import Flask
import jinja2
from myapp.views import inventory as inventory_views, warehouse as warehouse_views, index as index_views

app = Flask(__name__)

app.secret_key = "dev"

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

app.add_url_rule('/', view_func=index_views.index)

app.add_url_rule('/inventory/new', view_func=inventory_views.show_new_inventory_page)
app.add_url_rule('/inventory/new', view_func=inventory_views.new_inventory, methods=['POST'])
app.add_url_rule('/inventory/<id>', view_func=inventory_views.show_edit_inventory_page)
app.add_url_rule('/inventory/<id>', view_func=inventory_views.edit_inventory, methods=['POST'])
app.add_url_rule('/inventory/<id>/delete', view_func=inventory_views.delete_inventory, methods=['POST'])

app.add_url_rule('/warehouse/new', view_func=warehouse_views.show_new_warehouse_page)
app.add_url_rule('/warehouse/new', view_func=warehouse_views.new_warehouse, methods=['POST'])
app.add_url_rule('/warehouse/<id>', view_func=warehouse_views.show_edit_warehouse_page)
app.add_url_rule('/warehouse/<id>', view_func=warehouse_views.edit_warehouse, methods=['POST'])
app.add_url_rule('/warehouse/<id>/delete', view_func=warehouse_views.delete_warehouse, methods=['POST'])


