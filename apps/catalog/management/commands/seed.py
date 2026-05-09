from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.blog.models import BlogCategory, BlogPost, BlogTag
from apps.catalog.models import Brand, Category, Product
from apps.home.models import Banner, BannerFeature, FeaturedProduct, HeroSlide
from apps.pages.models import FAQ, AboutPage, TeamMember

User = get_user_model()


CATEGORIES = [
    ("Eau de Parfum", "Long-lasting parfum collection."),
    ("Eau de Toilette", "Lighter toilette scents for daytime."),
    ("Body Care", "Body sprays, lotions and care products."),
    ("Gift Sets", "Curated gift bundles."),
]

BRANDS = ["Sinp Atelier", "Sinp Noir", "Sinp Aqua"]

PRODUCTS = [
    {
        "name": "Velvet Rose Eau de Parfum 50ml",
        "category": "Eau de Parfum",
        "brand": "Sinp Atelier",
        "short_description": "Romantic rose with a smoky musk base.",
        "description": "A signature scent built on Damask rose, oud and warm amber. "
        "Hand-bottled in Grasse and aged for 90 days for depth.",
        "price": "129.00",
        "sale_price": "99.00",
        "sku": "SNP-EDP-VR50",
        "stock": 25,
        "is_featured": True,
    },
    {
        "name": "Black Vetiver Eau de Parfum 75ml",
        "category": "Eau de Parfum",
        "brand": "Sinp Noir",
        "short_description": "Deep vetiver with leather facets.",
        "description": "Smoked vetiver, Haitian roots and aged leather make this a bold, modern parfum.",
        "price": "159.00",
        "sale_price": None,
        "sku": "SNP-EDP-BV75",
        "stock": 18,
        "is_featured": True,
    },
    {
        "name": "Aqua Citrus Eau de Toilette 100ml",
        "category": "Eau de Toilette",
        "brand": "Sinp Aqua",
        "short_description": "Bright bergamot and sea salt.",
        "description": "A fresh splash of bergamot, mandarin and sea minerals — perfect for sunny days.",
        "price": "79.00",
        "sale_price": "59.00",
        "sku": "SNP-EDT-AC100",
        "stock": 40,
        "is_featured": False,
    },
    {
        "name": "Cedar Smoke EDP 50ml",
        "category": "Eau de Parfum",
        "brand": "Sinp Noir",
        "short_description": "Smoky cedar with warm spice.",
        "description": "Cedarwood smoke layered with cardamom and saffron.",
        "price": "119.00",
        "sale_price": None,
        "sku": "SNP-EDP-CS50",
        "stock": 22,
        "is_featured": False,
    },
    {
        "name": "Body Mist — Lily Garden 200ml",
        "category": "Body Care",
        "brand": "Sinp Atelier",
        "short_description": "Soft daily body mist.",
        "description": "Lily, white tea and sandalwood in a hydrating mist.",
        "price": "29.00",
        "sale_price": None,
        "sku": "SNP-BM-LG200",
        "stock": 60,
        "is_featured": False,
    },
    {
        "name": "Discovery Set — 5x10ml",
        "category": "Gift Sets",
        "brand": "Sinp Atelier",
        "short_description": "Five signature scents in travel sizes.",
        "description": "Discover the Sinp range in 5x10ml refillable atomisers.",
        "price": "69.00",
        "sale_price": "55.00",
        "sku": "SNP-GIFT-DS5",
        "stock": 35,
        "is_featured": True,
    },
    {
        "name": "Amber Oud EDP 100ml",
        "category": "Eau de Parfum",
        "brand": "Sinp Atelier",
        "short_description": "Resinous amber and aged oud.",
        "description": "A statement parfum centred on Cambodian oud, labdanum and benzoin.",
        "price": "189.00",
        "sale_price": None,
        "sku": "SNP-EDP-AO100",
        "stock": 12,
        "is_featured": True,
    },
    {
        "name": "Body Lotion — Velvet Rose 250ml",
        "category": "Body Care",
        "brand": "Sinp Atelier",
        "short_description": "Layer with the Velvet Rose parfum.",
        "description": "Rich shea-butter lotion infused with the Velvet Rose accord.",
        "price": "34.00",
        "sale_price": None,
        "sku": "SNP-BL-VR250",
        "stock": 50,
        "is_featured": False,
    },
    {
        "name": "Gift Set — His & Hers Duo",
        "category": "Gift Sets",
        "brand": "Sinp Atelier",
        "short_description": "Velvet Rose and Black Vetiver paired.",
        "description": "Two of our signature parfums boxed together.",
        "price": "239.00",
        "sale_price": "199.00",
        "sku": "SNP-GIFT-HH",
        "stock": 14,
        "is_featured": True,
    },
    {
        "name": "Aqua Citrus EDT 50ml Travel",
        "category": "Eau de Toilette",
        "brand": "Sinp Aqua",
        "short_description": "Pocket-sized fresh splash.",
        "description": "Travel-sized 50ml of our best-selling Aqua Citrus EDT.",
        "price": "49.00",
        "sale_price": None,
        "sku": "SNP-EDT-AC50",
        "stock": 45,
        "is_featured": False,
    },
]

