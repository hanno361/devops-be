"""Seed the database with FE-aligned demo data.

The Sinp template ships with four homepage themes — airpod, smartwatch, drone
and backpack. Every theme gets its own products, hero slides, featured cards
and banner so each `/api/home/*` endpoint can be filtered by `?theme=`.
"""
from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.blog.models import BlogCategory, BlogPost, BlogTag
from apps.catalog.models import (
    Brand,
    Category,
    Color,
    Product,
    Size,
    Tag,
    Theme,
    Vendor,
)
from apps.home.models import Banner, BannerFeature, FeaturedProduct, HeroSlide
from apps.pages.models import FAQ, AboutPage, TeamMember

User = get_user_model()


# ─── Theme → category map ────────────────────────────────────────────────

THEMES = [
    {
        "slug": "airpod",
        "name": "Airpod",
        "categories": ["Headphone", "Earbud", "Speaker", "Accessories"],
    },
    {
        "slug": "smartwatch",
        "name": "Smartwatch",
        "categories": ["Smartwatch", "Fitness Band", "Strap", "Accessories"],
    },
    {
        "slug": "drone",
        "name": "Drone",
        "categories": ["Drone", "Camera", "Battery", "Accessories"],
    },
    {
        "slug": "backpack",
        "name": "Backpack",
        "categories": ["Travel Bag", "Daypack", "Laptop Bag", "Accessories"],
    },
]

VENDORS = ["Apple", "Samsung", "Sony", "DJI", "Bose", "Herschel", "Garmin", "Anker"]

COLORS = [
    {"name": "Black", "value": "black", "hex": "#000000"},
    {"name": "White", "value": "white", "hex": "#ffffff"},
    {"name": "Blue", "value": "blue", "hex": "#3b82f6"},
    {"name": "Orange", "value": "orange", "hex": "#fc6539"},
    {"name": "Gray", "value": "gray", "hex": "#6b7280"},
    {"name": "Red", "value": "red", "hex": "#ef4444"},
    {"name": "Green", "value": "green", "hex": "#10b981"},
]

TAGS = ["New", "Sale", "Tech", "Audio", "Travel", "Featured", "Limited"]

SIZES = ["Small", "Medium", "Large"]


# ─── Products per theme ──────────────────────────────────────────────────

