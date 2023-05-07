from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from LittleLemonAPI import views

""" router = routers.DefaultRouter()
router.register(r'menuitems', views.menuViewSet) """

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
    path("api/", include("LittleLemonAPI.urls")),
    path("restaurant/", include("restaurant.urls")),
]
