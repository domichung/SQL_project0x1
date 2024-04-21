#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, redirect ,url_for ,session
import  domi_registerlist ,domi_login ,domi_account,domi_dice_classlist
import  domi_userlist ,domi_adminsys ,domi_newlogin
import  domi_listmyclass,domi_replacearr,domi_loadcanichoose
import  domi_addclass,domi_loadcanileave,alb_deleteClass,domi_classnamepromax


app = Flask(__name__)
app.secret_key = 'safe_key'

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/admin_choose/<login_admin>', methods=['GET'])
def rou_admin_choose(login_admin):
    session['adm_name'] = login_admin  
    return redirect(url_for('rou_admin'))

@app.route('/admin', methods=['GET'])
def rou_admin():
    list_all_student = domi_userlist.get_students_names()
    return render_template('admin.html', adm = session.get('adm_name', '空白使用者') , student_list = list_all_student )

@app.route('/admin/setuser/<settinguser>', methods=['GET'])
def rou_setuser_choose(settinguser):
    session['besettinguser'] = settinguser  
    return redirect(url_for('rou_admin_setuser'))

@app.route('/admin/setuser', methods=['GET'])
def rou_admin_setuser():
    
    settinguser = session.get('besettinguser', '請選擇用戶')
    admname = session.get('adm_name', '空白使用者')

    if (settinguser == "請選擇用戶"):
        print("empty input")
        return redirect(url_for('rou_admin'))
    else:

        load_sys = domi_adminsys.find_people_data(settinguser)

        return render_template('admin_change.html', 
                                admname = admname , 
                                settinguser = settinguser ,
                                userid = load_sys[0][0],
                                userpassword = load_sys[0][2],
                                useremail = load_sys[0][3],
                                usergrade = load_sys[0][5],
                                userbirth = load_sys[0][4], 
                                usermoreclass = load_sys[0][7],
                                userdepartment = load_sys[0][6],
                                userchoosenotherdepartment = load_sys[0][12],
                                first_check = load_sys[0][10], 
                                ABCDclass = load_sys[0][11],
                                list_all_class = domi_registerlist.get_class_names(),
                                list_all_department = domi_registerlist.get_department_names(), 
                                list_all_grade = domi_registerlist.get_grade_names())

@app.route('/login', methods=['GET'])
def rou_login():
    return render_template('login.html')

@app.route('/loginfaild', methods=['GET'])
def rou_login_f():
    return render_template('login_faild.html')

@app.route('/register', methods=['GET'])
def rou_register():
    list_all_department = domi_registerlist.get_department_names()
    list_all_class = domi_registerlist.get_class_names()
    list_all_grade = domi_registerlist.get_grade_names()
    return render_template('register.html', class_list = list_all_class, department_list = list_all_department, grade_list = list_all_grade )

@app.route('/registerfaild', methods=['GET'])
def rou_register_f():
    return render_template('register_faild.html')

@app.route('/registersuccess', methods=['GET'])
def rou_register_s():
    return render_template('register_successful.html')

#================================選課路由
#=============幹你娘寫一半===============

@app.route('/choose/<choose_user_id>', methods=['GET'])
def rou_choose_setuser(choose_user_id):
    session['choose_user'] = choose_user_id  
    return redirect(url_for('rou_choose_mainpage'))

@app.route('/choose/main', methods=['GET'])
def rou_choose_mainpage():
    studentid = session.get('choose_user', 'NULLID')
    classlist = domi_replacearr.replace(domi_listmyclass.get_students_classlist(studentid))
    studentname = domi_account.find_name_id(studentid)
    studentbonusclass = domi_account.find_moreclass_byid(studentid)
    nowchoosepoin = domi_account.find_userclasscount_byid(studentid)
    class_ineed = domi_loadcanichoose.simplify_courses(domi_loadcanichoose.givemeallcalss())
    try:
        will_list = domi_dice_classlist.read_userwillchooselist(studentid)
    except:
        will_list = "尚未預選"

    timeSlots = [
    "第 一 節 08:10 ~ 09:00",
    "第 二 節 09:10 ~ 10:00",
    "第 三 節 10:10 ~ 11:00",
    "第 四 節 11:10 ~ 12:00",
    "第 五 節 12:10 ~ 13:00",
    "第 六 節 13:10 ~ 14:00",
    "第 七 節 14:10 ~ 15:00",
    "第 八 節 15:10 ~ 16:00",
    "第 九 節 16:10 ~ 17:00",
    "第 十 節 17:10 ~ 18:00",
    "第十一節 18:30 ~ 19:20",
    "第十二節 19:25 ~ 20:15",
    "第十三節 20:25 ~ 21:15",
    "第十四節 21:20 ~ 22:10"
    ]

    if (session.get('showmode',"0") == 1):
        classlist = domi_classnamepromax.promax_input(classlist)
        will_list = domi_classnamepromax.promax_input(will_list)

    counter = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

    return render_template('choose_main.html', studentname = studentname, classlist=classlist 
                                             , timeSlots = timeSlots ,counter = counter 
                                             , studentbonusclass = studentbonusclass 
                                             , nowchoosepoin = nowchoosepoin, class_ineed = class_ineed
                                             , will_list = domi_classnamepromax.promax_input_string(will_list))

