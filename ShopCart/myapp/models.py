# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField (max_length = 150 )
    def __str__(self):
        return self.name
    # 複寫列印類別實例的方法, 使其顯示類別名稱

class ProductModel (models.Model):
    p_category = models.ForeignKey (Category, on_delete= models.CASCADE, null=True )
    p_name = models.CharField ( max_length = 25, default = '')
    p_price = models.IntegerField (default = 0)
    p_imgs = models.CharField ( max_length = 100,default = '')
    p_desc = models.TextField ( blank = True ,default = '')
    p_onsale = models.BooleanField (default = False)
    p_newproduct = models.BooleanField (default = False)
    def __str__(self):
        return self.p_name
 
class UserModel (models.Model):

    sex_choices = (('M','Male'),('F','Female'))
    # 第一個項目是實際要儲存的內容, 後面的項目是後臺內對應的說明

    user_account =  ( models.CharField ( max_length = 30,default = '', unique = True) )
    user_password = models.CharField ( max_length = 25, default = '')
    user_email = models.EmailField(max_length = 100, null = True, blank = False)
    user_gender = models.CharField (max_length = 2 ,choices = sex_choices)


    def __str__(self):
        return self.user_account

class Order(models.Model):
    usermodel = models.ForeignKey (UserModel, on_delete = models.CASCADE)
    # 每張訂單需指向唯一的客戶 (多對一), 當客戶不存在時訂單也會跟個被刪除

    full_name = models.CharField (max_length = 35)
    address = models.CharField (max_length = 150)
    phone = models.CharField (max_length = 15)
    create_time = models.DateTimeField (auto_now_add = True)
    update_time = models.DateTimeField (auto_now = True)
    paid = models.BooleanField (default = False)

    class Meta:
        ordering = ('-create_time',)
    def __str__(self):
        return 'Order : {}'.format(self.id)

class OrderList(models.Model):
    product = models.ForeignKey(ProductModel, on_delete = models.CASCADE, related_name = 'items')
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    #  設定價錢屬於小數型別, 總位數8位, 其中小數點後佔2位
    quantity = models.PositiveIntegerField (default = 1)

    def __str__(self):
        return '{}'.format(self.id)