BLOG_CATEGORIES = ["Notes & Stories", "Behind the Bottle", "Care Guide"]
BLOG_TAGS = ["fragrance", "rose", "oud", "summer", "tutorial"]
BLOG_POSTS = [
    {
        "title": "How to Layer a Signature Scent",
        "category": "Care Guide",
        "tags": ["fragrance", "tutorial"],
        "excerpt": "Three rules for building a layered fragrance wardrobe.",
        "body": "Start with a clean base, build with a complementary mist, and finish with a single spritz of EDP on pulse points...",
    },
    {
        "title": "Inside the Atelier: Distilling Damask Rose",
        "category": "Behind the Bottle",
        "tags": ["rose"],
        "excerpt": "A morning at the distillery in Isparta.",
        "body": "Every spring our team travels to Isparta where Damask rose is harvested before dawn...",
    },
    {
        "title": "Why Oud is the King of Notes",
        "category": "Notes & Stories",
        "tags": ["oud"],
        "excerpt": "From agarwood resin to your bottle.",
        "body": "Oud is the resinous heartwood of the agarwood tree. Its formation is a slow, rare process...",
    },
    {
        "title": "Summer Scent Survival Kit",
        "category": "Care Guide",
        "tags": ["summer", "tutorial"],
        "excerpt": "Light EDTs, body mists and a refreshing trick.",
        "body": "Heat changes how we wear scent. Swap heavy parfums for crisp citrus EDTs...",
    },
    {
        "title": "Notes 101: Top, Heart, Base",
        "category": "Notes & Stories",
        "tags": ["fragrance"],
        "excerpt": "A 3-minute guide to fragrance pyramids.",
        "body": "Top notes evaporate first — citrus, herbs, light spice. Heart notes are the soul of a scent...",
    },
]

FAQS = [
    ("Do you ship internationally?", "Yes, we ship to most countries within 3-7 business days."),
    ("How can I track my order?", "Once shipped, you'll receive a tracking link by email."),
    ("Are samples available?", "Yes, the Discovery Set lets you try five signature scents."),
    ("Can I return a fragrance?", "Unopened bottles can be returned within 14 days for a full refund."),
    ("How should I store my parfum?", "Keep it in a cool, dark place — avoid direct sunlight and heat."),
    ("How long does an EDP last?", "Most Sinp EDPs last 6-10 hours on skin and longer on clothing."),
    ("Are your products cruelty-free?", "Absolutely. Sinp is fully cruelty-free and Leaping-Bunny certified."),
]

ABOUT = {
    "title": "About Sinp",
    "intro": "A small atelier crafting modern parfums with old-world technique.",
    "body": (
        "Sinp was founded in 2019 with a simple promise: build fragrances slowly, age them deeply, "
        "and bottle them honestly. Every Sinp parfum is hand-batched in Grasse, France, and aged for "
        "a minimum of 90 days before it reaches you. We work directly with growers across Bulgaria, "
        "Türkiye and Madagascar to source rose, citrus and vanilla at peak quality."
    ),
}

TEAM = [
    ("Aylin Demir", "Master Perfumer", "Trained in Grasse, leads the Sinp atelier."),
    ("Marco Russo", "Lead Distiller", "Manages our small-batch distillation process."),
    ("Sara Lin", "Head of Experience", "Designs every Sinp customer touchpoint."),
]


HERO_SLIDES = [
    {
        "bg": "/images/slide1.webp",
        "eyebrow": "New collection",
        "title": "Discover the",
        "title_span": "Velvet Rose",
        "body": "Hand-batched in Grasse, aged ninety days for depth.",
        "cta_label": "Shop now",
        "cta_href": "/shop",
    },
    {
        "bg": "/images/slide2.webp",
        "eyebrow": "Limited edition",
        "title": "Black",
        "title_span": "Vetiver",
        "body": "Smoked vetiver and aged leather — a bold statement.",
        "cta_label": "Explore",
        "cta_href": "/product/black-vetiver-eau-de-parfum-75ml",
    },
]