#=========================退選路由

@app.route('/choose/leave/<unchoose_user_id>', methods=['GET'])
def rou_unchoose_setuser(unchoose_user_id):
    session['choose_user'] = unchoose_user_id
    return redirect(url_for('rou_unchoose_mainpage'))

@app.route('/choose/unchoose', methods=['GET'])
def rou_unchoose_mainpage():
    studentid = session.get('choose_user', 'NULLID')
    classlist = domi_replacearr.replace(domi_listmyclass.get_students_classlist(studentid))
    studentname = domi_account.find_name_id(studentid)
    studentbonusclass = domi_account.find_moreclass_byid(studentid)
    nowchoosepoin = domi_account.find_userclasscount_byid(studentid)
    class_ineed = domi_loadcanichoose.simplify_courses(domi_loadcanileave.unchoose_list(studentid))

    try:
        will_list = domi_dice_classlist.read_userwillchooselist(studentid)
    except:
        will_list = "尚未預選"

    timeSlots = [
    "第 一 節 08:10 ~ 09:00",
    "第 二 節 09:10 ~ 10:00",
    "第 三 節 10:10 ~ 11:00",
    "第 四 節 11:10 ~ 12:00",
    "第 五 節 12:10 ~ 13:00",
    "第 六 節 13:10 ~ 14:00",
    "第 七 節 14:10 ~ 15:00",
    "第 八 節 15:10 ~ 16:00",
    "第 九 節 16:10 ~ 17:00",
    "第 十 節 17:10 ~ 18:00",
    "第十一節 18:30 ~ 19:20",
    "第十二節 19:25 ~ 20:15",
    "第十三節 20:25 ~ 21:15",
    "第十四節 21:20 ~ 22:10"
    ]

    counter = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

    if (session.get('showmode',"0") == 1):
        classlist = domi_classnamepromax.promax_input(classlist)
        will_list = domi_classnamepromax.promax_input(will_list)

    return render_template('unchoose_main.html', studentname = studentname, classlist=classlist 
                                             , timeSlots = timeSlots ,counter = counter 
                                             , studentbonusclass = studentbonusclass 
                                             , nowchoosepoin = nowchoosepoin, class_ineed = class_ineed
                                             , will_list = domi_classnamepromax.promax_input_string(will_list))

#=========================預選路由

@app.route('/choose/will/<willchoose_user_id>', methods=['GET'])
def rou_willchoose_setuser(willchoose_user_id):
    session['choose_user'] = willchoose_user_id
    return redirect(url_for('rou_willchoose_mainpage'))

@app.route('/choose/willchoose', methods=['GET'])
def rou_willchoose_mainpage():
    studentid = session.get('choose_user', 'NULLID')
    classlist = domi_replacearr.replace(domi_listmyclass.get_students_classlist(studentid))
    studentname = domi_account.find_name_id(studentid)
    studentbonusclass = domi_account.find_moreclass_byid(studentid)
    nowchoosepoin = domi_account.find_userclasscount_byid(studentid)
    class_ineed = domi_loadcanichoose.simplify_courses(domi_loadcanichoose.givemeallcalss())

    try:
        will_list = domi_dice_classlist.read_userwillchooselist(studentid)
    except:
        will_list = "尚未預選"

    timeSlots = [
    "第 一 節 08:10 ~ 09:00",
    "第 二 節 09:10 ~ 10:00",
    "第 三 節 10:10 ~ 11:00",
    "第 四 節 11:10 ~ 12:00",
    "第 五 節 12:10 ~ 13:00",
    "第 六 節 13:10 ~ 14:00",
    "第 七 節 14:10 ~ 15:00",
    "第 八 節 15:10 ~ 16:00",
    "第 九 節 16:10 ~ 17:00",
    "第 十 節 17:10 ~ 18:00",
    "第十一節 18:30 ~ 19:20",
    "第十二節 19:25 ~ 20:15",
    "第十三節 20:25 ~ 21:15",
    "第十四節 21:20 ~ 22:10"
    ]

    counter = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

    if (session.get('showmode',"0") == 1):
        classlist = domi_classnamepromax.promax_input(classlist)
        will_list = domi_classnamepromax.promax_input(will_list)

    return render_template('willchoose_main.html', studentname = studentname, classlist=classlist 
                                             , timeSlots = timeSlots ,counter = counter 
                                             , studentbonusclass = studentbonusclass 
                                             , nowchoosepoin = nowchoosepoin, class_ineed = class_ineed
                                             , will_list = domi_classnamepromax.promax_input_string(will_list))

