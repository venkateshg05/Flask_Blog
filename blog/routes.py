from flask import render_template, url_for, flash, redirect

from blog import app
from blog.models import User, Post
from blog.forms import RegisterForm, LoginForm

posts = [
    {
        'title' : 'Post 1',
        'author' : 'Author 1',
        'date_posted' : 'Apr 20, 2018',
        'content' : 'post 1 content'
    },
    {
        'title' : 'Post 2',
        'author' : 'Author 2',
        'date_posted' : 'Jan 20, 2018',
        'content' : 'post 2 content'
    }
]

@app.route("/")
@app.route("/home")
def home():
    """
        function name arbitrary
        uses the above decorator to call this function
        render_template has 1st arg as filename under templates folder
        other **args are unpacked using the same param name used here
        they'll be referenced in the template passed
    """
    return render_template("home.html", posts=posts)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Created account for user {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template("login.html", title="Login", form=form)

@app.route("/about")
def about():
    return render_template("about.html",title="About")
