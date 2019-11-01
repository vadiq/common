from flask import Flask, render_template
# імпортую urlize для того, щоб адекватні урли формувались, але так і не зрозумів, куди втулити :(
# from jinja2.utils import urlize
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/<item>')
def get_item_page(item):
    for element in get_data():
        if element.get('title') == item:
            description = element.get('text')
            return render_template("layout-items.html", item=item, data=description)


@app.route('/author')
def get_page_author():
    return render_template("author.html", title='Author')


if __name__ == "__main__":
    app.run(debug=True)
