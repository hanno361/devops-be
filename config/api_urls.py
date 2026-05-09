from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.accounts.views import LoginView, MeView, RegisterView
from apps.blog.views import BlogPostDetailView, BlogPostListView
from apps.catalog.views import ProductDetailView, ProductListView
from apps.orders.views import OrderDetailView, OrderListCreateView
from apps.home.views import (
    BannerView,
    FeaturedProductListView,
    HeroSlideListView,
    HomeBlogView,
    HomeProductsView,
)
from apps.pages.views import AboutPageView, ContactMessageCreateView, FAQListView

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    # Auth (FE: POST /auth/login, /auth/register; GET /auth/me)
    path("auth/login", LoginView.as_view(), name="login"),
    path("auth/register", RegisterView.as_view(), name="register"),
    path("auth/me", MeView.as_view(), name="me"),

    # Catalog
    path("products", ProductListView.as_view(), name="product-list"),
    path("products/<slug:slug>", ProductDetailView.as_view(), name="product-detail"),

    # Blog
    path("blog", BlogPostListView.as_view(), name="blog-list"),
    path("blog/<slug:slug>", BlogPostDetailView.as_view(), name="blog-detail"),

    # Pages
    path("faq", FAQListView.as_view(), name="faq-list"),
    path("about", AboutPageView.as_view(), name="about"),
    path("contact", ContactMessageCreateView.as_view(), name="contact-create"),

    # Home content
    path("home/hero-slides", HeroSlideListView.as_view(), name="home-hero-slides"),
    path("home/featured-products", FeaturedProductListView.as_view(), name="home-featured-products"),
    path("home/banner", BannerView.as_view(), name="home-banner"),
    path("home/products", HomeProductsView.as_view(), name="home-products"),
    path("home/blog", HomeBlogView.as_view(), name="home-blog"),

    # Orders
    path("orders", OrderListCreateView.as_view(), name="orders"),
    path("orders/<str:number>", OrderDetailView.as_view(), name="order-detail"),

    # Internal (not consumed by FE; kept available)
    path("cart/", include("apps.cart.urls")),
    path("wishlist/", include("apps.wishlist.urls")),
]
