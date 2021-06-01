from django.urls import path

from . import views
urlpatterns = [
    path('', views.index,name="cloud"),
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('signup',views.register,name="signup"),
    path('folder/<id>',views.viewfolder,name="folder"),
    path('addfolder',views.addfolder,name='addfolder'),
    path('addfile',views.addfile,name='addfile'),
    path('logout', views.logout, name="logout"),
    path('deletecontent',views.deletecontent,name="deletecontent"),
    path('deletefile/<id>',views.deletefile,name="deletefile"),
    path('deletefolder*<id>',views.deletefolder,name="deletefolder")

]