#=========================以下腳本

@app.route('/menu', methods=['POST'])
def script_menu():

    go_login = request.form.get("login")
    go_register = request.form.get("register")

    if go_login:
        return redirect('/login')
    elif go_register:
        return redirect('/register')

@app.route('/admin', methods=['POST'])
def script_admin():
    set_username = request.form.get("change_user")
    start_set_user = request.form.get("set_people")
    go_login = request.form.get("backtomenu")
    if go_login:
        return redirect('/')
    elif start_set_user:
        print(domi_adminsys.find_people_data(set_username))
        return redirect(url_for('rou_setuser_choose', settinguser=set_username))

@app.route('/admin_change', methods=['POST'])
def script_admin_change():
    
    settinguser = session.get('besettinguser', '不存在的值')
    settinguserid = domi_adminsys.find_people_data(settinguser)[0][0]

    username = request.form.get("username")
    pw = request.form.get("password")
    email = request.form.get("email")
    birthday = request.form.get("birthday")
    grade = request.form.get("grade")
    chosenotheredepartment = request.form.get("chosenotheredepartment")
    Department = request.form.get("department")
    moreclass = request.form.get("moreclass")
    newusercheck = request.form.get("first_login_check")
    abcdclass = request.form.get("ABCD_CLASS")

    start_set_user = request.form.get("set_people")
    go_login = request.form.get("backtomenu")
    if go_login:
        return redirect('/')
    elif start_set_user:
        print("更改用戶:"+str(settinguserid))
        domi_adminsys.change_user_info(settinguserid ,username ,pw ,email ,birthday ,grade ,chosenotheredepartment ,Department ,moreclass ,newusercheck ,abcdclass)
        return redirect(url_for('rou_admin'))

@app.route('/choose_main_change', methods=['POST'])
def script_change_page():
    next1 = request.form.get("add")
    next2 = request.form.get("kill")
    next3 = request.form.get("wait")
    next4 = request.form.get("showchange")
    idcallback = session.get('choose_user', 'NULLID')
    if next1:
        #print("case1")
        return redirect(url_for('rou_choose_setuser', choose_user_id = idcallback))
    if next2:
        #print("case2")
        return redirect(url_for('rou_unchoose_setuser', unchoose_user_id = idcallback))
    if next3:
        #print("case3")
        return redirect(url_for('rou_willchoose_setuser', willchoose_user_id = idcallback))
    if next4:
        if (session.get('showmode',"0") == 1):
            session['showmode'] = 0
        else:
            session['showmode'] = 1
        return redirect(url_for('rou_choose_setuser', choose_user_id = idcallback))


@app.route('/choose_main', methods=['POST'])
def script_choose():
    next = request.form.get("test")
    test = request.form.get("showchange")
    willaddclass = request.form.get("chooselist").split()[0]
    studentid = session.get('choose_user', 'NULLID')
    #print(willaddclass + "!!!!!!!!!!!!!!!!!!!!")

    #if (test == "on"):
        #print("a")

    if next:
        reason = domi_addclass.add_userclass(studentid,willaddclass)
        if (reason == "success"):
            return render_template('choose_success.html',name= willaddclass)
        else:
            return render_template('choose_faild.html',reason = reason)

@app.route('/choose_faild', methods=['POST'])
def script_choose_faild():
    back = request.form.get("backtochoose")
    idcallback = session.get('choose_user', 'NULLID')
    if back:
        return redirect(url_for('rou_choose_setuser', choose_user_id = idcallback))

@app.route('/choose_success', methods=['POST'])
def script_choose_success():
    back = request.form.get("backtochoose")
    idcallback = session.get('choose_user', 'NULLID')
    if back:
        return redirect(url_for('rou_choose_setuser', choose_user_id = idcallback))
    

