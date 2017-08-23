#!/usr/bin/env python3

from flask import Flask, render_template, request
from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='$$',
        block_end_string='$$',
        variable_start_string='$',
        variable_end_string='$',
        comment_start_string='$#',
        comment_end_string='#$'
    ))

app = CustomFlask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

@app.route('/')
def home_page():
    data = {}
    return render_template('home.html', **data)

@app.route('/teams')
def people_page():
    data = {}
    return render_template('teams.html', **data)

@app.route('/news')
def news_page():
    data = {}
    return render_template('news.html', **data)

@app.route('/tools')
def tools_page():
    data = {}
    return render_template('tools.html', **data)


@app.route('/api', methods=['GET', 'POST'])
def some_api():
    if request.method == 'POST':
        do_something()
    else:
        show_something()

if __name__ == '__main__':
    #use animate.css and waypoints
    app.run(debug=True)
    # app.run(host='0.0.0.0', debug=True)
