from flask import Flask,render_template,url_for,flash,redirect,request
from flaskblog.forms import RegisterationForm, LoginForm
from flaskblog import app, db, bcrypt
from flaskblog.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required
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
            user = User.query.filter_by(email=form.email.data).first()

            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user,remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('home'))
            else:
                flash("Login unsuccessful, please check username and password", 'danger')

    return render_template('login.html', title='login', form=form)

@app.route('/register',methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterationForm()
    if form.validate_on_submit():
        password_hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=password_hashed)
        db.session.add(user)
        db.session.commit()
        flash('Your account has now been created, you can now login ')
        return redirect(url_for('home'))
    return render_template('signupp.html', title='register',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title="Account")
