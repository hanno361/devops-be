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

## API surface (high level)

### Public

- `GET  /api/catalog/categories/`
- `GET  /api/catalog/brands/`
- `GET  /api/catalog/products/`            (filter, search, ordering, pagination)
- `GET  /api/catalog/products/{slug}/`
- `GET  /api/blog/categories/`
- `GET  /api/blog/tags/`
- `GET  /api/blog/posts/`
- `GET  /api/blog/posts/{slug}/`
- `GET  /api/pages/faqs/`
- `GET  /api/pages/about/`
- `POST /api/pages/contact/`
- `POST /api/auth/register/`
- `POST /api/auth/login/`                  (returns access + refresh)
- `POST /api/auth/token/refresh/`

### Auth required (JWT `Authorization: Bearer …`)

- `GET/PATCH /api/auth/me/`
- `GET    /api/cart/`
- `POST   /api/cart/items/`
- `PATCH  /api/cart/items/{id}/`
- `DELETE /api/cart/items/{id}/`
- `POST   /api/cart/clear/`
- `GET/POST /api/wishlist/`
- `DELETE /api/wishlist/{id}/`
- `POST /api/orders/checkout/`
- `GET  /api/orders/`
- `GET  /api/orders/{number}/`

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
