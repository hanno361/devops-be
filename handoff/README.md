# FE Geliştirici için BE Handoff Paketi

Bu klasör, Sinp BE'yi başka bir makinede ayağa kaldırmak için gereken her şeyi içerir.

## En kolay yol — sıfırdan kurulum (önerim)

Dump'a hiç ihtiyacın yok, BE kendi kendini doldurur:

```bash
git clone https://github.com/hanno361/devops-be.git
cd devops-be
cp .env.example .env
docker compose up -d --build
docker compose exec web python manage.py seed
```

Bitince:
- API:     http://localhost:8000/api/
- Swagger: http://localhost:8000/api/schema/swagger-ui/
- Admin:   http://localhost:8000/admin/   (admin@sinp.local / admin12345)

`seed` komutu 10 ürün + 5 blog yazısı + 7 FAQ + about + hero slides + featured + banner + admin user oluşturur.

## Frontend'i bağlamak

FE projesinin kökünde `.env.local` dosyası oluştur:

```bash
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000/api
```

Sonra `npm run dev`. Hepsi bu kadar — FE Django'ya konuşur.

## Aynı veriyi Docker'sız makinede istiyorsan

İki dosya var:

### Seçenek 1 — `sinp_fixtures.json` (Django, en taşınabilir)

```bash
# BE klasöründe
python manage.py migrate
python manage.py loaddata handoff/sinp_fixtures.json
```

Boyutu küçük (17 KB), Postgres veya SQLite fark etmez.

### Seçenek 2 — `sinp_db.sql` (Postgres-only, ham)

```bash
psql -h 127.0.0.1 -U sinp -d sinp < handoff/sinp_db.sql
```

(`sinp` kullanıcısı + `sinp` DB'si önceden var olmalı.)

## Kullanıcılar

| Email | Şifre | Rol |
|---|---|---|
| `admin@sinp.local` | `admin12345` | Süper-admin (admin paneli + içerik yönetimi) |

Yeni kayıt için FE'deki `/login-register` veya `POST /api/auth/register` (Swagger'dan da çalışır).

## API contract

Ana README'deki "API surface — frontend contract" bölümüne bak (`/Users/kadir/Desktop/devops/README.md`).