FEATURED = [
    {
        "eyebrow": "Best seller",
        "title": "Velvet Rose Eau de Parfum",
        "description": "Romantic Damask rose grounded by smoky musk.",
        "image_src": "/images/product1_3.webp",
        "image_alt": "Velvet Rose bottle",
        "cta_href": "/product/velvet-rose-eau-de-parfum-50ml",
        "image_right": False,
    },
    {
        "eyebrow": "New",
        "title": "Aqua Citrus Eau de Toilette",
        "description": "A bright splash of bergamot and sea salt.",
        "image_src": "/images/product2_3.webp",
        "image_alt": "Aqua Citrus bottle",
        "cta_href": "/product/aqua-citrus-eau-de-toilette-100ml",
        "image_right": True,
    },
]

BANNER = {
    "eyebrow": "Atelier story",
    "title": "Slow-batched parfums, honest ingredients.",
    "background_image": "/images/bg.webp",
    "cta_label": "About Sinp",
    "cta_href": "/about",
    "features": [
        {"icon": "leaf", "label": "Cruelty-free"},
        {"icon": "globe", "label": "Worldwide shipping"},
        {"icon": "shield", "label": "90-day aged"},
    ],
}


class Command(BaseCommand):
    help = "Seed the database with demo catalog, blog and pages content."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Delete existing demo data first.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["reset"]:
            self.stdout.write("Resetting demo data...")
            Product.objects.all().delete()
            Brand.objects.all().delete()
            Category.objects.all().delete()
            BlogPost.objects.all().delete()
            BlogTag.objects.all().delete()
            BlogCategory.objects.all().delete()
            FAQ.objects.all().delete()
            TeamMember.objects.all().delete()
            AboutPage.objects.all().delete()
            BannerFeature.objects.all().delete()
            Banner.objects.all().delete()
            FeaturedProduct.objects.all().delete()
            HeroSlide.objects.all().delete()

        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                email="admin@sinp.local",
                username="admin",
                password="admin12345",
            )
            self.stdout.write(self.style.SUCCESS("Created superuser admin@sinp.local / admin12345"))

        for name, desc in CATEGORIES:
            Category.objects.get_or_create(name=name, defaults={"description": desc})

        for name in BRANDS:
            Brand.objects.get_or_create(name=name)

        for data in PRODUCTS:
            Product.objects.get_or_create(
                sku=data["sku"],
                defaults={
                    "name": data["name"],
                    "category": Category.objects.get(name=data["category"]),
                    "brand": Brand.objects.get(name=data["brand"]),
                    "short_description": data["short_description"],
                    "description": data["description"],
                    "price": Decimal(data["price"]),
                    "sale_price": Decimal(data["sale_price"]) if data["sale_price"] else None,
                    "stock": data["stock"],
                    "is_featured": data["is_featured"],
                },
            )

        for name in BLOG_CATEGORIES:
            BlogCategory.objects.get_or_create(name=name)
        for name in BLOG_TAGS:
            BlogTag.objects.get_or_create(name=name)

        author = User.objects.filter(is_superuser=True).first()
        for idx, data in enumerate(BLOG_POSTS):
            post, created = BlogPost.objects.get_or_create(
                title=data["title"],
                defaults={
                    "category": BlogCategory.objects.get(name=data["category"]),
                    "author": author,
                    "excerpt": data["excerpt"],
                    "body": data["body"],
                    "status": BlogPost.PUBLISHED,
                    "published_at": timezone.now() - timedelta(days=idx * 3),
                },
            )
            if created:
                post.tags.set(BlogTag.objects.filter(name__in=data["tags"]))

        for idx, (q, a) in enumerate(FAQS):
            FAQ.objects.get_or_create(question=q, defaults={"answer": a, "order": idx})

        AboutPage.objects.get_or_create(
            id=1,
            defaults={"title": ABOUT["title"], "intro": ABOUT["intro"], "body": ABOUT["body"]},
        )

        for idx, (name, role, bio) in enumerate(TEAM):
            TeamMember.objects.get_or_create(
                name=name, defaults={"role": role, "bio": bio, "order": idx}
            )

        for idx, data in enumerate(HERO_SLIDES):
            HeroSlide.objects.get_or_create(
                title=data["title"],
                defaults={**data, "order": idx},
            )

        for idx, data in enumerate(FEATURED):
            FeaturedProduct.objects.get_or_create(
                title=data["title"],
                defaults={**data, "order": idx},
            )

        banner, _ = Banner.objects.get_or_create(
            id=1,
            defaults={
                "eyebrow": BANNER["eyebrow"],
                "title": BANNER["title"],
                "background_image": BANNER["background_image"],
                "cta_label": BANNER["cta_label"],
                "cta_href": BANNER["cta_href"],
            },
        )
        if not banner.features.exists():
            for idx, feat in enumerate(BANNER["features"]):
                BannerFeature.objects.create(
                    banner=banner, icon=feat["icon"], label=feat["label"], order=idx
                )

        self.stdout.write(self.style.SUCCESS("Seed complete."))
