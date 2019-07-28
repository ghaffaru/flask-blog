from flask import Flask,render_template,url_for
app = Flask(__name__)


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
@app.route('/home')
def home_page():
    return render_template('home.html',posts=posts, title='home')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
