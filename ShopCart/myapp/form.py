from django import forms

class UserModel (forms.Form):

    Sex_choices = (('M','M'),('F','F'))

    uname = forms.CharField ( min_length = 3, max_length = 12 )
    upassword = forms.CharField ( min_length = 5, max_length = 12 )
    ugender = forms.CharField (max_length =2)
    uemail = forms.EmailField (required = True)
    ubirthday = forms.DateField (required = False) 

