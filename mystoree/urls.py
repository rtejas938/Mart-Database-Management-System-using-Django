from django.contrib import admin
from django.urls import path
from .import views

app_name ='mystoree'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('profile/',views.profile,name='profile'),
    path('imported/',views.imported,name='imported'),
    path('business/',views.business,name='business'),
    path('customer/',views.customer,name='customer'),
    path('addcustomer/',views.addcustomer,name='addcustomer'),
    path('details/<int:id>/',views.details ,name='details'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name ='delete'),

]