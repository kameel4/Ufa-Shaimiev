from flask import Flask, redirect, render_template, flash, url_for
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

info = {}


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(' Сработал POST')
        return render_template("post.html", form=form)
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
