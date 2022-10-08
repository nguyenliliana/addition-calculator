from flask import Flask  # , request
#from processing import do_calculation
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
