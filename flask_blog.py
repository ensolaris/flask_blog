from crypt import methods
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '00123344ed0172f2f4c3a4513b6fbecb'

posts = [
    {'author': 'Jane Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'October 12, 2022'
    },
    {'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'October 12, 2022'
    },
    {'author': 'Jimmy Smith',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'October 12, 2022'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template(
        'register.html', 
        title='Register', 
        form=form
        )


@app.route('/login')
def login():
    form = LoginForm()
    return render_template(
        'login.html', 
        title='Log In', 
        form=form
        )