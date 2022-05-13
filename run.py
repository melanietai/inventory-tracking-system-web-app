from app.models import connect_to_db
from app import app


if __name__=="__main__":

  connect_to_db(app)
  app.run(debug=True, host="0.0.0.0")