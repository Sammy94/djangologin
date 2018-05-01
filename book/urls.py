from django.conf.urls import url,include
from . import views
app_name="book"
#homepage
urlpatterns=[

url(r'^$',views.index,name='index'),
url(r'^signup$',views.signup,name='signup'),
url(r'^login$',views.login,name='login'),
url(r'^homepage$',views.homepage,name='homepage'),
url(r'^logout$',views.logout_view,name='logout'),
#url(r'^markdownx/', include('markdownx.urls')),


]