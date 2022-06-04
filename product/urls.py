from django.urls import path

from product.models import ProductCategory
from .views import ProductCategoryViewSet, ProductViewSet

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
    path(
        "product/search/",
        ProductViewSet.as_view({"get":"search_products"}),
        name="product_search_view"
    ),
    path(
        "product-category/",
        ProductCategoryViewSet.as_view({"get":"list","post":"create"}),
        name="product_category_view"
    )
]
