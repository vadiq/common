import uuid
from os import getcwd

from flask import Blueprint, render_template, flash, redirect, request, session

from flask_3.products.forms import AddProductForm

product = Blueprint('products', __name__, template_folder='templates', static_folder='static',
                    static_url_path='/products/static')

products_list = []


@product.route('/products/<item_id>')
def get_page_product(item_id):
    for item in products_list:
        if item['id'] == item_id:
            session[item_id] = 'clicked'
            return render_template('product.html', item=item)
    return redirect('/products')


@product.route('/products')
def get_page_all_products():
    if request.args:
        products_filter = []
        for item in products_list:
            for key, value in request.args.items():
                if item[key] == value:
                    products_filter.append(item)
    else:
        products_filter = products_list
    return render_template('products.html', products_list=products_filter)


@product.route('/add_product', methods=['GET', 'POST'])
def get_page_add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        data = {
            'id': str(uuid.uuid1()),
            'name': form.product_name.data,
            'description': form.product_description.data,
            'img_name': upload_image(),
            'price': str(form.product_price.data)
        }
        products_list.append(data)
        flash('Product added!', 'success')
        return redirect('/products')
    return render_template('add_product.html', form=form)


def upload_image():
    if request.files['product_image']:
        image = request.files['product_image']
        image.save(f'{getcwd()}/products/static/{image.filename}')
        return image.filename
    return 'no-photo.png'
