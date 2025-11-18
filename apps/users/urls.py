from django.urls import path
from .views import (
    UserRegisterView, UserLoginView, UserUpdateView,UserUpdatePasswordView,
    StudyGroupCreateView,StudyGroupListView,StudyGroupUpdateView,
    StudyGroupDetailView,
    StudyGroupArchiveView,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("update/", UserUpdateView.as_view(), name="user-update"),
    path("update-password/", UserUpdatePasswordView.as_view(), name="user-update-password"),
    path("groups/", StudyGroupCreateView.as_view(), name="group-create"),
    path("groups/list/", StudyGroupListView.as_view(), name="group-list"),
    path("groups/<int:pk>/", StudyGroupDetailView.as_view(), name="group-detail"),
    path("groups/<int:pk>/update/", StudyGroupUpdateView.as_view(), name="group-update"),
    path("groups/<int:pk>/archive/", StudyGroupArchiveView.as_view(), name="group-archive"),
]
