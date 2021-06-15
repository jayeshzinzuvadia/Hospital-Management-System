from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='loginApp'
urlpatterns=[
	path('',views.loginController,name="login"),
	path('login/',views.loginController,name='readlogin'),
	path('registration/', views.view_registration, name="register"),
	path('register/',views.newRegistration,name='newregister'),
	path('logout/', views.logOutController, name='logout'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)