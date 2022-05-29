from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path(
        "product/",
        ProductViewSet.as_view({"get":"get","post":"create"}),
        name="product_view_set"
    ),
        path(
        "product/<int:pk>/",
        ProductViewSet.as_view({"get":"get_product","patch":"update"}),
        name="product_detail_view_set"
    )
]
