from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from . import views


urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
    path('blog_api-auth/', include('rest_framework.urls')),
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>', views.CommentDetail.as_view()),
    path('categories/', views.CategoriesList.as_view()),
    path('categories/<int:pk>', views.CategoriesDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
