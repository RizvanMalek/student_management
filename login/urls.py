from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('login_model/',views.login_model,name='login_model'),
    path('logout/',views.logout_model,name='logout_model'),
    # path('',include('students.urls')),
]

