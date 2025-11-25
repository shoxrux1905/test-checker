from django.urls import path

from apps.users.api_endpoints.user import UserRegisterView, UserUpdateView, UserUpdatePasswordView
from apps.users.api_endpoints.study_group import StudyGroupListCreateView, StudyGroupRetrieveUpdateView


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("update/", UserUpdateView.as_view(), name="user-update"),
    path("update-password/", UserUpdatePasswordView.as_view(), name="user-update-password"),
    path("groups/", StudyGroupListCreateView.as_view(), name="group-list-create"),
    path("groups/<int:pk>/", StudyGroupRetrieveUpdateView.as_view(), name="group-retrieve-update"),
]
