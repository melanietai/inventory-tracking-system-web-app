from flask import Flask
from myapp.views import inventory as inventory_views, warehouse as warehouse_views, index as index_views

app = Flask(__name__)

app.secret_key = "dev"

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


