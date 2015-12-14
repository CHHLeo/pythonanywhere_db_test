from flask import Flask, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=False)
    is_completed = db.Column(db.Boolean)

    def __init__(self, title):
        self.title = title
        self.is_completed = False


# user_name = 'root'
# password = ''
# database_host_address = 'localhost:3306'
# database_name = 'test'
user_name = 'ch2leo'
password = '21070527'
database_host_address = 'ch2leo.mysql.pythonanywhere-services.com'
database_name = 'ch2leo$test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://' + user_name + ':' + password + '@' + database_host_address + '/' + database_name
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db.create_all()


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    db.session.add(Todo(title=request.form['title']))
    db.session.commit()
    return redirect('/')


app.debug = True

if __name__ == '__main__':
    app.run()
