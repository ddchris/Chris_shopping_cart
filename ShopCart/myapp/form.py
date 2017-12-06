# -*- coding: utf-8 -*-

from django import forms

class UserModel (forms.Form):

    Sex_choices = (('M','M'),('F','F'))

    signin_account = forms.CharField ( min_length = 3, max_length = 12 )
    signin_email = forms.EmailField (required = True)
    check_password = forms.CharField ( min_length = 5, max_length = 12 )
    user_gender = forms.CharField (max_length =2)
 
 