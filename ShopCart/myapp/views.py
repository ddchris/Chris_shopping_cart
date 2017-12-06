# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.db import IntegrityError 
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from myapp import views
from myapp import models 
from myapp import form 
from cart.cart import Cart
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
    foods = models.ProductModel.objects.filter(p_category__name__exact ='食物')
    stationeries = models.ProductModel.objects.filter(p_category__name__exact ='文具')
    computers = models.ProductModel.objects.filter(p_category__name__exact ='3C用品')
    necessities = models.ProductModel.objects.filter(p_category__name__exact ='生活用品')

    # 當欲查詢　ForeignKey　屬性時預設會查詢對應之主鍵，如要查別項需用 __name__exact說明

    if request.session.get('login_user'):
        status = 'login'
    else:
        status = ''

    if request.method == 'POST':
        login_account = request.POST['login_account']
        try:
            user = models.UserModel.objects.get(user_account = login_account)
            if request.POST['login_password'] == user.user_password:
                # 確認密碼
                request.session['login_user'] =  login_account  
                # 為使用者儲存自訂(key)名稱為 'login_user' 之 Session
                request.session.set_expiry(7200)  
                # 設定 session 持續 7200 sec

                message = '歡迎光臨! ' + str(user.user_account) + '~ Hooray!'
                g_status = 'login'
                status = g_status
                return render(request,'index.html',locals())

            else:
                message2 = '密碼錯誤 請重新輸入!'
        except ArithmeticError:
            message = '發生問題請先註冊'

    cart = Cart(request)
    #　引入購物車物件

    return render(request,'index.html',locals())


def logout(request):
    request.session.clear()
    auth.logout(request)

    global g_status
    g_status = ''
    status = ''
    return redirect('/index/')


def signin(request):
    message = ''

    if request.method == 'POST':     # 如果接收到表單以POST方式傳送之資料
        try:
           user_form = form.UserModel(request.POST)  # 以 request.POST 取得資料並建立表單
           if user_form.is_valid():      # 如果驗證通過 

               signin_account = user_form.cleaned_data['signin_account'] # 以 form_name.cleaned_data[' '] 收集資料
               signin_email = user_form.cleaned_data['signin_email']
               check_password = user_form.cleaned_data['check_password']
               user_gender = user_form.cleaned_data['user_gender']
           
               # 建立一筆新資料
               new_record = models.UserModel.objects.create(user_account = signin_account, user_password = check_password, user_email = signin_email, user_gender = user_gender )

               # 將新資料存入資料庫
               new_record.save()
               
               # to do by JS  message = '註冊中...完成後將自動返回首頁！'

               send_mail(signin_account,signin_email) # 寄認證信
               return redirect ('/index/') #　驗證成功後返回首頁

           else:
               message = '資料驗證失敗，請重新輸入！'
        except IntegrityError:
            message = '帳號與他人重複 請重新輸入！'
    
    # 此處不可加 else,因網頁必須無條件返回 http　物件
    return render(request,'index.html',locals())

def account_ckeck(request):
    status = ''
    if request.method == 'GET' and request.is_ajax():
        current_account = request.GET.get('current_account')

        status = 'ok'  
        if not current_account:
            status = 'illegal'
            return HttpResponse(status) 

        import re
        # 強迫帳號格式為英文數字混和,並介於5~12個字元
        if re.match(r'^(?=^.{5,12}$)(([a-zA-Z]+\d+|\d+[a-zA-Z]+)[a-zA-Z0-9]*)$', current_account ):
            pass
        else:
            status = 'illegal'
            return HttpResponse(status)

        # 驗證帳號是否重複
        users = models.UserModel.objects.all()
        # objects.all() 格式為大物件包含小物件
        for user in users:
            if user.user_account == current_account: 
               # 以.存取 QuerySet 中物件屬性
                status = 'duplicate'
                return HttpResponse(status)
            else:
                pass
    return HttpResponse(status)

def email_check(request):
    if request.method == 'GET' and request.is_ajax():
        import re
        current_email = request.GET.get('current_email')
        status = 'ok'
        if re.match(r'^[\w-]+@[\w\.-]+\.[a-zA-Z]+$', current_email ):
                return HttpResponse(status)
        else:
            status = 'not_ok'
            return HttpResponse(status)
    return HttpResponse(status)

#@login_required
def add_to_cart(request, product_id, quantity):

    quantity_count = 0
    if request.method == 'GET' and request.is_ajax():
        product = models.ProductModel.objects.get(id = product_id)
        cart = Cart(request)
        cart.add(product, product.p_price, quantity)

        quantity_count = cart.count()
        # 使用 cart 物件之 count() 方法, ps. 要直接執行需有＂括號＂！！　　
        return HttpResponse(quantity_count)
    return HttpResponse(quantity_count)

#@login_required
def remove_from_cart(request, product_id):
    product = models.ProductModel.objects.get(id = product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('/cart/')

#@login_required
def shop_cart(request):

    status = g_status
    all_cateragies = models.Category.objects.all()
    cart = Cart(request)

    return render(request,'cart.html',locals())





 