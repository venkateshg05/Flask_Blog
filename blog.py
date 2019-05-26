from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route("/about")
def about():
    return render_template("about.html",title="About")

if __name__ == '__main__':
    app.run(debug=True)