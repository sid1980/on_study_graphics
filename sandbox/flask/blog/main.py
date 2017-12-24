# coding: utf-8

import os
from flask import Flask, render_template
from werkzeug import cached_property
import markdown


POST_FILE_EXTENSION = '.md'
app = Flask(__name__)

class Post(object):
    def __init__(self, path):
        self.path = path

    #@property
    @cached_property
    def html(self):
        with open(self.path, 'r') as fin:
            content = fin.read().strip()
        return markdown.markdown(content)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/blog')
def blog():
    print('blog')
    return 'Hello, World! - blog'

# @app.route('/blog/post/')
@app.route('/blog/<path:path>/')
def blog_post(path):
    # import ipdb; ipdb.set_trace()
    # return 'Hello, World! - blog/post'
    path = os.path.join('posts', path + POST_FILE_EXTENSION)
    post = Post(path)
    # return render_template('post.html', post_content='Hello, World! (from template)')
    return render_template('post.html', post=post)

if __name__ == '__main__':
    # app.run(debug=True, port=8000)
    app.run(debug=True, port=8000)