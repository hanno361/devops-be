from datetime import datetime

import pytest
from django.urls import reverse
from django.utils import timezone

from apps.blog.models import BlogCategory, BlogPost, BlogTag


@pytest.fixture
def category(db):
    return BlogCategory.objects.create(name="News")


@pytest.fixture
def tag_audio(db):
    return BlogTag.objects.create(name="audio")


@pytest.fixture
def tag_tech(db):
    return BlogTag.objects.create(name="tech")


@pytest.fixture
def april_post(db, category, tag_audio):
    p = BlogPost.objects.create(
        category=category, title="April post",
        excerpt="x", body="x",
        status=BlogPost.PUBLISHED,
        published_at=timezone.make_aware(datetime(2026, 4, 15, 10, 0, 0)),
    )
    p.tags.add(tag_audio)
    return p


@pytest.fixture
def may_post(db, category, tag_tech):
    p = BlogPost.objects.create(
        category=category, title="May post",
        excerpt="x", body="x",
        status=BlogPost.PUBLISHED,
        published_at=timezone.make_aware(datetime(2026, 5, 10, 10, 0, 0)),
    )
    p.tags.add(tag_tech)
    return p


@pytest.mark.django_db
def test_blog_tags_sidebar(api_client, tag_audio, tag_tech):
    response = api_client.get(reverse("blog-tags"))
    assert response.status_code == 200
    slugs = [t["slug"] for t in response.json()]
    assert "audio" in slugs
    assert "tech" in slugs


@pytest.mark.django_db
def test_blog_archive(api_client, april_post, may_post):
    response = api_client.get(reverse("blog-archive"))
    assert response.status_code == 200
    archive = response.json()
    months = [e["month"] for e in archive]
    assert "April 2026" in months
    assert "May 2026" in months


@pytest.mark.django_db
def test_blog_list_filter_by_tag(api_client, april_post, may_post):
    response = api_client.get(reverse("blog-list") + "?tag=audio")
    titles = [p["title"] for p in response.json()["data"]]
    assert "April post" in titles
    assert "May post" not in titles


@pytest.mark.django_db
def test_blog_list_filter_by_year_month(api_client, april_post, may_post):
    response = api_client.get(reverse("blog-list") + "?year=2026&month=4")
    titles = [p["title"] for p in response.json()["data"]]
    assert "April post" in titles
    assert "May post" not in titles
