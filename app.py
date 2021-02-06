from flask import Flask, render_template
from fake_data import dogs, posts, get_dog_by_handle, get_posts_by_handle, get_post_by_id, add_post_url

app = Flask(__name__, template_folder="templates", static_url_path='/static')

@app.route('/')
def feed():
    return render_template('feed.html', posts=posts, get_dog_by_handle=get_dog_by_handle)
    
@app.route('/dog/<string:handle>')
def dog(handle):
    dog = get_dog_by_handle(handle)
    return render_template('dog.html', dog=dog, posts=get_posts_by_handle(handle))

@app.route('/post/<string:handle>/<string:id>')
def post(handle, id):
    dog = get_dog_by_handle(handle)
    return render_template('post.html', dog=dog, post=get_post_by_id(id))

if __name__ == "__main__":
    add_post_url()
    app.run(debug=True)