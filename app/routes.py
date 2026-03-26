from flask import Blueprint, render_template, jsonify, request, redirect, url_for
import os
from datetime import datetime, timezone

bp = Blueprint('main', __name__)

todos = []
_next_id = 1


@bp.route('/', methods=['GET'])
def index():
    error = request.args.get('error')
    return render_template('todo.html', todos=todos, app_name=os.environ.get('APP_NAME', 'Cloud Run To-Do'), error=error)


@bp.route('/add', methods=['POST'])
def add():
    global _next_id
    title = (request.form.get('title') or '').strip()
    if not title:
        return redirect(url_for('main.index'))
    todos.append({'id': _next_id, 'title': title, 'created': datetime.now(timezone.utc).isoformat()})
    _next_id += 1
    return redirect(url_for('main.index'))


@bp.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    # deletion requires the secret from the .env (sent in form as `secret`)
    secret = request.form.get('secret') or request.headers.get('X-ADMIN-SECRET')
    if secret != os.environ.get('TODO_SECRET', 'idk'):
        # redirect back with error flag to show a friendly message instead of generic 403 page
        return redirect(url_for('main.index', error='forbidden'))
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return redirect(url_for('main.index'))


@bp.route('/time')
def time():
    return jsonify({'utc': datetime.now(timezone.utc).isoformat()})


@bp.route('/info')
def info():
    keys = ['PROJECT_ID', 'GAE_SERVICE', 'PORT']
    env = {k: os.environ.get(k) for k in keys}
    return jsonify({'env': env})


@bp.route('/health')
def health():
    return 'OK', 200
