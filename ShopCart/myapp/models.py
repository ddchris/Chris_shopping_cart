from django.db import models

# Create your models here.

class ProductModel (models.Model):
    pname = models.CharField ( max_length = 25, default = '')
    pprice = models.IntegerField (default = 0)
    pimgs = models.CharField ( max_length = 100,default = '')
    pdesc = models.TextField ( blank = True ,default = '')
    ponsale = models.BooleanField (default = False)
    pnewproduct = models.BooleanField (default = False)
    def __str__(self):
        return self.pname

class UserModel (models.Model):

    Sex_choices = (('M','M'),('F','F'))

    uname = models.CharField ( max_length = 30, default = 'hello', unique = True)
    upassword = models.CharField ( max_length = 25, default = '')
    ugender = models.CharField (max_length =2 ,choices = Sex_choices,)
    uemail = models.EmailField (max_length = 100, null = True, blank = False)
    ubirthday = models.DateField (null = True)
    def __str__(self):
        return self.uname 
 





