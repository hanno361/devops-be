# Test Dokümantasyonu ve Uygulama Rehberi

Bu doküman, **Sinp Backend** projesi için hazırlanan birim (unit) ve entegrasyon testlerinin yapısını, kapsamını ve nasıl çalıştırılacağını açıklamaktadır. Proje, test süreçlerinde `pytest` ekosistemini kullanmaktadır.

---

## 1. Test Altyapısı ve Ayarlar

Sistem, testlerin hızlı ve güvenli bir şekilde koşturulması için ana veritabanından (PostgreSQL) izole edilmiştir.

- **Veritabanı:** Testler sırasında RAM üzerinde çalışan (in-memory) bir SQLite veritabanı kullanılır. Bu, fiziksel disk yazımını engeller ve testlerin saniyeler içinde tamamlanmasını sağlar.
- **İzolasyon:** Her test fonksiyonu `@pytest.mark.django_db` dekoratörü ile işaretlenmiştir. Bu sayede her test kendi işlem (transaction) bloğunda çalışır ve tamamlandığında veritabanı ilk haline geri döner (rollback).
- **Ayar Dosyası:** Testler, `config/settings/test.py` dosyasındaki özel konfigürasyonları baz alır.

---

## 2. Test Kategorileri

### Birim Testleri (Unit Tests)

Uygulamanın en küçük bileşenlerinin iş mantığını doğrular.

- **Modeller:** Otomatik slug üretimi (SEO dostu URL), fiyat hesaplamaları (indirimli fiyat mantığı) ve veritabanı kısıtlamaları (benzersizlik kontrolleri) test edilmiştir.
- **Serializerlar:** Veri dönüşüm kuralları, frontend için hazırlanan özel JSON formatları (`badges`, `cta` nesneleri) ve girdi doğrulama (miktar kontrolü vb.) kuralları test edilmiştir.
- **Servisler:** Sipariş oluşturma gibi birden fazla modeli etkileyen karmaşık işlemler, stok kontrolü ve hata fırlatma senaryoları özelinde test edilmiştir.

### Entegrasyon Testleri (API Tests)

Sistemin tüm katmanlarının (URL, View, Serializer, Model) birlikte uyumlu çalışmasını test eder.

- **API Contract:** Frontend (Next.js) ile kararlaştırılan veri zarfı (data envelope) yapısı ve hata formatları her endpoint için doğrulanmıştır.
- **Yetkilendirme:** JWT tabanlı kimlik doğrulama gerektiren Orders, Cart ve Wishlist gibi modüllerde yetkisiz erişimlerin engellendiği ve kullanıcı izolasyonunun sağlandığı kanıtlanmıştır.

---

## 3. Modüler Test Yapısı

Testler, projenin her bir uygulaması (app) altında `/tests` dizininde mantıksal dosyalara bölünmüştür:

```
apps/
└── [app_name]/
    └── tests/
        ├── test_models.py      # Veritabanı ve iş mantığı testleri
        ├── test_serializers.py # Veri doğrulama ve formatlama testleri
        ├── test_api.py         # HTTP istek/yanıt ve endpoint testleri
        └── test_admin.py       # Admin paneli özel izin testleri
```

---

## 4. Testlerin Çalıştırılması

Testleri çalıştırmadan önce sanal ortamın (`venv`) aktif olduğundan ve gerekli paketlerin yüklü olduğundan emin olunmalıdır.

### Tüm Testleri Çalıştırmak

Proje kök dizininde aşağıdaki komutu çalıştırın:

```bash
pytest
```

### Belirli Bir Uygulamanın Testlerini Çalıştırmak

Örneğin sadece sepet (cart) modülünü test etmek için:

```bash
pytest apps/cart/tests/
```

### Hata Mesajlarını Detaylı Görmek

Testler sırasında çıktıları ve detayları görmek için `-v` (verbose) parametresini ekleyebilirsiniz:

```bash
pytest -v
```

---

## 5. Kapsanan Temel Senaryolar

- **Auth:** Kayıt sırasında e-posta adresinden benzersiz kullanıcı adı üretilmesi ve isim parçalama algoritması.
- **Catalog:** İndirimli ürünlerde yüzdelik badge hesaplaması ve sadece aktif ürünlerin listelenmesi.
- **Orders:** Sipariş sonrası ilgili ürünlerin stoğundan adet düşülmesi ve yetersiz stokta işlemin iptal edilmesi.
- **Cart:** Sepete aynı ürün tekrar eklendiğinde yeni satır açmak yerine miktarın güncellenmesi.
- **Core:** Tüm sistem genelinde hata mesajlarının frontend uyumlu bir standart yapıya dönüştürülmesi.