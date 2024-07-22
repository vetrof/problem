from django.urls import path

from app_api.views import AllProductView

urlpatterns = [
    path('all_products/', AllProductView.as_view())
]
