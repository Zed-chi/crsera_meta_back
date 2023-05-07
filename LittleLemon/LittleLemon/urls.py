from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

""" urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] """
""" urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
] """

urlpatterns = [
    path("admin/", admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
