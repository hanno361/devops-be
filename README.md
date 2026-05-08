# Sinp Backend (devops-be)

Django REST Framework backend for the **Sinp** single-product e-commerce site.
Course project: BSM464 — Güncel Yazılım Geliştirme Süreçleri ve DevOps.

## Stack

- Django 5 + DRF
- PostgreSQL 16
- SimpleJWT auth
- drf-spectacular (Swagger UI)
- Docker + docker-compose

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

- API:        http://localhost:8000/api/
- Swagger:    http://localhost:8000/api/schema/swagger-ui/
- Admin:      http://localhost:8000/admin/

## More

See setup, seed, tests, deploy details below — populated as stages land.
