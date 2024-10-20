from django.urls import path

from library.views import home_view,products_view

urlpatterns = [
    path('',home_view, name='home'),
    path('library/',products_view,name='products')

]