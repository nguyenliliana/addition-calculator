from flask import Flask
from processing import do_calculation

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=["GET", "POST"])
def adder_page():
    return '''
     <html>
      <body>
       <p> Enter your numbers: </p>
       <form method="post" action".">
        <p><input name="number1" /></p>
        <p><input name="number2" /></p>
        <p><input type="submit" value="Do calculation" /></p>
       </form>
      </body>
     </html>
    '''


if __name__ == '__main__':
    app.run(debug=True, port=8000)