PRODUCTS = [
    # airpod (6)
    {"name": "Airpod product ides", "theme": "airpod", "category": "Earbud",
     "vendor": "Apple", "colors": ["white", "black"], "tags": ["Sale", "Audio"],
     "price": "130.00", "sale_price": "110.00", "sku": "AIRPOD-IDES",
     "stock": 12, "is_featured": True, "image": "/images/product1.webp",
     "description": "Wireless earbuds with active noise cancellation and adaptive audio."},
    {"name": "Airpod product kiebd", "theme": "airpod", "category": "Earbud",
     "vendor": "Sony", "colors": ["white"], "tags": ["New", "Audio"],
     "price": "150.00", "sale_price": None, "sku": "AIRPOD-KIEBD",
     "stock": 18, "is_featured": True, "image": "/images/product2.webp",
     "description": "Studio-grade earbuds tuned by Grammy-winning engineers."},
    {"name": "Studio Headphone Pro", "theme": "airpod", "category": "Headphone",
     "vendor": "Bose", "colors": ["black", "gray"], "tags": ["Tech", "Audio"],
     "price": "299.00", "sale_price": "249.00", "sku": "AIRPOD-HPRO",
     "stock": 8, "is_featured": True, "image": "/images/product3.webp",
     "description": "Reference-class over-ear headphones with leather earcups."},
    {"name": "Compact Bluetooth Speaker", "theme": "airpod", "category": "Speaker",
     "vendor": "Anker", "colors": ["blue", "orange"], "tags": ["Travel", "Audio"],
     "price": "79.00", "sale_price": None, "sku": "AIRPOD-SPK1",
     "stock": 30, "is_featured": False, "image": "/images/product4.webp",
     "description": "Pocket-sized speaker with 16-hour playback and IPX7 water resistance."},
    {"name": "Charging Case Premium", "theme": "airpod", "category": "Accessories",
     "vendor": "Apple", "colors": ["white", "black"], "tags": ["Featured"],
     "price": "49.00", "sale_price": "39.00", "sku": "AIRPOD-CASE",
     "stock": 45, "is_featured": False, "image": "/images/product5.webp",
     "description": "MagSafe charging case for airpod variants."},
    {"name": "Travel Earbud Bundle", "theme": "airpod", "category": "Earbud",
     "vendor": "Sony", "colors": ["black"], "tags": ["Sale", "Travel"],
     "price": "189.00", "sale_price": "159.00", "sku": "AIRPOD-BUNDLE",
     "stock": 14, "is_featured": True, "image": "/images/product1.webp",
     "description": "Travel pouch + earbuds + spare tips bundle."},

    # smartwatch (5)
    {"name": "Smartwatch Series X", "theme": "smartwatch", "category": "Smartwatch",
     "vendor": "Apple", "colors": ["black", "red"], "tags": ["New", "Tech"],
     "price": "399.00", "sale_price": None, "sku": "SW-SERIES-X",
     "stock": 10, "is_featured": True, "image": "/images/product2.webp",
     "description": "AMOLED always-on display, ECG, blood oxygen sensor."},
    {"name": "Smartwatch Fit Plus", "theme": "smartwatch", "category": "Smartwatch",
     "vendor": "Samsung", "colors": ["black", "blue"], "tags": ["Sale", "Tech"],
     "price": "299.00", "sale_price": "249.00", "sku": "SW-FITPLUS",
     "stock": 16, "is_featured": True, "image": "/images/product3.webp",
     "description": "Fitness-first smartwatch with 50m water resistance."},
    {"name": "Fitness Band Lite", "theme": "smartwatch", "category": "Fitness Band",
     "vendor": "Garmin", "colors": ["black", "green"], "tags": ["New"],
     "price": "129.00", "sale_price": None, "sku": "SW-FITBAND",
     "stock": 22, "is_featured": True, "image": "/images/product4.webp",
     "description": "Lightweight band with heart-rate, sleep and stress tracking."},
    {"name": "Leather Watch Strap", "theme": "smartwatch", "category": "Strap",
     "vendor": "Herschel", "colors": ["black", "gray"], "tags": ["Featured"],
     "price": "59.00", "sale_price": "49.00", "sku": "SW-STRAP-LEATHER",
     "stock": 28, "is_featured": False, "image": "/images/product5.webp",
     "description": "Premium leather strap with quick-release pins."},
    {"name": "Sport Strap Bundle", "theme": "smartwatch", "category": "Strap",
     "vendor": "Apple", "colors": ["blue", "orange", "white"], "tags": ["Sale"],
     "price": "79.00", "sale_price": None, "sku": "SW-STRAP-SPORT",
     "stock": 35, "is_featured": False, "image": "/images/product1.webp",
     "description": "Three sport bands in popular colors."},

    # drone (5)
    {"name": "Drone Pro Quadcopter", "theme": "drone", "category": "Drone",
     "vendor": "DJI", "colors": ["gray", "black"], "tags": ["New", "Tech"],
     "price": "899.00", "sale_price": None, "sku": "DRONE-PRO-QUAD",
     "stock": 6, "is_featured": True, "image": "/images/product3.webp",
     "description": "4K HDR camera, 35-min flight time, omnidirectional obstacle sensing."},
    {"name": "Drone Mini Folding", "theme": "drone", "category": "Drone",
     "vendor": "DJI", "colors": ["white", "gray"], "tags": ["Sale", "Travel"],
     "price": "499.00", "sale_price": "439.00", "sku": "DRONE-MINI-FOLD",
     "stock": 9, "is_featured": True, "image": "/images/product4.webp",
     "description": "249-gram folding drone, perfect for travel."},
    {"name": "4K Action Camera", "theme": "drone", "category": "Camera",
     "vendor": "Sony", "colors": ["black"], "tags": ["Tech"],
     "price": "349.00", "sale_price": None, "sku": "DRONE-CAM-4K",
     "stock": 12, "is_featured": False, "image": "/images/product2.webp",
     "description": "120fps 4K action camera mount-compatible with drone bodies."},
    {"name": "Extra Battery Pack", "theme": "drone", "category": "Battery",
     "vendor": "DJI", "colors": ["black"], "tags": ["Featured"],
     "price": "129.00", "sale_price": "99.00", "sku": "DRONE-BATTERY-2X",
     "stock": 20, "is_featured": False, "image": "/images/product1.webp",
     "description": "Two intelligent flight batteries with USB-C fast charging."},
    {"name": "Propeller Guard Set", "theme": "drone", "category": "Accessories",
     "vendor": "Anker", "colors": ["white"], "tags": ["New"],
     "price": "39.00", "sale_price": None, "sku": "DRONE-GUARD",
     "stock": 50, "is_featured": False, "image": "/images/product5.webp",
     "description": "Snap-on propeller guards for indoor flight safety."},

    # backpack (5)
    {"name": "Travel Backpack 30L", "theme": "backpack", "category": "Travel Bag",
     "vendor": "Herschel", "colors": ["black", "gray"], "sizes": ["Medium"],
     "tags": ["Travel", "Featured"], "price": "139.00", "sale_price": "119.00",
     "sku": "BAG-TRAVEL-30", "stock": 18, "is_featured": True,
     "image": "/images/product4.webp",
     "description": "30L travel backpack with separate laptop sleeve and TSA-friendly opening."},
    {"name": "Daypack Classic", "theme": "backpack", "category": "Daypack",
     "vendor": "Herschel", "colors": ["blue", "red", "black"], "sizes": ["Small", "Medium"],
     "tags": ["New"], "price": "89.00", "sale_price": None,
     "sku": "BAG-DAYPACK", "stock": 24, "is_featured": True,
     "image": "/images/product5.webp",
     "description": "The classic Herschel-style daypack with leather straps."},
    {"name": "Laptop Bag 15 inch", "theme": "backpack", "category": "Laptop Bag",
     "vendor": "Anker", "colors": ["black", "gray"], "sizes": ["Medium"],
     "tags": ["Tech"], "price": "99.00", "sale_price": "79.00",
     "sku": "BAG-LAPTOP-15", "stock": 30, "is_featured": True,
     "image": "/images/product1.webp",
     "description": "Padded laptop bag with anti-theft RFID pocket."},
    {"name": "Hiking Backpack 60L", "theme": "backpack", "category": "Travel Bag",
     "vendor": "Herschel", "colors": ["green", "orange"], "sizes": ["Large"],
     "tags": ["Travel", "Sale"], "price": "249.00", "sale_price": "199.00",
     "sku": "BAG-HIKE-60", "stock": 7, "is_featured": False,
     "image": "/images/product2.webp",
     "description": "Multi-day hiking pack with hip belt and rain cover."},
    {"name": "Mini Crossbody Bag", "theme": "backpack", "category": "Accessories",
     "vendor": "Herschel", "colors": ["black", "white", "blue"], "sizes": ["Small"],
     "tags": ["New"], "price": "49.00", "sale_price": None,
     "sku": "BAG-CROSSBODY", "stock": 40, "is_featured": False,
     "image": "/images/product3.webp",
     "description": "Compact crossbody bag for daily essentials."},
]


