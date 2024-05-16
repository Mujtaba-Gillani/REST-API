from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    # path("", views.post_list, name="list_posts"),
    path("", views.ListPostView.as_view(), name="list_posts"),
    path("<int:post_id>/", views.PostRetrieveUpdateDeleteView.as_view(), name="details_posts")
    # path("update/<int:post_id>/", views.update_post, name="update_post"),
    # path("delete/<int:post_id>/", views.delete_post, name="delete_post")
    # # Add more URL patterns as needed
]
