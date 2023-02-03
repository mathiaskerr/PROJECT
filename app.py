from flask import Flask, render_template
from controllers.transactions_controller import transactions_blueprint

#from yor controller import the blue prints for each class


app = Flask(__name__)

# app.register_blueprint(****_blueprint) for each class 

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)    