# ─── Hero slides per theme ──────────────────────────────────────────────

HERO_SLIDES_BY_THEME = {
    "airpod": [
        {"bg": "/images/slide1.webp",
         "eyebrow": "#Feel The Rhythm.", "title": "Walk Up Your Passion",
         "title_span": "Listen Good Music.",
         "body": "Experience the decibels like your ears deserve to.",
         "cta_label": "Explore More", "cta_href": "/shop?theme=airpod"},
        {"bg": "/images/slide2.webp",
         "eyebrow": "Feel The Rhythm.", "title": "Spark Up Your Passion",
         "title_span": "With Good Music.",
         "body": "Safe for the ears, very for the heart.",
         "cta_label": "Explore More", "cta_href": "/shop?theme=airpod"},
    ],
    "smartwatch": [
        {"bg": "/images/slide1.webp",
         "eyebrow": "#Track Your Day.", "title": "Health On Your",
         "title_span": "Wrist.",
         "body": "From the gym to the boardroom — track every move.",
         "cta_label": "Shop Watches", "cta_href": "/shop?theme=smartwatch"},
        {"bg": "/images/slide2.webp",
         "eyebrow": "Stay Connected.", "title": "Smart Notifications,",
         "title_span": "Quiet Battery.",
         "body": "Up to 7 days of battery on a single charge.",
         "cta_label": "Discover", "cta_href": "/shop?theme=smartwatch"},
    ],
    "drone": [
        {"bg": "/images/slide1.webp",
         "eyebrow": "#Take Flight.", "title": "See The World",
         "title_span": "From Above.",
         "body": "4K HDR aerial photography in the palm of your hand.",
         "cta_label": "Shop Drones", "cta_href": "/shop?theme=drone"},
        {"bg": "/images/slide2.webp",
         "eyebrow": "Travel-ready.", "title": "Fold, Fly,",
         "title_span": "Capture.",
         "body": "Sub-250g body — no flight registration needed.",
         "cta_label": "Discover", "cta_href": "/shop?theme=drone"},
    ],
    "backpack": [
        {"bg": "/images/slide1.webp",
         "eyebrow": "#Carry It Well.", "title": "Built For",
         "title_span": "Your Journey.",
         "body": "Travel and laptop bags engineered to last decades.",
         "cta_label": "Shop Bags", "cta_href": "/shop?theme=backpack"},
        {"bg": "/images/slide2.webp",
         "eyebrow": "Everyday Carry.", "title": "Daypack",
         "title_span": "Reimagined.",
         "body": "From commute to weekend trips with one bag.",
         "cta_label": "Explore", "cta_href": "/shop?theme=backpack"},
    ],
}


