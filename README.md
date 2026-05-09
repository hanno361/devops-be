# Sinp Backend (devops-be)

Django REST Framework backend for the **Sinp** single-product e-commerce site
(perfume / cosmetic atelier scenario).

Course project: **BSM464 — Güncel Yazılım Geliştirme Süreçleri ve DevOps**.

The matching frontend (Next.js + Tailwind, based on the Sinp HTML template) lives
in a separate repository and consumes this API.

---

## Stack

- **Django 5** + **DRF**
- **PostgreSQL 16** (local via Docker, prod on Azure Database for PostgreSQL)
- **SimpleJWT** for authentication
- **drf-spectacular** for OpenAPI / Swagger UI
- **Docker** + **docker-compose**
- **pytest** + **pytest-django** for tests

## Project layout

```
config/                      Django project (split settings)
  settings/{base,dev,prod,test}.py
  urls.py / api_urls.py
apps/
  accounts/                  Custom user, register, login (JWT), me
  catalog/                   Category, Brand, Product, ProductImage (+ seed)
  blog/                      BlogCategory, BlogTag, BlogPost
  pages/                     FAQ, AboutPage, TeamMember, ContactMessage
  cart/                      Cart, CartItem (auth)
  wishlist/                  WishlistItem (auth)
  orders/                    Order, OrderItem, checkout service (auth)
docker-compose.yml           web + db
Dockerfile
requirements.txt
pytest.ini / conftest.py
```

## Quick start (Docker)

```bash
cp .env.example .env
docker compose up --build
```

After containers are up:

```bash
# create superuser + seed demo data
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py seed
```

The `seed` command also auto-creates a default admin (`admin@sinp.local` /
`admin12345`) the first time it runs if no superuser exists.

| Endpoint                                | URL                                                 |
| --------------------------------------- | --------------------------------------------------- |
| API root                                | http://localhost:8000/api/                          |
| Swagger UI                              | http://localhost:8000/api/schema/swagger-ui/        |
| ReDoc                                   | http://localhost:8000/api/schema/redoc/             |
| Django admin                            | http://localhost:8000/admin/                        |

## Local (without Docker)

```bash
python3.11 -m venv .venv
.venv/bin/pip install -r requirements.txt
# point POSTGRES_HOST to your local Postgres or run docker compose up db
.venv/bin/python manage.py migrate
.venv/bin/python manage.py seed
.venv/bin/python manage.py runserver
```

## Tests

Tests use an in-memory SQLite via `config.settings.test` so they run without
PostgreSQL:

```bash
.venv/bin/pytest
```

## API surface — frontend contract

This BE is shaped to match the Next.js frontend exactly. All endpoints are
under `/api`. URLs do **not** end with a trailing slash (`APPEND_SLASH=False`).

### Response envelopes

| Type    | Shape                                                              |
| ------- | ------------------------------------------------------------------ |
| List    | `{ data: T[], meta: { page, pageSize, totalItems, totalPages } }`  |
| Single  | `{ data: T }`                                                      |
| Error   | `{ error: { code, message, details? } }`                           |

### Query params (list endpoints)

| Param      | Notes                                                          |
| ---------- | -------------------------------------------------------------- |
| `page`     | 1-indexed                                                      |
| `pageSize` | default 12, max 100                                            |
| `sort`     | `default \| price_asc \| price_desc \| name_asc \| name_desc` |
| `search`   | full-text search where supported                               |

### Public

- `POST /api/auth/register`         body: `{email, password, name}` → `{user, token}`
- `POST /api/auth/login`            body: `{email, password}` → `{user, token}`
- `GET  /api/products`              list of `Product`
- `GET  /api/products/{slug}`       single `Product`
- `GET  /api/blog`                  list of `BlogPost`
- `GET  /api/blog/{slug}`           single `BlogPost`
- `GET  /api/faq`                   list of `FaqItem`
- `GET  /api/about`                 single `AboutContent` (body is `string[]`)
- `POST /api/contact`               body: `{name, email, subject, message}`
- `GET  /api/home/hero-slides`      list of `HeroSlide`
- `GET  /api/home/featured-products`list of `FeaturedProductData`
- `GET  /api/home/banner`           single `BannerData`
- `GET  /api/home/products`         featured products for the homepage grid
- `GET  /api/home/blog`             latest blog posts for the homepage

### Auth required (JWT `Authorization: Bearer <token>`)

- `GET  /api/auth/me`               → `{data: User}`
- `GET  /api/orders`                list of own `Order`s
- `POST /api/orders`                body: `{items:[{productId,productName,quantity,price}], shipping:{name,email,phone,address,city,zipCode}}` → `{data: Order}`
- `GET  /api/orders/{orderNumber}`  single `Order`

### Internal (kept for completeness; not consumed by the FE)

- `GET/POST /api/cart/`, `/api/cart/items/...`
- `GET/POST /api/wishlist/`

## Environment variables

See `.env.example`. Required in production:

- `DJANGO_SETTINGS_MODULE=config.settings.prod`
- `DJANGO_SECRET_KEY`
- `DJANGO_ALLOWED_HOSTS`
- `POSTGRES_*` (Azure-managed Postgres values)
- `CORS_ALLOWED_ORIGINS` (frontend origin)

## Deploy notes (Azure)

- Provision **Azure Database for PostgreSQL — Flexible Server**, set firewall to
  allow the VM, take `host / db / user / password` and put them in `.env`.
- Provision a small **Azure VM** (Linux), install Docker + Compose.
- Clone the repo, set `.env`, run `docker compose -f docker-compose.yml up -d`.
- Point an `.xyz` domain at the VM's public IP; terminate TLS via Caddy or
  Nginx in front of the `web` service if needed.
- The Azure Pipelines pipeline (lives in the project-lead's repo) builds and
  deploys this image to the VM on push to `master`.

## Course requirement mapping

| Requirement                                                    | Where                                                         |
| -------------------------------------------------------------- | ------------------------------------------------------------- |
| Django Web API + PostgreSQL                                    | `config/`, `apps/`, `docker-compose.yml`                      |
| Code-first, modular, sınıf tasarım prensipleri                 | One Django app per domain, thin views, services for orders    |
| Frontend ↔ Backend Docker                                      | `Dockerfile`, `docker-compose.yml`                            |
| Login + ≥ 5 protected pages                                    | `me`, `cart`, `wishlist`, `orders`, `checkout`                |
| Listing page + detail page                                     | Products list + detail, Orders list + detail                  |
| Contact form                                                   | `POST /api/pages/contact/`                                    |
| ≥ 10 sub-pages backed by Postgres                              | products, categories, brands, blog posts, blog categories, tags, faqs, about, cart, wishlist, orders |
| Unit tests for important units                                 | `apps/*/tests/test_*.py` (17 tests)                           |
| Swagger                                                        | `/api/schema/swagger-ui/`                                     |
