from flask import Flask, render_template

app = Flask(__name__)

fruits_list = [
    'melon',
    'apple',
    'strawberry',
    'grape'
]

vegetables_list = [
    'beans',
    'carrot',
    'beetroot',
    'cucumber'
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/vegetables')
def vegetables():
    return render_template('vegetables.html',
                           title='Vegetables',
                           vegetables_list=vegetables_list
                           )


@app.route('/fruits')
def fruits():
    return render_template('fruits.html',
                           title='Fruits',
                           fruits_list=fruits_list
                           )


if __name__ == "__main__":
    app.run(debug=1)
