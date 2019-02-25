from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import folium
# from .. import file

# TODO: load data from DB
# TODO: validate new posted data
# TODO: use cookies to verify if the user already submitted location

bp = Blueprint('map', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    m = folium.Map(location=[20, 0], zoom_start=3)
    map_html = m._repr_html_()
    # print(map_html)
    text1 = 'fdalfkdjfla'
    if request.method == 'POST':
        # TODO: add new point to map and generate new map1.html inside templates folder
        location = request.form['location']
        print('new location: ', location)
    return render_template('base.html', map_=map_html)  # map_html  # 'base.html', map_=map_html)


@bp.route('/map')
def map1():
    m = folium.Map(location=[20, 0], zoom_start=3)
    return m._repr_html_()

