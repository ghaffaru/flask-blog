from flask import Flask,render_template,url_for,flash,redirect
from forms import RegisterationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '112497dcc2ea30daa2f1c8268917dc6c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    image_file = db.Column(db.String(20), nullable=False,default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User " + self.username + " email: " + self.email + " image: " + self.image_file


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
 
    def __repr__(self):
        return "Post " + self.title + " date posted: " + str(self.date_posted)



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



if __name__ == '__main__':
    app.run(debug=True)
