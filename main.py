from flask import Flask, render_template
from database import todo_list_dao
app = Flask(__name__)

@app.route('/')
def index():

    content_list = todo_list_dao.get_todolist()

    # now = datetime.today()
    # content_list.append(now)

    html = render_template('index.html', data_list=content_list)
    return html

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)