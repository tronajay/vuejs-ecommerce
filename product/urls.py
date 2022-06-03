from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path(
        "product/",
        ProductViewSet.as_view({"get":"get","post":"create"}),
        name="product_view_set"
    ),
        path(
        "product/<uuid:product_uuid>/",
        ProductViewSet.as_view({"get":"get_product","patch":"update"}),
        name="product_detail_view_set"
    ),
    path(
        "product/<str:slug>/view/",
        ProductViewSet.as_view({"get":"product_detail"}),
        name="product_detail_view"
    ),
]