# ─── Featured products per theme ────────────────────────────────────────

FEATURED_BY_THEME = {
    "airpod": [
        {"eyebrow": "FEATURED PRODUCT", "title": "Minimal Headphone\nFor Music Lover",
         "description": "When an unknown printer took a galley of type and scrambled it to make a type specimen book.",
         "image_src": "/images/product1.webp", "image_alt": "Featured headphone",
         "cta_href": "/product/airpod-product-ides", "image_right": False},
        {"eyebrow": "MINIMAL PRODUCT", "title": "Studio Grade\nReference Sound",
         "description": "Tuned for honest mids and detailed highs.",
         "image_src": "/images/product3.webp", "image_alt": "Studio headphone",
         "cta_href": "/product/studio-headphone-pro", "image_right": True},
    ],
    "smartwatch": [
        {"eyebrow": "FEATURED WATCH", "title": "Always-On AMOLED\nDisplay",
         "description": "Stunning screen that adapts to your environment.",
         "image_src": "/images/product2.webp", "image_alt": "Smartwatch",
         "cta_href": "/product/smartwatch-series-x", "image_right": False},
        {"eyebrow": "FITNESS FIRST", "title": "Track Every\nHeartbeat",
         "description": "24/7 heart rate, blood oxygen, sleep and stress.",
         "image_src": "/images/product3.webp", "image_alt": "Fitness smartwatch",
         "cta_href": "/product/smartwatch-fit-plus", "image_right": True},
    ],
    "drone": [
        {"eyebrow": "FEATURED DRONE", "title": "Pro 4K HDR\nAerial Photography",
         "description": "Cinema-grade footage with intelligent obstacle sensing.",
         "image_src": "/images/product3.webp", "image_alt": "Pro drone",
         "cta_href": "/product/drone-pro-quadcopter", "image_right": False},
        {"eyebrow": "TRAVEL-READY", "title": "Sub-249g\nFolding Body",
         "description": "Fits in your pocket. Unfolds in seconds.",
         "image_src": "/images/product4.webp", "image_alt": "Mini drone",
         "cta_href": "/product/drone-mini-folding", "image_right": True},
    ],
    "backpack": [
        {"eyebrow": "FEATURED BAG", "title": "30L Travel\nBackpack",
         "description": "TSA-friendly opening with dedicated laptop sleeve.",
         "image_src": "/images/product4.webp", "image_alt": "Travel backpack",
         "cta_href": "/product/travel-backpack-30l", "image_right": False},
        {"eyebrow": "ICONIC DESIGN", "title": "The Classic\nDaypack",
         "description": "Leather straps, signature stripe, lifetime guarantee.",
         "image_src": "/images/product5.webp", "image_alt": "Daypack",
         "cta_href": "/product/daypack-classic", "image_right": True},
    ],
}


