from django.contrib import admin
from myapp.models import ProductModel,UserModel 

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id','pname','pprice','pimgs','pdesc','ponsale','pnewproduct')

class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id','uname','upassword','ugender','uemail','ubirthday')

admin.site.register(ProductModel,ProductModelAdmin)

admin.site.register(UserModel,UserModelAdmin)