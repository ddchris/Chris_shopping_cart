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
    url(r'^detail/(\d+?)/$',views.detail),
    url(r'^signin/$', views.signin),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^account_ckeck/$', views.account_ckeck),
    url(r'^email_ckeck/$', views.email_check),
]