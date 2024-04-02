#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, redirect ,url_for
import MySQLdb
import domi_classlist ,domi_login ,domi_account

app = Flask(__name__)

# 預設導向

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/menu', methods=['POST'])
def action_menu():
    go_login = request.form.get("login")
    go_register = request.form.get("register")

    if go_login:
        return redirect('/login')
    elif go_register:
        return redirect('/register')

# 登入介面 
@app.route('/login', methods=['GET'])  
def show_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def action_login():
    
    username = request.form.get("username")
    pw = request.form.get("password")

    results = domi_login.check_login(username,pw)

    if results == 0:
        return redirect('/login/faild')
    elif results == 1:
        return redirect('/admin/do/u/want/to/build/the/snowman')
    else:
        return redirect(url_for('into_choose', username=username))

# 登入失敗介面
@app.route('/login/faild', methods=['GET'])  
def login_faild():
    return render_template('login_faild.html')

@app.route('/login_faild', methods=['POST'])
def action_login_faild():
    go_menu = request.form.get("backtomenu")
    go_login = request.form.get("backtologin")

    if go_login:
        return redirect('/login')
    elif go_menu:
        return redirect('/')
    
@app.route('/admin/do/u/want/to/build/the/snowman', methods=['GET'])  
def into_admin():
    return render_template('admin.html')

# 註冊介面 
@app.route('/register', methods=['GET'])  
def show_register():
    # print(domi_classlist.get_department_names()) #debug show class list
    mylist = domi_classlist.get_department_names()
    return render_template('register.html', class_list = mylist )

@app.route('/register', methods=['POST'])
def action_register():
    
    username = request.form.get("username")
    pw = request.form.get("password")
    repw = request.form.get("repassword")
    email = request.form.get("mail")
    birthday = request.form.get("birthday")
    grade = request.form.get("grade")
    photo = request.form.get("user_photo")
    Department = request.form.get("Department")

    reason = domi_account.check_createsuccessful(username ,pw ,repw ,email ,birthday ,grade ,Department ,photo)

    if (reason == 1):
        domi_account.insert_newaccount(username, pw, email, birthday, grade, Department, photo)
        return redirect('/register/successful')
    else:
        return render_template('register_faild.html', reason=reason)
    
# 註冊失敗介面
@app.route('/register/faild', methods=['GET'])  
def register_faild():
    return render_template('register_faild.html')

@app.route('/register_faild', methods=['POST'])
def action_register_faild():
    go_menu = request.form.get("backtomenu")
    go_register = request.form.get("backtoregister")

    if go_register:
        return redirect('/register')
    elif go_menu:
        return redirect('/')
    
# 註冊成功介面
@app.route('/register/successful', methods=['GET'])  
def register_successful():
    return render_template('register_successful.html')

@app.route('/register_successful', methods=['POST'])
def action_register_successful():
    go_login = request.form.get("go_login")

    if go_login:
        return redirect('/login')

# 進入選課系統
@app.route('/choose/<username>')  
def into_choose(username):
    return render_template('choose_main.html', username=username)

@app.route('/choose_main', methods=['POST'])
def choose_main():
    go_login = request.form.get("backtomenu")

    if go_login:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
