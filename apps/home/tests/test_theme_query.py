import pytest
from django.urls import reverse

from apps.catalog.models import Theme
from apps.home.models import Banner, BannerFeature, FeaturedProduct, HeroSlide


@pytest.fixture
def airpod(db):
    return Theme.objects.create(name="Airpod", slug="airpod")


@pytest.fixture
def drone(db):
    return Theme.objects.create(name="Drone", slug="drone")


@pytest.fixture
def airpod_hero(db, airpod):
    return HeroSlide.objects.create(
        theme=airpod, title="Airpod Hero", bg="/images/a.webp",
    )


@pytest.fixture
def drone_hero(db, drone):
    return HeroSlide.objects.create(
        theme=drone, title="Drone Hero", bg="/images/d.webp",
    )


@pytest.fixture
def airpod_banner(db, airpod):
    return Banner.objects.create(
        theme=airpod, title="Airpod banner", background_image="/images/bg.webp",
    )


@pytest.fixture
def drone_banner(db, drone):
    return Banner.objects.create(
        theme=drone, title="Drone banner", background_image="/images/bg.webp",
    )


@pytest.mark.django_db
def test_hero_slides_filtered_by_theme(api_client, airpod_hero, drone_hero):
    response = api_client.get(reverse("home-hero-slides") + "?theme=airpod")
    titles = [s["title"] for s in response.json()["data"]]
    assert "Airpod Hero" in titles
    assert "Drone Hero" not in titles


@pytest.mark.django_db
def test_hero_slides_default_theme_airpod(api_client, airpod_hero, drone_hero):
    response = api_client.get(reverse("home-hero-slides"))
    titles = [s["title"] for s in response.json()["data"]]
    assert "Airpod Hero" in titles
    assert "Drone Hero" not in titles


@pytest.mark.django_db
def test_banner_filtered_by_theme(api_client, airpod_banner, drone_banner):
    response = api_client.get(reverse("home-banner") + "?theme=drone")
    assert response.status_code == 200
    assert response.json()["data"]["title"] == "Drone banner"


@pytest.mark.django_db
def test_banner_not_found_for_unknown_theme(api_client):
    response = api_client.get(reverse("home-banner") + "?theme=unknown")
    assert response.status_code == 404
