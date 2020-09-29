from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_index, name='post_index'),
    path('posts/<int:post_id>', views.post_show, name='posts_show'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('user/<username>/', views.profile, name='profile'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('posts/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment_create'),
    path('posts/<int:pk>/comment/<int:comment_id>/update', views.CommentUpdate.as_view(), name='comment_update'),
]