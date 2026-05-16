from decimal import Decimal

import pytest
from django.urls import reverse

from apps.catalog.models import (
    Category,
    Color,
    Product,
    Size,
    Tag,
    Theme,
    Vendor,
)


@pytest.fixture
def airpod_theme(db):
    return Theme.objects.create(name="Airpod", slug="airpod")


@pytest.fixture
def smartwatch_theme(db):
    return Theme.objects.create(name="Smartwatch", slug="smartwatch")


@pytest.fixture
def cat_earbud(db, airpod_theme):
    return Category.objects.create(name="Earbud", slug="airpod-earbud", theme=airpod_theme)


@pytest.fixture
def cat_watch(db, smartwatch_theme):
    return Category.objects.create(name="Smartwatch", slug="smartwatch-smartwatch", theme=smartwatch_theme)


@pytest.fixture
def black(db):
    return Color.objects.create(name="Black", value="black", hex="#000000")


@pytest.fixture
def tag_new(db):
    return Tag.objects.create(name="New")


@pytest.fixture
def apple(db):
    return Vendor.objects.create(name="Apple")


@pytest.fixture
def airpod_product(db, airpod_theme, cat_earbud, black, tag_new, apple):
    p = Product.objects.create(
        theme=airpod_theme, category=cat_earbud, vendor=apple,
        name="Airpod test", sku="AP-1", price=Decimal("100"), stock=10,
    )
    p.colors.add(black)
    p.tags.add(tag_new)
    return p


@pytest.fixture
def watch_product(db, smartwatch_theme, cat_watch):
    return Product.objects.create(
        theme=smartwatch_theme, category=cat_watch,
        name="Watch test", sku="W-1", price=Decimal("200"), stock=5,
    )


@pytest.mark.django_db
def test_categories_sidebar_lists_all(api_client, cat_earbud, cat_watch):
    response = api_client.get(reverse("product-categories"))
    assert response.status_code == 200
    slugs = [c["slug"] for c in response.json()]
    assert "airpod-earbud" in slugs
    assert "smartwatch-smartwatch" in slugs


@pytest.mark.django_db
def test_categories_sidebar_filtered_by_theme(api_client, cat_earbud, cat_watch):
    response = api_client.get(reverse("product-categories") + "?theme=airpod")
    assert response.status_code == 200
    slugs = [c["slug"] for c in response.json()]
    assert "airpod-earbud" in slugs
    assert "smartwatch-smartwatch" not in slugs


@pytest.mark.django_db
def test_colors_sidebar(api_client, airpod_product, black):
    response = api_client.get(reverse("product-colors"))
    assert response.status_code == 200
    values = [c["value"] for c in response.json()]
    assert "black" in values


@pytest.mark.django_db
def test_tags_sidebar(api_client, airpod_product, tag_new):
    response = api_client.get(reverse("product-tags"))
    assert response.status_code == 200
    slugs = [t["slug"] for t in response.json()]
    assert "new" in slugs


@pytest.mark.django_db
def test_vendors_sidebar(api_client, airpod_product, apple):
    response = api_client.get(reverse("product-vendors"))
    assert response.status_code == 200
    slugs = [v["slug"] for v in response.json()]
    assert "apple" in slugs


@pytest.mark.django_db
def test_product_list_filters_by_theme(api_client, airpod_product, watch_product):
    response = api_client.get(reverse("product-list") + "?theme=airpod")
    assert response.status_code == 200
    skus = [p["slug"] for p in response.json()["data"]]
    assert "airpod-test" in skus
    assert "watch-test" not in skus


@pytest.mark.django_db
def test_product_list_filters_by_color(api_client, airpod_product, watch_product):
    response = api_client.get(reverse("product-list") + "?color=black")
    assert response.status_code == 200
    skus = [p["slug"] for p in response.json()["data"]]
    assert "airpod-test" in skus
    assert "watch-test" not in skus
