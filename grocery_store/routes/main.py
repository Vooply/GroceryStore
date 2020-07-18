from collections import namedtuple

from flask import Blueprint, render_template
from flask_login import current_user, login_required
from grocery_store.models import Good

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
                           user=current_user.name,
                           email=current_user.email)


@main.route('/myorders')
@login_required
def orders():
    data = namedtuple('Orders', ['store', 'date', 'price', 'goods'])
    order_list = [data(order.store.name,
                       order.created_time,
                       sum([good.good.price for good in order.order_lines]),
                       {good.good.name: good.good.price for good in order.order_lines}) for order in
                  current_user.orders]
    totalsum = sum(order.price for order in order_list)
    return render_template("orders.html", orders=order_list, totalsum=totalsum)


@main.route('/prices')
def goods_prices():
    return render_template('goods_list.html', goods=Good.query.all())


@main.route("/manage_stores")
@login_required
def stores():
    return render_template("stores.html", stores=current_user.manage_stores)
