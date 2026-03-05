from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


def load_posts():
    with open("posts.json", "r") as file:
        return json.load(file)


def save_posts(posts):
    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)


@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        posts = load_posts()

        new_post = {
            "id": len(posts) + 1,
            "author": request.form['author'],
            "title": request.form['title'],
            "content": request.form['content']
        }

        posts.append(new_post)

        save_posts(posts)

        return redirect('/')

    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)