# ─── Banner per theme ───────────────────────────────────────────────────

BANNER_BY_THEME = {
    "airpod": {
        "eyebrow": "#Action Feature", "title": "Ultimate comfort.",
        "background_image": "/images/bg.webp",
        "cta_label": "Buy Now", "cta_href": "/product/airpod-product-ides",
        "features": [
            {"icon": "icofont-bluetooth", "label": "Smart Connectivity"},
            {"icon": "icofont-battery-full", "label": "Long lasting battery"},
            {"icon": "icofont-touch", "label": "Touch Control Panel"},
            {"icon": "icofont-volume-up", "label": "Volume Up Control"},
            {"icon": "icofont-water-drop", "label": "Water Dust Proof"},
        ],
    },
    "smartwatch": {
        "eyebrow": "#Always On", "title": "Smarter every day.",
        "background_image": "/images/bg.webp",
        "cta_label": "Shop Watches", "cta_href": "/product/smartwatch-series-x",
        "features": [
            {"icon": "icofont-heart-beat", "label": "Heart Rate"},
            {"icon": "icofont-tools", "label": "GPS Tracking"},
            {"icon": "icofont-battery-full", "label": "7-day Battery"},
            {"icon": "icofont-water-drop", "label": "50m Water Resistance"},
        ],
    },
    "drone": {
        "eyebrow": "#Take Flight", "title": "Cinema in the sky.",
        "background_image": "/images/bg.webp",
        "cta_label": "Buy Drone", "cta_href": "/product/drone-pro-quadcopter",
        "features": [
            {"icon": "icofont-eye", "label": "4K HDR Camera"},
            {"icon": "icofont-clock-time", "label": "35-min Flight"},
            {"icon": "icofont-tools", "label": "GPS Return-to-Home"},
            {"icon": "icofont-shield", "label": "Obstacle Sensing"},
        ],
    },
    "backpack": {
        "eyebrow": "#Carry It Well", "title": "Built for life.",
        "background_image": "/images/bg.webp",
        "cta_label": "Shop Bags", "cta_href": "/product/travel-backpack-30l",
        "features": [
            {"icon": "icofont-suitcase", "label": "TSA-Friendly"},
            {"icon": "icofont-laptop", "label": "Padded Laptop Sleeve"},
            {"icon": "icofont-shield", "label": "RFID Pocket"},
            {"icon": "icofont-water-drop", "label": "Water Resistant"},
        ],
    },
}


