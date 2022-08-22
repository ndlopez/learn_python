from flask import (Blueprint, flash,g,redirect,render_template,request,url_for)
from werkzeug.exceptions import abort

from flaskr_blog.auth import login_required
from flaskr_blog.db import get_db

bp = Blueprint('blog',__name__)

@bp.route('/')
def index():
    db = get_db()
    allPosts = db.execute(
        'SELECT p.id,title,body,created_on, author_id, username '
        'FROM post p JOIN user u ON p.author_id = u.id '
        'ORDER BY created_on DESC'
    ).fetchall()

    return render_template('blog/index.html',posts=allPosts)

def get_post(id,check_author=True):
    myPost = get_db().execute(
        'SELECT p.id, title, body, created_on, author_id, username '
        'FROM post p JOIN user u ON p.author_id = u.id '
        'WHERE p.id = ?',(id,),
    ).fetchone()

    if myPost is None:
        abort(404,f"Post id {id} does not exist") #Not found msg
    if check_author and myPost['author_id'] != g.user['id']:
        abort(403) #Forbidden access
    return myPost

@bp.route('/create',methods=('GET','POST'))
@login_required
def create():
    """create a new post for the current user"""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        if not title:
            error = 'Sorry, title is required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title,body,author_id) VALUES (?,?,?)',(title,body,g.user['id']),
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

@bp.route('/<int:id>/update',methods=('GET','POST'))
@login_required
def update(id):
    """update a post if the current user is the author"""
    thisPost = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is kinda required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ? WHERE id = ?',(title,body,id)
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html",post=thisPost)

@bp.route('/<int:id>/delete',methods=('POST',))
@login_required
def delete(id):
    """delete a post if the post exists and belongs to the logged user"""
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id=?',(id,))
    db.commit()
    return redirect(url_for('blog.index'))