from flask import Flask, render_template

from flask_3.products.main import product
from flask_3.supermarkets.main import supermarket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret password'

app.register_blueprint(product)
app.register_blueprint(supermarket)


@app.route('/')
def get_page_home():
    return render_template('home.html')


@app.errorhandler(404)
def get_page_404(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
