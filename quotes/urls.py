from django.urls import path
from quotes import views
app_name='quotes'

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('add_stock',views.add_stock, name='add_stock'),
    path('delete/',views.delete, name='delete'),
    path('delete_stock/<pk>/',views.del_stock.as_view(), name='del_stock'),

    
]