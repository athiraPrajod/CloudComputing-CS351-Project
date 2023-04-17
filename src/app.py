from flask import Flask, render_template, request, session, make_response
from pymongo.mongo_client import MongoClient

import db

from common.database import Database
from models.blog import Blog
from models.post import Post
from models.user import User

uri = "mongodb+srv://athira_p:cc-proj@cc-project.jz0cu2o.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
#client = MongoClient('mongodb://localhost:27017/')
client = MongoClient(uri)
db = client['blogs']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Exception -",e)

# def get_db():
#     client = MongoClient(host='test_mongodb',
#                          port=27017, 
#                          username='root', 
#                          password='',
#                         authSource="admin")
#     db = client["animal_db"]
#     return db

app = Flask(__name__)  # '__main__'
app.secret_key = "olga"


@app.route('/')
def home_template():
    return render_template('home.html')

@app.route("/test")
def test():
    db.db.collection.insert_one({"name": "John", "blog_id": 1, "blog_name":"test blog"})
    return "Connected to the data base!"


@app.route('/login')  # www.my_site.com/api/login
def login_template():
    return render_template('login.html')
    # return "hello, world"


@app.route('/register')  # 127.0.0.1:4995/register
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template('profile.html', email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template('profile.html', email=session['email'])


@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])

    blogs = user.get_blogs()

    return render_template("user_blogs.html", blogs=blogs, email=user.email)


@app.route('/posts/<string:blog_id>')
@app.route('/posts')
def blog_posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()

    return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)


@app.route('/blogs/new', methods=['POST', 'GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])

        new_blog = Blog(user.email, title, description, user._id)
        new_blog.save_to_mongo()

        return make_response(user_blogs(user._id))


@app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])

        new_post = Post(blog_id, title, content, user.email)
        new_post.save_to_mongo()

        return make_response(blog_posts(blog_id))


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
