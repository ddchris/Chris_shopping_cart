# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class ProductModel (models.Model):
    p_name = models.CharField ( max_length = 25, default = '')
    p_price = models.IntegerField (default = 0)
    p_imgs = models.CharField ( max_length = 100,default = '')
    p_desc = models.TextField ( blank = True ,default = '')
    p_onsale = models.BooleanField (default = False)
    p_newproduct = models.BooleanField (default = False)
    def __str__(self):
        return self.p_name
 
class UserModel (models.Model):

    sex_choices = (('M','M'),('F','F'))

    user_account = models.CharField ( max_length = 30, default = 'hello', unique = True)
    user_password = models.CharField ( max_length = 25, default = '')
    user_email = models.EmailField (max_length = 100, null = True, blank = False)
    user_gender = models.CharField (max_length =2 ,choices = sex_choices)


    def __str__(self):
        return self.user_account






