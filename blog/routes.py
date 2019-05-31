from flask import render_template, url_for, flash, redirect, request

from blog import app, db, bcrypt, login_manager
from blog.models import User, Post
from blog.forms import RegisterForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                            form.password.data).decode('utf-8')
        user = User(
                username=form.username.data, email=form.email.data,
                password=hashed_password
                )
        db.session.add(user)
        db.session.commit()
        flash(f'Created account for user {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please enter correct email and password','info')
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html",title="Account")

@app.route("/about")
def about():
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    return render_template("about.html",title="About", image_file=image_file)
