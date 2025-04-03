from .views import ArticleView 
from django.urls import path
 
 
app_name = "articles" 
 
# app_name will help us do a reverse look-up latter. 
urlpatterns = [ 
  path('articles/', ArticleView.as_view()), 
  path('articles/<int:pk>', ArticleView.as_view())
] 
