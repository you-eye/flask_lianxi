from flask import Flask, render_template, request, redirect, url_for

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        context = {
            'name': 'zyc',
            'age': '94',
            'li': [1, 2, 3, 4, 5, 6]
        }
        return render_template('register.html', **context)
    else:
        user = request.form.get('username')
        paw = request.form.get('password')
        print(user, paw)
        return redirect(url_for('index'))


@app.route('/index1/')
def index():
    return 'shouye'


if __name__ == '__main__':
    app.run()
