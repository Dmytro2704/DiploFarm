from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    path("",views.index, name='index'),
    path("about",views.about, name="about"),
    path("blog",views.blog, name="blog"),
    path("contact",views.contact, name="contact"),
    path("products",views.products, name="products"),



    # path('category/<str:name>',views.category, name="category"),
    # path('search',views.search, name='search'),

    # path('login', LoginView.as_view(), name='blog_login'),
    # path('logout', LogoutView.as_view(), name='blog_logout')



]