@app.route('/unchoose_main', methods=['POST'])
def script_unchoose():
    next = request.form.get("setting")
    willdeleteclass = request.form.get("unchooselist").split()[0]
    studentid = session.get('choose_user', 'NULLID')
    if next:
        try:
            reason = alb_deleteClass.delete_user_class(willdeleteclass,studentid)
            if (reason == "success"):
                return render_template('unchoose_success.html',name= willdeleteclass)
            else:
                return render_template('unchoose_faild.html',reason = reason)
        except:
            return render_template('unchoose_faild.html',reason = "你尚未選取要退選課")
        
@app.route('/unchoose_faild', methods=['POST'])
def script_unchoose_faild():
    back = request.form.get("backtochoose")
    idcallback = session.get('choose_user', 'NULLID')
    if back:
        return redirect(url_for('rou_unchoose_setuser', unchoose_user_id = idcallback))

@app.route('/unchoose_success', methods=['POST'])
def script_unchoose_success():
    back = request.form.get("backtochoose")
    idcallback = session.get('choose_user', 'NULLID')
    if back:
        return redirect(url_for('rou_unchoose_setuser', unchoose_user_id = idcallback))
    
@app.route('/willchoose_main', methods=['POST'])
def script_willchoose():
    next = request.form.get("setting")
    willclass = request.form.get("willchooselist").split()[0]
    studentid = session.get('choose_user', 'NULLID')
    if next:
        reason = domi_dice_classlist.dic_main(studentid,willclass)
        if (reason == "success"):
            return render_template('willchoose_success.html',name= willclass)
        else:
            return render_template('willchoose_faild.html',reason = reason)
        
@app.route('/willchoose_faild', methods=['POST'])
def script_willchoose_faild():
    back = request.form.get("backtochoose")
    idcallback = session.get('choose_user', 'NULLID')
    if back:
        return redirect(url_for('rou_willchoose_setuser', willchoose_user_id = idcallback))

@app.route('/willchoose_success', methods=['POST'])
def script_willchoose_success():
    back = request.form.get("backtochoose")
    idcallback = session.get('choose_user', 'NULLID')
    if back:
        return redirect(url_for('rou_willchoose_setuser', willchoose_user_id = idcallback))


@app.route('/login', methods=['POST'])
def script_login():

    username = request.form.get("username")
    pw = request.form.get("password")

    results = domi_login.check_login(username,pw)
    idcallback = domi_account.find_id(username)

    if results == 0:
        return redirect('/loginfaild')
    elif results == 1:
        return redirect(url_for('rou_admin_choose', login_admin = username))
    else:
        if (results == 3):
            print("尚未登入過開始建立課表\n")
            domi_newlogin.newclasslist_main(idcallback)
        elif (results == 2):
            print("已經登入過囉歡迎回來\n")

        session['showmode'] = 0
        return redirect(url_for('rou_choose_setuser', choose_user_id = idcallback))

@app.route('/login_faild', methods=['POST'])
def script_login_f():
    go_menu = request.form.get("backtomenu")
    go_login = request.form.get("backtologin")

    if go_login:
        return redirect('/login')
    elif go_menu:
        return redirect('/')

@app.route('/register', methods=['POST'])
def script_register():
    username = request.form.get("username")
    pw = request.form.get("password")
    repw = request.form.get("repassword")
    email = request.form.get("mail")
    birthday = request.form.get("birthday")
    grade = request.form.get("grade")
    photo = request.form.get("user_photo")
    Department = request.form.get("Department")
    myABCD_class = request.form.get("ABCD_class")

    reason = domi_account.check_createsuccessful(username ,pw ,repw ,email ,birthday ,grade ,Department ,photo ,myABCD_class)

    if (reason == 1):
        domi_account.insert_newaccount(username, pw, email, birthday, grade, Department, photo, myABCD_class)
        return redirect('/registersuccess')
    else:
        return render_template('register_faild.html', reason=reason)

@app.route('/register_faild', methods=['POST'])
def script_register_f():

    go_menu = request.form.get("backtomenu")
    go_register = request.form.get("backtoregister")

    if go_register:
        return redirect('/register')
    elif go_menu:
        return redirect('/')

@app.route('/register_successful', methods=['POST'])
def script_register_s():
    go_login = request.form.get("go_login")
    if go_login:
        return redirect('/login')
    

if __name__ == '__main__':
    app.run(debug=True)