from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
      'author': 'Cedric Sambaan',
      'title': 'Blog Post 1',
      'content': 'First Post Content',
      'date_posted': 'October 13, 2021'  
    },
    {
      'author': 'Jane Doe',
      'title': 'Blog Post 2',
      'content': 'Second Post Content',
      'date_posted': 'October 14, 2021'  
    }
]


def main():
    app.run(debug=True)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title= 'About')


if __name__ == "__main__":
    main()