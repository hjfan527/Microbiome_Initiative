from flask import Flask, render_template

# This class creates custom delimiters for jinja variables
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
    block_start_string='$$',
    block_end_string='$$',
    variable_start_string='$',
    variable_end_string='$',
    comment_start_string='$#',
    comment_end_string='#$',
    ))

app = CustomFlask(__name__)

@app.route('/')
def hello_world():
    data = {'content':  'This is the body', 'title': 'This is the title', 'heading': 'HEADING'}
    return render_template('index.html', **data)

if __name__ == '__main__':
   app.run(debug=True)

