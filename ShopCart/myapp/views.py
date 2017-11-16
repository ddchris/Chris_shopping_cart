from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.db import IntegrityError 
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from myapp import models
from myapp import form 
import json
from time import sleep

g_status=''

def send_mail(uname,uemail):
    strSmtp = "smtp.gmail.com:587"  #主機	            
    strAccount = "chris2012test@gmail.com"  #帳號
    strPassword = "aaaaaaaaa"  #密碼
    content = '<p>歡迎成為克里斯美食中心會員，請利用下列網址進行認證後即可使用服務: </p>  <a href="http://127.0.0.1:8000/index/' + uname +'"' + '> 我要認證！</a>' #郵件內容
    msg = MIMEText(content, "html", "utf-8")
    msg["Subject"] = "克里斯美食中心-認證信"  #郵件標題
    mailto = uemail  #收件者
	#mailto = ["收件者電子郵件"]  #收件者
	#mailto = ["收件者電子郵件一", "收件者電子郵件二"]

    server = SMTP(strSmtp)  #建立SMTP連線
    server.ehlo()  #跟主機溝通
    server.starttls()  #TTLS安全認證
    try:
        server.login(strAccount, strPassword)  #登入
        server.sendmail(strAccount, mailto, msg.as_string())  #寄信
        hint = "郵件已發送！"
    except SMTPAuthenticationError:
        hint = "無法登入！"
    except:
        hint = "郵件發送產生錯誤！"
    server.quit()  #關閉連線


def index(request):
    global g_status 
    status = g_status    
    message = ''
    message2 = '您好 請先登入'
    foods = models.ProductModel.objects.all()

    if request.method == 'POST':
        user_name = request.POST['user_name']
        try:
            user = models.UserModel.objects.get(uname = user_name)
            if request.POST['password'] == user.upassword:
                request.session['username'] =  user_name  # 'username' 為session 自訂key名稱
                request.session.set_expiry(3600)  # 設定 session 持續 3600 sec
                message = '歡迎光臨! ' + str(user.uname) + '~ Hooray!'
                g_status = 'login'
                status = g_status
                return render(request,'index.html',locals())

            else:
                message2 = '密碼錯誤 請重新輸入!'
        except:
            message = '請先註冊'
    return render(request,'index.html',locals())



def detail(request,id):
    food = models.ProductModel.objects.get(id=id)
    return render(request,'detail.html',locals())

def signin(request):
    message = ''

    if request.method == 'POST':     # 如果接收到表單以POST方式傳送之資料
        try:
           user_form = form.UserModel(request.POST)  # 以 request.POST 取得資料並建立表單
           if user_form.is_valid():      # 如果驗證通過 

               uname = user_form.cleaned_data['uname'] # 以 form_name.cleaned_data[' '] 收集資料
               upassword = user_form.cleaned_data['upassword']
               ugender = user_form.cleaned_data['ugender']
               uemail = user_form.cleaned_data['uemail']
               ubirthday = user_form.cleaned_data['ubirthday']
           
               # 建立一筆新資料
               new_record = models.UserModel.objects.create(uname = uname, upassword = upassword, ugender = ugender, uemail = uemail, ubirthday = ubirthday )

               # 將新資料存入資料庫
               new_record.save()
               
               # to do by JS  message = '註冊中...完成後將自動返回首頁！'

               send_mail(uname,uemail) # 寄認證信

               sleep(3)
               return redirect ('/index/') #　驗證成功後返回首頁

           else:
               message = '資料驗證失敗，請重新輸入！'
        except IntegrityError:
            message = '帳號與他人重複 請重新輸入！'
    
    # 此處不可加 else,因網頁必須無條件返回 http　物件
    return render(request,'signin.html',locals())



def logout(request):
    if  request.session :
        del request.session
    global g_status
    g_status = ''
    return redirect ('/index/')



 