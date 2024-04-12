#/usr/bin/python
from flask import Flask,render_template

app = Flask(__name__)  #__name__ is the name of the module which we are passing to Flask claas

#Multiple route handled by same function using a decorator

posts = [
            {
                'author': 'Abhi Mukh',
                'title': 'Blog post 1',
                'content': 'First post content',
                'date_posted': 'Aug 9, 2022'
            },
            {
                'author': 'Abhi Mukh',
                'title': 'Blog post 1',
                'content': 'First post content',
                'date_posted': 'Aug 9, 2022'
            }
        ]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    #whatever variable name we pass to render_template it will have access in the template

@app.route("/about")
def about():
    return render_template('about.html', title ='About')




if __name__ == '__main__':
    print("In main")
    app.run(debug=True)
