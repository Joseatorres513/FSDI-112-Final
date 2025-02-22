from django.urls import path
from posts import views


urlpatterns = [
    path("<int:pk>/new/", views.PostCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete"),
    path("<int:pk>/list/", views.PostListView.as_view(), name="post_list"),
]