# ─── Blog ───────────────────────────────────────────────────────────────

BLOG_CATEGORIES = ["News", "Reviews", "Buying Guide"]
BLOG_TAGS = ["airpod", "smartwatch", "drone", "backpack", "news", "tech", "audio"]
BLOG_POSTS = [
    {"title": "Sarbi at ligula porta", "category": "News",
     "tags": ["airpod", "news"],
     "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
     "body": "Headphones have come a long way — here is our pick of the year so far...",
     "cover_url": "/images/blog1.webp"},
    {"title": "Donec tellus nulla lorem", "category": "Reviews",
     "tags": ["smartwatch", "tech"],
     "excerpt": "An honest review of the latest smartwatch lineup.",
     "body": "We tested the top 5 smartwatches for two weeks straight...",
     "cover_url": "/images/blog2.webp"},
    {"title": "Norbi at omgula qorta", "category": "Buying Guide",
     "tags": ["drone", "tech"],
     "excerpt": "How to pick the right drone for travel photography.",
     "body": "Folding drones changed the travel photography game...",
     "cover_url": "/images/blog3.webp"},
    {"title": "Quanto rib ai mortala", "category": "Reviews",
     "tags": ["backpack"],
     "excerpt": "The 30L travel backpack roundup.",
     "body": "We carried five travel backpacks across three continents...",
     "cover_url": "/images/blog4.webp"},
    {"title": "Plomo at terra quanta", "category": "News",
     "tags": ["audio", "airpod"],
     "excerpt": "The next generation of wireless audio is here.",
     "body": "Adaptive audio is the headline feature of the new airpod variants...",
     "cover_url": "/images/blog1.webp"},
]

FAQS = [
    ("What is your return policy?", "We offer a 30-day no-questions-asked return policy on all products."),
    ("How long does shipping take?", "Standard shipping takes 5-7 business days. Express options are available at checkout."),
    ("Do you ship internationally?", "Yes, we ship to over 50 countries worldwide."),
    ("How do I track my order?", "Once shipped, you'll receive a tracking link via email."),
    ("Are your products authentic?", "Yes, every item is sourced directly from manufacturers and authorized distributors."),
    ("Do you offer a warranty?", "All electronics come with a 12-month manufacturer warranty."),
    ("How do I cancel an order?", "Open the order from your account page and hit Cancel within 24 hours of purchase."),
]

ABOUT = {
    "title": "About Sinp",
    "intro": "Sinp is a single-product e-commerce brand delivering premium audio, watch, drone and bag products directly to enthusiasts around the world.",
    "body": (
        "Founded with a passion for sound, we curate every product to meet uncompromising standards. "
        "From wireless earbuds to studio-grade headphones, each item is selected for craftsmanship, "
        "reliability, and timeless design."
        "\n\n"
        "Our mission is simple: bring exceptional experiences to everyone, everywhere. "
        "We believe great products should be accessible, beautiful, and built to last."
    ),
}

TEAM = [
    ("Alex Carter", "Founder & CEO", "Started Sinp in a garage with a single product line."),
    ("Mira Tanaka", "Head of Product", "Leads product curation and quality control."),
    ("Diego Romero", "Customer Experience", "Manages every customer touchpoint."),
]


