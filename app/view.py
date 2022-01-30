from web.app import app
from flask import render_template, request, session, flash, redirect, url_for, sessions
from web.app.dbcreateuser import DBCreateUser
from web.app.dblogin import DBLogin
from datetime import datetime

@app.route('/home/<username>')
def home(username):
    return render_template('base.html', name=username)

@app.route('/register', methods=['post', 'get'])
def register():
    # принимаем логин и пароль из веб формы login
    login = request.form.get('login')
    password = request.form.get('password')
    # если createUser вернул ошибку, то вывести ее пользователю
    # если формы логин и пароль не заполнены
    if login == None and password == None:
        return render_template('register.html')
    # если имя уже есть в БД вывести ошибку
    elif DBCreateUser().createUser(login,password) == 'login incorrect':
        test = 'login incorrect'
    # если ошибки нет то вывести логин
    else:
        test = str(login)
    return render_template('register.html', test=test)

@app.route('/login', methods=['get','post'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    # экземпляр класса проверки пользователя
    testInput = DBLogin()
    # если формы логин и пароль не заполнены
    if login == None and password == None:
        return render_template('login.html')
    elif testInput.login(login, password):
    # заполняем сессионные куки (логин, дата-время)
        session['user_login'] = login
        session['time_date'] = datetime.now()
        test = 'Sucsess login'
    else:
        test = 'False'
    return render_template('login.html', test=test)

@app.route('/welcome', methods=['get','post'])
def welcome():
    # добавить ограничение по времени (проблемы с удаление временной зоны в куках)
    print(session.get('time_date'))
    print(datetime.now(tz=None))

    if not session.get('user_login'):
        flash("Please log in first")
        return redirect(url_for('login'))
    else:
        return render_template('welcome.html')

@app.route('/exit', methods=['get','post'])
def exit():
    flash('Выход выполнен')
    session.clear()
    return redirect(url_for('login'))

