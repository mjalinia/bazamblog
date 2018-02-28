from django.urls import path
from . import views
urlpatterns = [
   path('', views.BlogListView.as_view(),name="home",),
   path('post/<int:pk>/detail', views.BlogDetailVIew.as_view(),name="detail",), 
   path('post/<int:pk>/delete', views.BlogDeleteView.as_view(),name="delete",), 
   path('post/create', views.BlogCreateView.as_view(),name="create",),
   path('post/<int:pk>/edit', views.BlogUpdateView.as_view(),name="edit",),

]
