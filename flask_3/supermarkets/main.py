import uuid
from os import getcwd

from flask import Blueprint, render_template, flash, redirect, request, session

from supermarkets.forms import AddSupermarketForm

supermarket = Blueprint('supermarkets', __name__, template_folder='templates', static_folder='static',
                        static_url_path='/supermarkets/static')

supermarkets_list = []


@supermarket.route('/supermarkets/<item_id>')
def get_page_supermarket(item_id):
    for item in supermarkets_list:
        if item['id'] == item_id:
            session[item_id] = 'clicked'
            return render_template('supermarket.html', item=item)
    return redirect('/supermarkets')


@supermarket.route('/supermarkets')
def get_page_all_supermarkets():
    supermarkets_filter = []
    if request.args:
        for key, value in request.args.items():
            if value:
                supermarkets_filter = [item for item in supermarkets_list if item[key] == value]
    else:
        supermarkets_filter = supermarkets_list
    return render_template('supermarkets.html', supermarkets_list=supermarkets_filter)


@supermarket.route('/add_supermarket', methods=['GET', 'POST'])
def get_page_add_supermarket():
    form = AddSupermarketForm()
    if form.validate_on_submit():
        data = {
            'id': str(uuid.uuid1()),
            'name': form.supermarket_name.data,
            'location': form.supermarket_location.data,
            'img_name': upload_image()
        }
        supermarkets_list.append(data)
        flash('Supermarket added!', 'success')
        return redirect('/supermarkets')
    return render_template('add_supermarket.html', form=form)


def upload_image():
    if request.files['supermarket_image']:
        image = request.files['supermarket_image']
        image.save(f'{getcwd()}/supermarkets/static/{image.filename}')
        return image.filename
    return 'no-photo.png'
