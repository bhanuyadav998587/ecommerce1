from django.urls import path,include
from ecomm.views import  index,detail,cart_view, intermediate,register,loginpage,logoutpage
app_name = 'ecomm'
urlpatterns = [
    
    path('', index, name= 'index'),
    path('login/', loginpage, name="login"),
    path('register/', register, name="register"),
    path('logoutpage/', logoutpage, name="logoutpage"),
    path('detail/<int:product_id>/<slug:slug>', detail, name= 'detail'),
    path('cart/',cart_view, name = 'cart'),
    path('intermediate/', intermediate, name="intermediate"),
       
]