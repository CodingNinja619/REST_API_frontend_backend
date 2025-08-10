from django.urls import path, include

from .views import BookView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookView)

app_name = "myapp"

urlpatterns = [
    path('', include(router.urls))
]