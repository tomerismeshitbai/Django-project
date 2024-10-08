from django.urls import path 
from .views import Home, PostDetail, AddPost , EditPost , DeletePost , AddComment 

urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('post/<int:pk>', PostDetail.as_view(), name = "post-detail"),
    path('add_post/', AddPost.as_view(), name = "add-post"),
    path('post/edit/<int:pk>', EditPost.as_view(), name = "edit-post"),
    path('post/delete/<int:pk>', DeletePost.as_view(), name = "delete-post"),
    path('post/<int:pk>/comment/', AddComment.as_view(), name="add_comment"),
]