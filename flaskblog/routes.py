from flask import Flask,render_template,url_for,flash,redirect
from flaskblog.forms import RegisterationForm, LoginForm
from flaskblog import app
from flaskblog.models import User,Post

posts = [
    {
        "author": "Coreh Shcaeer",
        "title" : "Blog post 1",
        "content" : "Contents",
        "date posted": "April 20, 2019"
    },
       {
        "author": "Jane Shcaeer",
        "title" : "Blog post 2",
        "content" : "Contents",
        "date_posted": "April 20, 2018"
    }
]
@app.route('/')
#@app.route('/home')
def home():
    return render_template('home.html',posts=posts, title='home')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful, please check username and password", 'danger')

    return render_template('login.html', title='login', form=form)

@app.route('/register',methods=['GET','POST'])
def signup():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash('Account created for ' + form.username.data,'success')
        return redirect(url_for('home'))
    return render_template('signupp.html', title='register',form=form)

