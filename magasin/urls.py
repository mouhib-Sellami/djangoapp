from django.urls import path
from . import views
urlpatterns = [
    path("vetrine",views.index,name="vetrine"),
    path('shop',views.shop,name="shop"),
    path('',views.vetrine,name=""),
    path('forni',views.forni,name="forni"),
    path('forniprod/<id>',views.forniprod,name="forniprod"),
    path('viewshop',views.viewshop,name="viewshop"),
        path('deleteforni/<id>',views.deleteforni,name="deleteforni"),
    path('addforni',views.addforni,name="addforni"),
    path('deletecom/<id>',views.deletecom,name="deletecom"),
]