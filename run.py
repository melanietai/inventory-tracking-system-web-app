from myapp.models import connect_to_db
from myapp import app


if __name__=="__main__":

  connect_to_db(app)
  app.run(debug=True, host="0.0.0.0")