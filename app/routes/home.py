from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = (
        db
            .query(Post)
            .order_by(Post.created_at.desc())
            .all()
    )
    #the posts=posts renders the template with posts data
    return render_template('homepage.html', posts=posts)

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>')
def single(id):
    #gets single post by id
    db = get_db()
    #use filter method on connection object to specify the SQL where clause
    #use one method instead of all to grab single post
    post = db.query(Post).filter(Post.id == id).one()
    return render_template('single-post.html', post=post)