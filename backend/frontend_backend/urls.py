from django.urls import path, include
# from rest_framework import routers
from django.contrib import admin

from book.views import BookView

# router = routers.DefaultRouter()
# router.register(r'books', BookView)

urlpatterns = [
    # path('', include(router.urls)),
    path('', include('book.urls')),
    path('admin/', admin.site.urls),
]

# for url in router.urls:
#     print(url)