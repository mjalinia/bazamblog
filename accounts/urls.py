from django.urls import path
from . import views
urlpatterns = [
   path('usersignup', views.BlogUserCreate.as_view(),name="signup",), 

]
