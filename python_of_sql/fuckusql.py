#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, redirect
import MySQLdb

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

    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="login_ad",
                           passwd="test1234",
                           db="user_sos")
    # 欲查詢的 query 指令
    query = "SELECT password FROM people where username LIKE '{}%';".format(
        username)
    # 執行查詢
    cursor = conn.cursor()
    cursor.execute(query)

    results = "none"

    # 取得並列出所有查詢結果
    for (password, ) in cursor.fetchall():
        results = "{}".format(password)

    if (results == "none"):
        print("警告 : 帳號不存在\n輸入帳號:" + username + "\n輸入密碼:" + pw)
    else:
        print("帳號:" + username + "\n輸入密碼:" + pw + "\n實際密碼:" + results + "\n")

    #==============================================

    # 比對帳號密碼是否正確
    if results != pw:
        return redirect('/login/faild')
    else:
        return redirect('/choose')

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

# 進入選課系統
@app.route('/choose', methods=['GET'])  
def into_choose():
    return render_template('choose_main.html')

# 註冊介面 
@app.route('/register', methods=['GET'])  
def show_register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def action_register():
    
    username = request.form.get("username")
    pw = request.form.get("password")
    repw = request.form.get("repassword")
    email = request.form.get("mail")
    birthday = request.form.get("birthday")
    grade = request.form.get("grade")
    photo = request.form.get("user_photo")
    
    
    # 建立資料庫連線
    conn = MySQLdb.connect(host="127.0.0.1",
                           user="login_ad",
                           passwd="test1234",
                           db="user_sos")
    cursor = conn.cursor()
    
    # 檢查是否有相同用戶名的帳號
    query = "SELECT username FROM people WHERE username = %s;"
    cursor.execute(query, (username,))
    existing_user = cursor.fetchone()
    
    if not (username and pw and repw and email and birthday and grade):
        reason = "有欄位未填寫"
        return render_template('register_faild.html', reason=reason)
    elif existing_user:
        reason = "已存在的用戶"
        return render_template('register_faild.html', reason=reason)
    elif pw != repw:
        reason = "兩次密碼不相同"
        return render_template('register_faild.html', reason=reason)
    else:
        # 如果不存在相同用戶名的帳號，則將新用戶的資料插入資料庫
        query = "INSERT INTO people (username, password, mail, birthday, grade, user_photo) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (username, pw, email, birthday, grade, photo))
        conn.commit()
        return redirect('/register/successful')
    
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

if __name__ == '__main__':
    app.run(debug=True)
