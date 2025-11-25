from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.assignments.views import AssignmentViewSet

router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet, basename='assignments')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
    path("assignments/", include("apps.assignments.urls")),
    path('api/submissions/', include('apps.assignments.urls')),
    path('api/', include('apps.assignments.urls')),
]


from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('apps.assignments.urls')),
    path('api-auth/', include('rest_framework.urls')),  
    path('api-token-auth/', drf_views.obtain_auth_token),  
]

