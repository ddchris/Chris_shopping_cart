"""
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from datetime import datetime
from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^logout/$', views.logout),
    url(r'^signin/$', views.signin),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^account_ckeck/$', views.account_ckeck),
    url(r'^email_ckeck/$', views.email_check),
    url(r'^cart/$', views.shop_cart),
    url(r'^add_item/(\d+)/(\d+)/$', views.add_to_cart, name = 'additem-url'),
    url(r'^remove_item/(\d+)/$', views.remove_from_cart, name = 'removeitem-url'),
]