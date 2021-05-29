from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template
from flask import abort, redirect

app = Flask(__name__)



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/')
def index():
    return 'Index Page'


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return redirect(url_for('hello'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('hello.html'), 404


@app.route('/error/<int:number>')
def error(number):
    abort(number)
"""@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()"""


@app.route("/me")
def me_api():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return {
        "username": "yale li",
        "theme": "dark"

    }


with app.test_request_context('/hello?username=yale&password=abc', method='POST'):
    print(request.args.get('username', 'Null'))
