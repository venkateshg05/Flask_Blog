from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'cd4e828b9aecaad2b6cbaf029155ebf5'

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

if __name__ == '__main__':
    app.run(debug=True)