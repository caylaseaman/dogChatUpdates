from flask import Flask, render_template
# from fake_data import dogs, get_post_by_id, add_post_url
from database import get_posts, get_posts_by_handle, get_dogs, get_dog_by_handle
app = Flask(__name__, template_folder="templates", static_url_path='/static')

@app.route('/')
def feed():
    posts = add_post_url()
    return render_template('feed.html', posts=posts)
    
@app.route('/dog/<string:handle>')
def dog(handle):
    dog = get_dog_by_handle(handle)
    return render_template('dog.html', dog=dog, posts=get_posts_by_handle(handle))

@app.route('/post/<string:handle>/<string:id>')
def post(handle, id):
    dog = get_dog_by_handle(handle)
    return render_template('post.html', dog=dog, post=get_post_by_id(id))


def add_post_url():
    results = []
    posts = get_posts()
    dogs = get_dogs()
    for post in posts:
        for dog in dogs:
            sub = "@" + dog['Handle']
            print(sub)
            if sub in post['Text']:
                link = '<a href="/dog/' +dog['Handle'] + '">' + sub + '</a>'
                post['Text'] = post['Text'].replace(sub, link)     
        results.append(post)
    return results

if __name__ == "__main__":
    add_post_url()
    app.run(debug=True)