from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['Secret_Key'] = '8aff9f095fa8fdcf48ffacb7cf292e8b'

posts = [
    {
        'author': 'Adam Fine',
        'title': 'Bomber',
        'content': 'first post content',
        'date_posted': 'April 15, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Bomber 2',
        'content': 'second post content',
        'date_posted': 'April 16, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)


if __name__ == "__main__":
    app.run(debug=True)
