from flask import Blueprint, render_template
from app.posts.dao.posts_dao import PostsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO("data/posts.json")

@posts_blueprint.route('/')
def posts_all():

    try:
        posts = posts_dao.get_all()
        return render_template("index.html", posts=posts)
    except:
        return "Что-то пошло не так"


@posts_blueprint.route('/posts/<int:post_bk >/')
def posts_one(post_id):

    try:
        post = posts_dao.get_by_pk(post_id)
        return render_template("post.html", post=post)
    except:
        return "Произошла ошибка при получении поста"


@posts_blueprint.route('/search/')
def posts_search():
    return "Поиск по постам"


@posts_blueprint.route('/users/<username>/')
def posts_by_user(username):
    return "Поиск по пользователям"