class Command(BaseCommand):
    help = "Seed the database with FE-aligned demo data (4 themes)."

    def add_arguments(self, parser):
        parser.add_argument("--reset", action="store_true", help="Delete existing demo data first.")

    @transaction.atomic
    def handle(self, *args, **options):
        if options["reset"]:
            self.stdout.write("Resetting demo data...")
            Product.objects.all().delete()
            Brand.objects.all().delete()
            Vendor.objects.all().delete()
            Color.objects.all().delete()
            Tag.objects.all().delete()
            Size.objects.all().delete()
            Category.objects.all().delete()
            Theme.objects.all().delete()
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

        # superuser
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                email="admin@sinp.local", username="admin", password="admin12345"
            )
            self.stdout.write(self.style.SUCCESS("Created superuser admin@sinp.local / admin12345"))

        # themes + categories
        theme_objs = {}
        for t in THEMES:
            obj, _ = Theme.objects.get_or_create(slug=t["slug"], defaults={"name": t["name"]})
            theme_objs[t["slug"]] = obj
            for cat_name in t["categories"]:
                cat_slug = f"{t['slug']}-{cat_name.lower().replace(' ', '-')}"
                Category.objects.get_or_create(
                    slug=cat_slug,
                    defaults={"name": cat_name, "theme": obj},
                )

        vendor_objs = {name: Vendor.objects.get_or_create(name=name)[0] for name in VENDORS}
        color_objs = {
            c["value"]: Color.objects.get_or_create(
                value=c["value"], defaults={"name": c["name"], "hex": c["hex"]}
            )[0]
            for c in COLORS
        }
        tag_objs = {name: Tag.objects.get_or_create(name=name)[0] for name in TAGS}
        size_objs = {name: Size.objects.get_or_create(name=name)[0] for name in SIZES}

        # products
        for data in PRODUCTS:
            theme = theme_objs[data["theme"]]
            cat_slug = f"{data['theme']}-{data['category'].lower().replace(' ', '-')}"
            category = Category.objects.get(slug=cat_slug)
            vendor = vendor_objs.get(data["vendor"])

            product, created = Product.objects.get_or_create(
                sku=data["sku"],
                defaults={
                    "theme": theme,
                    "category": category,
                    "vendor": vendor,
                    "name": data["name"],
                    "short_description": data.get("description", "")[:200],
                    "description": data.get("description", ""),
                    "price": Decimal(data["price"]),
                    "sale_price": Decimal(data["sale_price"]) if data.get("sale_price") else None,
                    "stock": data["stock"],
                    "is_featured": data["is_featured"],
                    "image_url": data["image"],
                },
            )
            if created:
                product.colors.set([color_objs[c] for c in data.get("colors", []) if c in color_objs])
                product.tags.set([tag_objs[t] for t in data.get("tags", []) if t in tag_objs])
                product.sizes.set([size_objs[s] for s in data.get("sizes", []) if s in size_objs])

        # hero slides
        for theme_slug, slides in HERO_SLIDES_BY_THEME.items():
            theme = theme_objs[theme_slug]
            for idx, slide in enumerate(slides):
                HeroSlide.objects.get_or_create(
                    theme=theme, title=slide["title"],
                    defaults={**slide, "order": idx},
                )

        # featured
        for theme_slug, featured in FEATURED_BY_THEME.items():
            theme = theme_objs[theme_slug]
            for idx, f in enumerate(featured):
                FeaturedProduct.objects.get_or_create(
                    theme=theme, title=f["title"],
                    defaults={**f, "order": idx},
                )

        # banners
        for theme_slug, b in BANNER_BY_THEME.items():
            theme = theme_objs[theme_slug]
            banner, created = Banner.objects.get_or_create(
                theme=theme,
                defaults={
                    "eyebrow": b["eyebrow"], "title": b["title"],
                    "background_image": b["background_image"],
                    "cta_label": b["cta_label"], "cta_href": b["cta_href"],
                },
            )
            if created:
                for idx, feat in enumerate(b["features"]):
                    BannerFeature.objects.create(
                        banner=banner, icon=feat["icon"], label=feat["label"], order=idx,
                    )

        # blog
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
                    "cover_url": data.get("cover_url", ""),
                    "status": BlogPost.PUBLISHED,
                    "published_at": timezone.now() - timedelta(days=idx * 7),
                },
            )
            if created:
                post.tags.set(BlogTag.objects.filter(name__in=data["tags"]))

        # FAQ / about / team
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

        self.stdout.write(self.style.SUCCESS("Seed complete."))
