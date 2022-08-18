from django.urls import path

from ads.views import (AdListView, AdDetailView, AdUpdateView, AdImageView, AdDeleteView, AdCreateView,
                       CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryCreateView,
                       index,
                       UserListView, UserDetailView, UserUpdateView, UserDeleteView, UserCreateView)

urlpatterns = [
    path('', index),
    path('ad/', AdListView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/upload_image/', AdImageView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('user/', UserListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', UserDeleteView.as_view()),
    path('user/create/', UserCreateView.as_view()),
]
