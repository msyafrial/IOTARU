# IOTARU Design System

> Design tokens, komponen, dan konvensi visual untuk website IOTARU Teknologi Nusantara.
> Sumber kebenaran: `public/css/custom.css` (variabel global di `:root`), `public/css/fonts.css`, `src/styles/global.css`, `src/styles/critical.css`.

---

## 1. Brand

| Item | Nilai |
|------|-------|
| Nama brand | IOTARU Teknologi Nusantara |
| Domain | IOT (Internet of Things) — smart security, monitoring, automation |
| Logo | `/public/images/logo.png` (max-width 140px di footer, 100px di navbar mobile) |
| Tone visual | Dark-tech, profesional, industrial; aksen oranye energik |
| Bahasa UI | Campuran EN/ID (heading EN, label tombol CTA terkadang ID — "Lihat Semua Produk") |

---

## 2. Color Tokens

Didefinisikan di `public/css/custom.css` → `:root`:

| Token | Nilai | Penggunaan |
|-------|-------|------------|
| `--primary-color` | `#03171D` | Warna dasar gelap (teal-hitam). Background section gelap, warna heading, teks pada tombol aksen |
| `--secondary-color` | `#F9F9F9` | Background section terang / kartu |
| `--bg-color` | `#FFFFFF` | Background dasar halaman |
| `--text-color` | `#59676C` | Teks body / paragraf (abu-abu kebiruan) |
| `--accent-color` | `#FF9800` | Oranye aksen — tombol CTA, ikon, highlight, hover, badge dot |
| `--white-color` | `#FFFFFF` | Teks di atas section gelap |
| `--divider-color` | `#03171D1A` | Divider/border di section terang (10% opacity dari primary) |
| `--dark-divider-color` | `#FFFFFF1A` | Divider/border di section gelap (10% opacity putih) |
| `--error-color` | `rgb(230, 87, 87)` | Pesan error form |
| `--default-font` | `"Inter Tight", sans-serif` | Font utama |

### 2.1 Palet Sistem Warna

```text
Primary (dark)   #03171D  ████████  → section gelap, heading, teks tombol
Secondary (bg)   #F9F9F9  ▒▒▒▒▒▒▒▒  → kartu & section terang
Surface          #FFFFFF  ░░░░░░░░  → halaman, kartu di atas secondary
Text body        #59676C  ████████  → paragraf
Accent           #FF9800  ████████  → CTA, ikon, indikator aktif
Error            #E65757  ████████  → validasi form
```

### 2.2 Aturan Pemakaian Warna

- **Kontras tinggi selalu**: teks di atas `--primary-color` = putih; teks di atas aksen = `--primary-color`.
- Divider memakai **alpha token**, bukan warna baru — jangan hardcode rgba baru.
- Section gelap memakai class `.dark-section` (dengan background-image dekoratif), section terang `.bg-section`.

---

## 3. Typography

### 3.1 Font Face

- **Inter Tight Variable** (weight `100 900`), self-hosted woff2 (`latin` + `latin-ext` + italic).
- `font-display: swap` — wajib dipertahankan.
- Fallback stack: `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`.
- Tidak boleh memuat font dari CDN eksternal (CSP `font-src 'self' data:`).

### 3.2 Base

| Properti | Nilai |
|----------|-------|
| Font-size body | `16px` |
| Line-height body | `1em` (paragraf `1.6em`) |
| Weight heading | `600` (H1 hero `500`) |
| Line-height heading | `1.2em` |

### 3.3 Type Scale (Desktop → Mobile)

| Elemen | Desktop | ≤991px | ≤767px |
|--------|---------|--------|--------|
| H1 hero / page-header | `80px` / w500 | `54px` | `28px` |
| H2 section-title | `48px` | `38px` | `26px` |
| H2 post-entry | `48px` | `38px` | `26px` |
| H3 post-entry | `40px` | — | — |
| H4 post-entry | `30px` | — | — |
| Kartu / judul item (h3) | `20px` | `18px` (mobile) | `18px` |
| Label eyebrow (`section-title h3`) | `14px`, pill, uppercase-ish (capitalize) | — | — |
| Body paragraf | `16px` | `16px` | `16px` |
| Footer link / meta | `16px` | — | — |

### 3.4 Pola Khas

- **Eyebrow/pill label**: `.section-title h3` — pill `border-radius: 100px`, background `--secondary-color` (terang) atau `--dark-divider-color` + blur (gelap), dengan **dot aksen 8px** di kiri (`::before`), padding `8px 16px 8px 34px`.
- Heading center: `.section-title.section-title-center`.
- Teks di section gelap: selalu `--white-color` (dicover oleh aturan `.dark-section ...`).

---

## 4. Spacing

| Token pola | Nilai |
|------------|-------|
| Padding section (desktop) | `100px 0` |
| Padding section (≤991px) | `50px 0` |
| Jarak antar item grid | `30px` (gap flex) |
| Section title margin-bottom | `40px` (mobile `30px`) |
| `.section-row` margin-bottom | `80px` (mobile `40px` → `30px` @767px) |
| Padding kartu standar | `30–40px` (mobile `20px`) |
| Padding kartu "wrapper" (pricing, what-we-do-3) | `10px` (kartu dalam kartu) |

**Aturan**: skala spacing mengikuti pola `10 / 20 / 30 / 40 / 50 / 60 / 80 / 100`. Hindari nilai di luar pola.

---

## 5. Radius

| Token | Nilai | Penggunaan |
|-------|-------|------------|
| Kartu / section / figure | `20px` | `.bg-section`, kartu, gambar, accordion, form-box |
| Elemen sedang | `10px` | Tombol, input, ikon-box, pagination, tag |
| Elemen kecil (mobile accordion) | `14px` | — |
| Pill / avatar / dot | `100px` / `50%` | Label pill, social icon, skill bar, dot |

---

## 6. Elevation & Glassmorphism

Proyek ini tidak memakai box-shadow untuk depth; efek kedalaman dicapai dengan:

| Teknik | Implementasi |
|--------|--------------|
| **Glass blur** | `backdrop-filter: blur(30–50px)` + `--dark-divider-color` background (navbar, kartu testimoni, form footer) |
| **Hover lift** | `transform: translateY(-5px)` (integration item) |
| **Image zoom** | `transform: scale(1.06)` pada hover gambar kartu (blog/team), transisi `0.6s` |
| **Transisi standar** | `all 0.4s ease-in-out` (elemen besar), `all 0.3s ease-in-out` (elemen kecil) |

---

## 7. Buttons

### 7.1 `.btn-default` (utama)

```text
background: var(--accent-color)
color:      var(--primary-color)
font:       16px / 600, capitalize
padding:    20px 58px 20px 24px   (mobile 17px 45px 17px 18px)
radius:     10px
```

- Ada **panah 24px** di kanan via `::before` (sprite `arrow-primary.svg`).
- Hover: warna teks → putih, dan `::after` (layer `--primary-color`) **mengembang dari kanan ke kiri** hingga memenuhi tombol (width 0 → 100%).

### 7.2 Varian

| Varian | Perbedaan |
|--------|-----------|
| `.btn-dark` | Background `--dark-divider-color` + `backdrop-filter: blur(50px)`, teks putih (untuk section gelap) |
| `.btn-highlighted` | Sama seperti default; hover mengembalikan teks ke primary, `::after` putih |

### 7.3 Aturan

- Satu CTA primer per konteks (jangan dua `btn-default` berdampingan tanpa hierarki).
- Panah pada tombol wajib ada untuk link navigasi; untuk tombol form (submit newsletter) boleh ikon saja.

---

## 8. Komponen Inti

### 8.1 Section Shell

```html
<section class="key-features bg-section">          <!-- terang -->
<section class="why-choose-us bg-section dark-section"> <!-- gelap -->
  <div class="container">
    <div class="row section-row">
      <div class="col-lg-12">
        <div class="section-title section-title-center">
          <h3>Eyebrow label</h3>       <!-- pill + dot aksen -->
          <h2 class="text-anime-style-3" data-cursor="-opaque">Judul besar</h2>
          <p class="wow fadeInUp" data-wow-delay="0.2s">Deskripsi</p>
        </div>
      </div>
    </div>
    <!-- konten grid Bootstrap -->
  </div>
</section>
```

- `.bg-section`: max-width `1880px`, radius `20px`, background `--secondary-color`; di ≤991px radius dihilangkan.
- `.dark-section`: background `--primary-color` + tekstur `dark-section-bg-shape.png`.

### 8.2 Navbar Glass (`Navbar.astro`)

- `.glass-nav` mengambang (absolute, top 50px), glass effect saat scroll (`.scrolled`).
- Desktop: `.glass-nav-menu` + CTA `.glass-nav-cta` (→ `/contact`).
- **Dropdown** (Solutions & Products): wrapper `.glass-nav-item.has-dropdown` → panel `.glass-dropdown`.
  - **Arsitektur portal**: panel dipindahkan ke `<body>` via JS saat init. Alasan: `backdrop-filter` pada descendant dari elemen yang punya `backdrop-filter` sendiri (`.glass-nav`) tidak membaca backdrop halaman — panel tampak transparan tanpa blur. Dengan portal, frosted glass dropdown identik dengan navbar.
  - **Anti-FOUC (fix bug flash dropdown saat load)**: akar masalahnya `custom.css` dimuat async via trik `media="print"` → aturan sembunyi (`.glass-dropdown` opacity:0, `.glass-mobile-submenu` max-height:0) baru aktif setelah CSS selesai load, sehingga panel muncul sesaat tanpa style saat first paint. Solusinya dua lapis:
    1. Panel di-*server-render* dengan atribut **`hidden`** (`.glass-dropdown` ×2 dan `.glass-mobile-submenu` ×2) — UA stylesheet menyembunyikan sejak paint pertama, tanpa perlu CSS eksternal.
    2. Gate JS `cssReady()`: JS hanya melepas `hidden` setelah stylesheet dipastikan aktif (`link.media === 'all'`, dideteksi via event `load` + polling 60ms). **Tanpa timeout fallback tanpa syarat** — jika CSS lambat, panel tetap tersembunyi sampai CSS benar-benar aktif (terverifikasi simulasi slow-network: tidak ada flash).
    3. Submenu mobile: `hidden` dilepas saat accordion pertama kali dibuka (sebelum set `maxHeight`).
  - Posisi panel: `position: fixed`, dihitung JS dari `getBoundingClientRect()` trigger (+14px gap), di-reposisi saat scroll/resize.
  - Muncul via **hover** (dengan delay close 120ms agar mouse bisa pindah ke panel), **klik trigger** (toggle), dan **fokus keyboard**; `Escape` menutup. Hanya satu panel terbuka pada satu waktu (exclusive-open).
  - Glass formula **serasi dengan navbar**: `rgba(3,23,29,0.6)` + `blur(30px) saturate(160%)` (navbar: 0.4/12px — keluarga warna sama), border alpha `0.08`, shadow lembut memakai warna brand `rgba(3,23,29,0.28)` — **bukan hitam pekat**.
  - Hover item = alpha putih `0.1` (sama dengan hover link navbar); desc text alpha `0.6` (dekat dengan link navbar `0.7`).
  - Outline fokus keyboard memakai **aksen oranye** 2px (`:focus-visible`), bukan outline default browser.
  - Panel disembunyikan total (`display: none`) di ≤991px — mobile memakai accordion.
  - Bridge `::after` setinggi 14px mencegah gap hover antara link dan panel.
  - Caret chevron rotate 180° saat aktif.
  - Item dropdown: `.glass-dropdown-item` = ikon box 38px (radius 10px, aksen → fill aksen saat hover) + title 14px/600 + desc 12px.
  - Solutions: daftar vertikal 3 item (ikon path per-solusi) + footer "View all solutions".
  - Products: **grid 2 kolom** 6 produk terbaru + row chip kategori (`.glass-dropdown-cat-chip`) + footer "View all N products".
  - Data dropdown **di-generate dari content collection** (`getCollection`) saat build — bukan hardcode.

**Mobile sidebar** (≤991px) — `.glass-mobile-menu`:
  - **Satu tema desktop**: background `rgba(3,23,29,0.8)` (sama navbar scrolled state) + blur 24px saturate 200%, border-left alpha 0.05, sudut kiri membulat radius 24px, shadow dengan aksen oranye subtle.
  - **Link pill**: radius 100px, text alpha 0.7, hover alpha 0.1 background — identik desktop `.glass-nav-link`.
  - **Active link styling**: pill oranye aksen + shadow 0 2px 12px rgba(255,152,0,0.35) — konsisten dengan `.glass-nav-link.active` desktop.
  - Slide-in dari kanan (`translateX(100%)` → 0), overlay blur, close via tombol ✕, overlay click, link click, atau `Escape`; body `overflow: hidden` saat terbuka.
  - **Submenu accordion**: `.glass-mobile-group` pill radius 100px + tombol `.glass-mobile-group-btn` (flex, gap 14px, pill 100px, text alpha 0.7 → 1.0 saat open). Chevron rotate 180° saat terbuka.
  - **Active tombol accordion (Solutions/Products)**: karena tombol grup adalah `<button>` (bukan `<a>`), class `active` di-set server-side via `isActive('/solutions')` / `isActive('/products')` di frontmatter (match semua child, mis. `/products/smart-cam`). CSS rule `.glass-mobile-group-btn.active` (juga `.active.open`) = pill aksen oranye identik `.glass-mobile-link.active`; dideklarasikan **setelah** rule `.open` agar state "halaman saat ini" selalu menang saat accordion terbuka sekaligus aktif.
  - Submenu terbuka/tutup via `max-height` 0.35s anim. Single-open: membuka satu grup menutup grup lain. Produk dikelompokkan per kategori.
  - **Divider submenu**: `border-left: 2px solid var(--dark-divider-color)` — memakai token, bukan hardcode rgba.
  - **Sublink soft pill**: radius 20px (cukup bulat tapi tetap readable), padding 10px 14px, text alpha 0.65 → aksen saat hover.
  - **CTA button**: pill 100px radius, oranye aksen → `#ffa726` hover, transform up 2px, shadow aksen 0.35 opacity.
  - **Icon (toggle & social)**: bulat 50% radius, aksen oranye saat hover.
  - **Anti-FOUC**: semua panel `.glass-mobile-submenu` di-server-render dengan `hidden`, JS melepas saat CSS aktif + accordion pertama dibuka.

- Link aktif (desktop & mobile) — class `.active` disetel **server-side** di frontmatter `Navbar.astro` via `Astro.url.pathname` + helper `isActive()` (exact `/` vs prefix-match `href + '/'`, trailing slash dinormalkan). No JS blink — HTML benar sejak first paint.

### 8.3 Preloader (`Preloader.astro`)

- Fullscreen overlay `z-index: 9999`, spinner.
- Menunggu **dua** gambar kritis (`hero-bg-image-6.webp` + `hero.jpg`) lalu 2× `requestAnimationFrame`, fallback hard **5 detik**.
- Selesai → dispatch event `preloader:done` yang memicu pemuatan script non-kritis.

### 8.4 Kartu Produk

- Carousel homepage: `.iot-ep-card` (gambar + tag kategori overlay + judul + deskripsi + "View Details" + panah), navigasi panah prev/next + dots.
- Katalog: `.product-card` via `ProductCard.astro`, grid 6 per halaman, pagination server-side (`?page=`).

### 8.5 Galeri Produk Detail

- `.product-gallery` — main slider + thumbnail + counter "1 / N" + panah; gambar di-disprotect (`oncontextmenu="return false"`).
- Data galeri dikirim via atribut `data-images` (JSON).

### 8.6 Form

- `.form-control`: radius `10px`, padding `18px 20px`, background putih di form terang; versi glass di footer (transparent + blur).
- Validasi client-side: `required` + `maxlength` (nama 100, email 254, subject 200, pesan 2000).
- Submit → `mailto:` link (subject/body ter-encode).

### 8.6b Contact Page (`src/pages/contact/index.astro`)

Pola **"hero konversi dua kolom: copy + form glass di first view"** — evolusi Sept 2026 (v1 split-panel card → v2 hero konversi → v3 form-in-hero → v4 overlay → v5 logo asli → **v6 glass navbar + peta + custom dropdown, final**):

> ⚠️ **v6 menggantikan v5**: form card pakai **formula glass yang sama dengan navbar** (`rgba(3,23,29,0.5)` + `blur(24px) saturate(180%)`); info kontak (Email/WhatsApp/Address) pindah ke **kolom kiri first view**; **peta Google Maps** ditambahkan sebagai section terpisah dengan alamat lengkap; dropdown "Saya tertarik pada" jadi **custom dropdown glass** (bukan `<select>` native).

**Layout utama (v6, final):**
- `.contact-hero-grid`: `1fr 480px` (≤1199: 420px; ≤991: 1 kolom) — kolom kiri: h2 44px (eyebrow badge DIHAPUS Sept 2026 — langsung mulai dari headline) → sub → brand strip → trust row → **info kontak** (horizontal kompak, in fold); kolom kanan: form glass.
- **Form glass navbar formula**: `.form-card` bg `rgba(3,23,29,0.5)` + `backdrop-filter: blur(24px) saturate(180%)` + border `rgba(255,255,255,0.12)` + radius 24px + shadow `0 12px 40px rgba(3,23,29,0.35)` — identik dengan `.glass-nav.scrolled` (custom.css 11553). `::before` garis highlight gradient di tepi atas.
- **Info kontak kolom kiri (v8 kompak)**: **horizontal** (flex row wrap, gap 12/24) — bukan vertikal — agar masuk fold 768px tinggi; item = icon box gelap 34px + label uppercase 11px + nilai 13.5px; Address link ke `#contact-map` (teks singkat "Kalisari, Pasar Rebo, Jakarta Timur" — detail lengkap di peta); margin-top 20px + padding-top 16px; brand strip margin-top 24px; trust margin/padding 20/16px (semua dipadatkan dari 28/24). Verifikasi: 1366×768 info top 642/bottom 696 ✓ in fold; 1280×800 sama ✓; mobile tetap row (compact).
- **Custom dropdown "Saya tertarik pada"** (`.custom-select`, **v2 sticky**): button glass (icon box oranye `fa-bullseye` 34px + value bold + caret SVG rotasi saat open) → panel portal ke `<body>` via JS (`position: fixed`) agar backdrop-filter bekerja — **pola sama dengan `.glass-dropdown` navbar** (custom.css 12066). Panel: bg `rgba(3,23,29,0.85)` + blur 30px saturate 160% + radius 16px; opsi = icon box 32px + judul bold + deskripsi kecil + checkmark oranye untuk terpilih; hover bg `rgba(255,152,0,0.14)`. A11y: `role="listbox"/"option"`, `aria-expanded`, `aria-selected`, Escape = close, klik-luar = close. Nilai disimpan di `<input type="hidden" name="subject">` (function.js tetap baca form). **v2 fix**: panel `position()` dipanggil ulang saat `scroll` (capture=true) & `resize`; **auto-close saat tombol keluar viewport** (atas/bawah — panel tidak melayang sendiri); clamp horizontal 12px + **flip ke atas** bila ruang bawah kurang; mobile ≤768 melebar full. **Init di `DOMContentLoaded`** (fallback `load` DILARANG — iframe Google Maps ERR_ABORTED bisa memblok `window load` tanpa batas sehingga dropdown mati).
- **Validasi form modern (inline + alert glass)**: form `novalidate` (validasi native bubble nonaktif). Handler submit capture berjalan SEBELUM handler mailto jQuery lama; bila invalid: `e.stopImmediatePropagation()` memblokir mailto, field diberi `.is-invalid` (border merah + shake, **TANPA teks error per-field — semua info cukup lewat alert bawah tombol**), fokus+scroll ke field pertama yang invalid, dan **banner alert glass** `.form-alert.form-alert-error` yang berisi **ringkasan error** (mis. "Nama wajib diisi · Format email tidak valid · Pesan wajib diisi", di-join dengan " · ", di-dedup via Set). Bila valid: banner hijau lalu **mailto dijalankan handler capture sendiri** (lihat §14.8). Email divalidasi regex; error dibersihkan tiap submit ulang; **validasi on-blur yang sopan** (field dikosongkan yang belum tersentuh tidak langsung dihukum; error alert hilang otomatis saat semua field valid kembali). Init via `astro:page-load` + fallback `DOMContentLoaded` (cold-load).
- **Slot alert tetap — anti layout-shift (Sept 2026)**: `#msgSubmit` = **slot `height: 84px` tetap** (≤480px: 116px) yang SELALU mencadangkan ruang di bawah tombol — tinggi card **tidak pernah berubah** saat alert muncul/hilang (verifikasi A/B: card 662px stabil di state bersih/error/tertutup/sukses). Alert `.form-alert` = `position: absolute; inset: 0` mengisi slot; `align-items: center`; success auto-dismiss 6s + progress bar; error persist sampai diperbaiki (on-blur `hideErrorAlert`) atau tombol close. **GOTCHA KRITIS Astro**: alert di-inject via `innerHTML` sehingga TIDAK punya `data-astro-cid` → semua selector scoped (`.form-alert` dll.) TIDAK pernah ter-apply (computed style menunjukkan `position: static`, `font-size: 16px`, `padding: 0` — style global `p` yang menang). **Solusi: bungkus SEMUA selector alert dengan `:global()`** di `<style>` halaman (class alert unik milik halaman ini, aman untuk global). Selalu verifikasi computed style elemen yang di-inject JS, bukan cuma markup.
- **Input modern (adaptasi "modern-form", Sept 2026)**: setiap input dibungkus `.input-wrap` (position relative) + `.input-icon` FontAwesome kiri (posisi absolute left 14px); input `.form-control` height 46px, padding-left 42px, radius 10px, bg `rgba(255,255,255,0.08)`, border `rgba(255,255,255,0.22)`; hover border lebih terang; focus = border aksen + **ring 4px `rgba(255,152,0,0.18)`** (tanpa outline dobel — rule `:focus-visible` lama DIHAPUS); textarea padding `13px 14px 13px 42px` (icon top 15px). **Valid live**: `:not(:placeholder-shown):not(.is-invalid):valid` → border hijau `rgba(74,222,128,0.5)` + ikon hijau (via `:has()` di wrapper). **Invalid**: border merah + bg merah tipis + glow 4px + ikon merah + shake. Dropdown custom menyusul gaya sama (height 46px, radius 10px, ring 4px).
- **Alert profesional (Sept 2026)**: struktur `#msgSubmit .form-alert` = **icon chip bulat 34px** (`.alert-icon`, bg tint + border) + `.alert-body` (strong + span) + **tombol close** (`.alert-close`, pojok kanan atas, hover bg putih 0.08) + **progress bar auto-dismiss 6 detik** (`.alert-progress`, hanya success, animasi scaleX kiri→kanan habis). Success **auto-dismiss 6s** + progress bar mengikuti; error **tetap sampai diperbaiki** — hilang otomatis saat semua field valid kembali (`hideErrorAlert()` dari on-blur) atau via tombol close. Animasi masuk `formAlertIn` (slide-down + scale 0.98→1, cubic-bezier spring), keluar `formAlertOut` via class `.is-leaving`.
- **Peta section** (`#contact-map`): `.contact-map-section` bg `--primary-color` padding 24/80; `.contact-map-card` glass (0.6 + blur 24px saturate 180% radius 24); `.map-head` = icon oranye 48px + judul "Kunjungi Kami" + alamat lengkap + tombol pill "Petunjuk Arah" (link Google Maps, hover jadi aksen); `.map-frame` height 360px (≤991: 320px, ≤768: 260px) radius 16px, iframe Google Maps embed (`?q=...&output=embed`) + `filter: grayscale(0.3) contrast(1.05)` agar serasi tema gelap; `loading="lazy"`.
- Alamat resmi: **Jalan Intisari Raya, RT.2/RW.9, Kalisari, Pasar Rebo, Kota Jakarta Timur, DKI Jakarta, ID 13780**.
- Brand chips tetap: putih solid + logo warna asli; headline/sub/trust tetap text-shadow foreground (tanpa overlay bg).
- Mobile ≤768: grid 1 kolom, form-row 1 kolom, submit full-width, brand chip 25%, map-frame 260px, tombol arah full-width.
- **Verifikasi v7 (Playwright)**: desktop — info in fold (top 674), form top 160, **formBlur `blur(24px) saturate(1.8)` ✓**, map 360px + iframe ✓, dropdown portal open→pilih "Kemitraan"→hidden input berubah→panel close ✓, hOverflow false; mobile — info top 642, form top 841, map 260px, hOverflow false. Screenshot `testsprite_tests/tmp/review7-{desktop-fold,mobile-fold,desktop-full}.jpg` (41–83KB).

**⚠️ GOTCHA KRITIS — backdrop-filter di scoped style Astro:**
Lightningcss (minifier default Astro) **menghapus properti standar `backdrop-filter`** jika ada duplikat `-webkit-backdrop-filter` di deklarasinya (menganggap prefix = duplikat). Hasil: rule ter-serve hanya `-webkit-` yang **tidak dikenali Chromium modern** → blur diam-diam mati (computed `backdrop-filter: none`). Navbar tidak kena karena CSS-nya di `public/css/` (tidak diproses). **Solusi: di scoped `<style>` Astro, tulis HANYA `backdrop-filter` standar tanpa prefix `-webkit-`.** Selalu verifikasi computed style, bukan cuma visual.

**Hero responsif (pola WAJIB untuk halaman intro):**
- Inline style di markup **dilarang** untuk padding/min-height — dipindah ke `<style>` di class `.hero.contact-hero` (specificity `(0,2,0)` menang atas `.hero` global `(0,1,0)`).
- Latar belakang hero **harus** di-set lewat CSS (bukan inline) supaya bisa dioverride breakpoint.

**Form & info card mobile (≤768px):**
- (v6) Lihat bagian "Layout utama (v6)" di atas — aturan mobile form terkini ada di sana.
- Aturan global tetap berlaku: input `font-size: 16px` **wajib** (cegah auto-zoom iOS saat focus); focus ring `:focus-visible` outline aksen; atribut a11y di markup: `autocomplete` (name/email/tel), `inputmode` (email/tel), `spellcheck="true"` pada textarea.

**Submit button (adaptasi "modern-form", Sept 2026):**
- `.contact-submit` **bukan lagi** `.btn-default.btn-highlighted` — tombol modern mandiri: height 52px, radius 10px, bg aksen, ikon `fa-paper-plane` + label, `overflow: hidden`; child `.button-glow` (gradient putih transparan, `translateX(-100%)` → hover `translateX(100%)`, sweep 0.6s); hover = lift `translateY(-1px)` + shadow oranye `0 8px 20px rgba(255,152,0,0.35)`; active = turun kembali. `:focus-visible` outline putih offset 2.

**Mailto (§14.8 — fix bug tersembunyi, Sept 2026):**
- Handler mailto jQuery lama di `function.js` membaca `$("#subject").val().trim()` padahal hidden input custom-select hanya punya `name="subject"` **tanpa `id="subject"`** → `TypeError: reading 'trim'` → **mailto tidak pernah benar-benar jalan** (error diam-diam di console). Fix: handler capture di `contact/index.astro` kini **menjalankan mailto sendiri** (baca `input[name="subject"]`, buka `mailto:` window, `form.reset()`, kembalikan label custom-select manual karena `reset()` tidak menyentuh teks label) lalu `stopImmediatePropagation()` memblokir handler lama. Handler lama di `function.js` TIDAK diubah (prinsip minim sentuhan file global).

### 8.6c About Page (`src/pages/about/index.astro`)

Di-refactor Agustus 2026 (mobile UX audit 380px) — pola sama dengan contact: **inline styles anti-responsif tidak boleh dipakai untuk ukuran/padding kritis**:

**Hero (`.hero.about-hero`):**
- Inline `background-image` + sub-teks `font-size: 1.1em` dipindah ke CSS scoped.
- **Bug hierarki**: sub-teks inline `1.1em` (17.6px) LEBIH BESAR dari judul h2 global mobile 20px. Fix: `.about-hero .section-title h2` = 30px (≤768px) / 26px (≤480px); `.about-hero-sub` = 1.05em desktop → 1em mobile.
- `.hero.about-hero` (0,2,0): padding 120/64 desktop, 96/48 mobile; min-height 340px → 280px mobile.

**Grid & spacing mobile:**
- Stat "By The Numbers": tambah `col-6` (2×2 mobile) — sebelumnya `col-xl-3 col-md-6` tanpa col-6 → 4 kartu full-width bertumpuk (page 12638px). Sekarang `col-6 col-md-6 col-xl-3` → 12005px.
- Stat card: `.stat-item` padding `24px 16px` (mobile, override inline 40px 20px), `.stat-number` 2.4rem → 2rem (480px), label 0.9rem.
- Team images: inline `height: 280px` pindah ke `.about-team-img` (280px) → **200px di ≤768px** (crop cover tidak agresif di layar sempit).
- CTA `.about-us-btn .btn-default` & `.how-it-work-btn .btn-default`: `width: 100%` di ≤768px (thumb-reach).

**Rule mau-diingat**: `!important` kadang perlu karena `.stat-item` bersaing dengan `.feature-item` (specificity scoped `(0,2,0)` sebenarnya sudah menang — dipakai defensif).

### 8.7 Ikon

- **Font Awesome 7** (`fa-solid`, `fa-brands`) — ikon kontak, sosial, ceklis list (`\f058`).
- **Inline SVG** stroke 2–2.5px — panah, ikon menu mobile, gallery arrows.
- Gambar ikon kustom — `icon-box` 50–60px dengan radius `8–10px`, background aksen, hover mengisi primary (animasi scale/rotate dari pojok).

---

## 9. Motion

| Elemen | Library | Pola |
|--------|---------|------|
| Split text heading | GSAP + SplitText | `.text-anime-style-3` |
| Scroll reveal | WOW.js (`wow fadeInUp`, `data-wow-delay`) | delay umum `0.2s` / `0.4s` |
| Parallax/scroll effects | ScrollTrigger | section homepage |
| Carousel produk | Custom JS (scroll-snap style) | homepage |
| Counter angka | jquery.counterup + waypoints | statistik |
| Smooth scroll | SmoothScroll.js | global |
| Custom cursor | magiccursor.js + `mousecursor.css` | `data-cursor="-opaque"` pada judul |
| Preloader exit | opacity/visibility `0.3s ease` | global |
| Transisi antar halaman | Astro `ClientRouter` + prefetch hover | client-side swap (lihat §14) |

**Prinsip**: animasi hanya pada enter/interaksi; durasi pendek (0.3–0.4s); easing `ease-in-out`; tidak ada animasi loop berat selain dekorasi CTA kecil. Semua init JS wajib via event `astro:page-load` (bukan `DOMContentLoaded`) — lihat §14.

---

## 10. Breakpoints

| Breakpoint | Kondisi |
|------------|---------|
| `≤1880px` | `.bg-section` menyempit (`calc(100% - 40px)`) |
| `≤1580px`, `≤1525px`, `≤1440px`, `≤1325px` | Penyesuaian hero/header/konten |
| `≤1024px` | Grid mengecil (3→2 kolom), padding turun |
| `≤991px` | **Breakpoint utama mobile**: navbar jadi hamburger, section padding `50px`, radius section hilang, grid 2→1 |
| `≤767px` | Grid satu kolom penuh, heading mengecil drastis |
| `≤480px` | Penyesuaian akhir kecil |
| `(hover: none) and (pointer: coarse)` | Penonaktifan efek hover di perangkat sentuh |

Grid layout memakai **Bootstrap 5** (container, row, col-*).

---

## 11. Aset Gambar

| Jenis | Lokasi | Format |
|-------|--------|--------|
| Foto produk | `src/assets/products/*` | jpg/png (dioptimasi Astro Image) |
| Aset stack/teknologi | `src/assets/stack/*` | — |
| Ikon & sprite | `public/images/*` | svg/png |
| Hero & background | `public/images/hero.jpg`, `hero-bg-image-6.webp` | webp preferred |
| Font | `public/fonts/inter-tight-*.woff2` | woff2 |

Aturan:
- Gambar konten utama hero: preload + `fetchpriority="high"`.
- Gambar di bawah lipatan: `loading="lazy"`.
- Format preferensi: **WebP** untuk foto besar.

---

## 12. Do & Don't

### ✅ Do

- Pakai CSS variable (`var(--accent-color)`) — jangan hardcode warna.
- Ikuti pola section shell (`.bg-section` + `.section-title` + `wow fadeInUp`).
- Radius konsisten: 10 / 14 / 20 / 100.
- Teks di section gelap selalu putih; teks di atas aksen selalu primary.
- Form wajib punya `maxlength` dan label eksplisit.
- Link internal pakai path absolut (`/products`, `/contact`) — bukan anchor `#` lintas halaman.

### ❌ Don't

- Jangan menambah CDN eksternal (font/script) — melanggar CSP `default-src 'self'`.
- Jangan menambah warna baru di luar token tanpa diskusi.
- Jangan pakai `box-shadow` besar sebagai depth — gunakan blur glass / border alpha.
- Jangan mem-bypass preloader event (`preloader:done`) dengan script blocking.
- Jangan hardcode heading scale baru di luar type scale tabel 3.3.

---

## 13. Keamanan Visual-adjacent

| Header | Nilai |
|--------|-------|
| `Content-Security-Policy` | `default-src 'self'; script-src 'self' 'unsafe-inline' 'wasm-unsafe-eval' https://www.youtube.com https://www.youtube-nocookie.com; style-src 'self' 'unsafe-inline'; font-src 'self' data:; img-src 'self' data: blob: https:; media-src 'self' blob:; frame-src https://www.youtube.com https://www.youtube-nocookie.com; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'; connect-src 'self'` |
| `X-Frame-Options` | `DENY` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=()` |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |
| `Cross-Origin-Opener-Policy` | `same-origin` |

Catatan CSP:
- `'unsafe-inline'` pada `script-src` tetap diperlukan (Astro inline island script + preloader bootstrap). `'unsafe-eval'` sudah dihapus.
- YouTube embed diizinkan eksplisit (`script-src`, `frame-src`).
- Tidak ada CDN pihak ketiga selain YouTube — font & asset semuanya self-hosted.

Dikelola terpusat di `src/middleware.ts` (objek `SECURITY_HEADERS`) — jangan set header serupa di tempat lain.

---

## 14. Navigasi & View Transitions (ClientRouter)

Perpindahan halaman memakai **Astro View Transitions** (`<ClientRouter />`) sehingga navbar tidak pernah "reload" — DOM di-swap dalam dokumen yang sama. Preloader hanya muncul di kunjungan pertama.

### 14.1 Konfigurasi

| Item | Lokasi | Nilai |
|------|--------|-------|
| Router | `src/layouts/MainLayout.astro` | `<ClientRouter />` sebagai elemen pertama `<head>` |
| Prefetch | `astro.config.mjs` | `prefetch: { prefetchAll: false, defaultStrategy: 'hover' }` |
| Guard loader berat | `MainLayout.astro` | `window.__iotaruHeavyLoaded` — cegah double-load GSAP/Swiper/loop skrip berat saat swap |
| Flag page-load lewat | `MainLayout.astro` | `window.__iotaruPageLoadFired` — ditandai oleh listener `astro:page-load`; dipakai `function.js` sebagai fallback init (lihat §14.6) |

### 14.2 Pola init script (WAJIB)

Semua `<script>` komponen/halaman **tidak boleh** memakai `DOMContentLoaded` atau memanggil init secara langsung di top-level. Gunakan:

```js
function initSomething() { /* ... */ }
document.addEventListener('astro:page-load', initSomething);
```

`astro:page-load` fire saat load pertama **dan** setelah tiap navigasi client-side — satu hook untuk keduanya. Yang sudah dimigrasi: `Navbar`, `ProductCarousel`, `Footer`, `Preloader`, `products/index` (`initProductFilters`), `products/[slug]` (`initGallery`), `public/js/function.js` (`initSite`), `public/js/magiccursor.js` (`initCursor`).

**PENTING — timing event vs script berat:** `astro:page-load` pada kunjungan pertama fire saat event `window load`, sedangkan `function.js` baru dieksekusi SETELAH preloader selesai (bisa jauh setelahnya, apalagi di jaringan lambat). Listener yang didaftarkan di dalam `function.js` terlambat dan **tidak akan pernah ter-panggil** pada kunjungan pertama. Solusinya lihat §14.6 (fallback flag `__iotaruPageLoadFired`).

### 14.3 Pola teardown & dedupe listener

- **Teardown di awal init** (`function.js → initSite`): `ScrollTrigger.getAll().forEach(t => t.kill())`, destroy semua swiper di registry `window.__iotaruSwipers`, `window.__iotaruWow.reset()`.
- **Registry window untuk listener global** (karena `document` persist lintas swap, listener bisa menumpuk):
  - `window.__galleryKeydown`, `window.__galleryLightboxKeydown`, `window.__galleryPopstate` — pola `removeEventListener → addEventListener` di `products/[slug]`.
  - `window.__iotaruStickyBound`, `window.__iotaruTopBound` — guard bind-sekali di `function.js`.
  - `window.__iotaruCursor` — instance cursor; `<body>` sepenuhnya diganti saat swap sehingga `.cb-cursor` + listener-nya hilang; `astro:after-swap` memanggil `initCursor()` ulang (hapus sisa `.cb-cursor` dulu agar tidak duplikat).
- **Interval autoplay galeri** disimpan di `window.__galleryAutoplay` dan di-`clearInterval` di awal `initGallery`.

### 14.4 Preloader & swap

- Root preloader: `<div class="preloader" id="preloader" transition:persist="preloader">` — bertahan lintas swap sehingga kunjungan pertama tetap memakai preloader.
- `astro:after-swap` di `Preloader.astro` **force-dismiss** (`display:none` + `window.__preloaderDone = true`) agar preloader tidak mengunci navigasi client-side berikutnya; gate `preloader:done` untuk loader berat tetap jalan normal di kunjungan pertama.

### 14.6 Cold-load race guard & fallback init (WAJIB dipertahankan)

Bug historis (Juli 2026): pada **kunjungan pertama dengan cache dingin** (terutama mobile/jaringan lambat), teks & gambar tidak muncul karena animasi WOW tidak pernah jalan. Dua akar masalah:

1. **Race double-start loader**: listener `preloader:done` DAN fallback `window load` bisa ter-fire hampir bersamaan → dua rantai `loadScriptsSequentially` paralel → semua script berat dimuat 2× → `magiccursor.js` crash (`Identifier 'Cursor' has already been declared`, deklarasi top-level bentrok).
2. **`initSite()` tidak pernah jalan**: `astro:page-load` fire saat `window load` (~2,5–4s) tetapi `function.js` baru dieksekusi setelah preloader (~5,7s) → listener `astro:page-load` yang didaftarkannya terlambat → WOW tidak pernah init → semua `.wow` tetap `visibility: hidden` (dari `critical.css`).

Pola perbaikan (jangan dihapus):

```js
// MainLayout.astro — guard race di startLoad:
var loadStarted = false;
function startLoad() {
  if (loadStarted) return; // {once:true} hanya per-event-type, BUKAN global!
  loadStarted = true;
  loadScriptsSequentially(nonCritical, 0);
}

// MainLayout.astro — tandai bahwa astro:page-load sudah lewat:
document.addEventListener('astro:page-load', function () {
  window.__iotaruPageLoadFired = true;
});

// function.js — fallback init manual jika script dieksekusi setelah event:
// GUARD __iotaruInitDone WAJIB (Sept 2026): loader MainLayout kini memanggil
// initSite() langsung di akhir rantai script (fix WOW di halaman non-home) —
// tanpa guard, astro:page-load berikutnya double-init di halaman yang sama.
// RESET di astro:after-swap JUGA WAJIB (bug v13): tanpa reset, guard memblok
// init halaman KEDUA dst saat navigasi View Transitions (WOW mati lagi).
document.addEventListener('astro:page-load', function () {
  if (window.__iotaruInitDone) return;
  window.__iotaruInitDone = true;
  initSite();
});
if (window.__iotaruPageLoadFired && !window.__iotaruInitDone) {
  window.__iotaruInitDone = true;
  initSite();
}
window.__iotaruInitSite = initSite;

// MainLayout.astro — reset guard tiap swap (DOM halaman baru butuh init baru):
document.addEventListener('astro:after-swap', function () {
  window.__iotaruInitDone = false;
});
```

**Bug WOW non-home (Sept 2026, WAJIB dipertahankan)**: Preloader hanya ada di **homepage**. Di semua halaman lain, event `preloader:done` tidak pernah fire dan `window load` bisa stuck (iframe Google Maps `ERR_ABORTED`) → `function.js` tidak pernah dimuat → **WOW & semua animasi mati di seluruh halaman non-home**. Fix di MainLayout loader:

```js
// Fallback ketiga: halaman tanpa #preloader → preloader:done tak akan fire;
// window load bisa stuck → pakai DOMContentLoaded + delay singkat.
if (!document.getElementById("preloader")) {
  if (document.readyState !== "loading") {
    setTimeout(startLoad, 100);
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(startLoad, 100);
    }, { once: true });
  }
}

// Dan di akhir loadScriptsSequentially (index >= scripts.length):
// panggil initSite manual — loader tahu tepat kapan semua script siap.
setTimeout(function () {
  if (typeof window.__iotaruInitSite === "function" && !window.__iotaruInitDone) {
    window.__iotaruInitDone = true;
    window.__iotaruInitSite();
  }
}, 0);
```

Aturan terkait:

- **Preloader** harus set `window.__preloaderDone = true` SEBELUM dispatch `preloader:done` (agar loader yang cek flag sinkron tidak ketinggalan).
- **Indikator "animated" WOW**: config memakai `resetAnimation: true` (class `animated` dihapus setelah animasi selesai) → jumlah `.wow.animated` BUKAN indikator valid. Cek inline style `animation-name` ≠ none + `visibility: visible`.
- Elemen `.wow` yang masih hidden di bawah viewport itu **normal** (WOW lazy — dianimasikan saat di-scroll).

**Verifikasi cold-load** (Playwright + CDP):

```js
const client = await page.context().newCDPSession(page);
await client.send('Network.setCacheDisabled', { cacheDisabled: true });
await client.send('Network.emulateNetworkConditions', {
  offline: false, latency: 150,
  downloadThroughput: (1.6 * 1024 * 1024) / 8, // 3G-ish
  uploadThroughput: (750 * 1024) / 8,
});
// goto → evaluate: window.__iotaruWow ada, fjsCount === 1,
// zero pageerror, semua .wow punya animation-name / di bawah viewport
```

Selalu reset kondisi CDP (`cacheDisabled: false`, throughput `-1`) setelah tes.

### 14.7 Verifikasi View Transitions (Playwright, Agustus 2026)

- Rangkaian `/ → /about → /blog → /products → / → /products/smart-cam`: `performance.getEntriesByType('navigation')` tetap **1** (tidak ada full reload), active link navbar benar di tiap halaman, cursor tetap 1 instance, dropdown portal navbar tetap ter-render setelah swap.
- Filter pill `/products` (collapse/expand "Lainnya") dan galeri autoplay + tombol next di detail produk berfungsi setelah swap.
- Catatan perilaku trigger dropdown: klik link Solutions/Products di desktop **langsung navigasi** ke halaman induk; dropdown dibuka via **hover/fokus** (desktop) atau **tap** (perangkat sentuh, dideteksi via `matchMedia('(hover: hover)')` — guard juga diterapkan pada handler `focus` agar tap tidak bentrok dengan click-toggle).

### 14.8 Contact form v14 — UI modern-form + mailto fix (Sept 2026)

- **Sumber desain**: CSS "modern-form" dari user (light theme) → diadaptasi ke tema gelap IOTARU (aksen oranye, glass) tanpa mengubah warna brand.
- **Adaptasi**: ikon kiri input (FontAwesome, absolute left 14px, padding-left 42px), height 46px + radius 10px, focus ring 4px `rgba(255,152,0,0.18)` (outline `:focus-visible` dobel dihapus), hover border lebih terang; valid live hijau `rgba(74,222,128,0.5)` + ikon hijau via `:has()`; invalid merah + shake 0.35s sekali (retrigger via reflow); textarea + custom-select menyusul gaya sama.
- **Tombol**: `.contact-submit` mandiri (bukan `.btn-default`) height 52px radius 10px + ikon `fa-paper-plane` + `.button-glow` sweep hover + lift/shadow oranye.
- **Alert profesional**: icon chip bulat 34px + `.alert-body` + tombol close + `.alert-progress` (hanya success). Success auto-dismiss 6s; error persist — hilang otomatis saat semua field valid kembali (on-blur `hideErrorAlert`) atau via close. Keluar via `.is-leaving` + `formAlertOut`.
- **GOTCHA mailto tersembunyi (fix)**: handler jQuery lama (`function.js` ~356) membaca `$("#subject").val().trim()` padahal hidden input hanya punya `name` tanpa `id="subject"` → `TypeError` diam-diam → **mailto tidak pernah jalan**. Fix di handler capture `contact/index.astro` saja (function.js tak disentuh): jalankan mailto sendiri (subject dari `input[name="subject"]`), `form.reset()`, reset label custom-select manual, `stopImmediatePropagation()` blok handler lama.
- **Gotcha testing**: klik locator Playwright bisa gagal "intercepts pointer events" padahal `elementsFromPoint` bersih (artefak animasi shake) → uji via `dispatchEvent` koordinat/in-page; opsi goto = `waitUntil` (camelCase); tab background men-throttle `setTimeout` (auto-dismiss terlihat gagal padahal jalan) → polling in-page untuk pengujian timer.
- Verifikasi (Playwright 1366×768): submit kosong → banner error + 3 field error + focus `#name` ✓; email invalid → shake + ikon merah ✓; email diperbaiki → hijau + err hilang ✓; submit valid → success + progress + form reset + mailto tanpa pageerror ✓; close button ✓; auto-dismiss ✓. Screenshot `testsprite_tests/tmp/review10-{form,error,valid,success2}.jpg`.

---

*Dibuat otomatis dari audit kode — Juli 2026. Perbarui dokumen ini saat token/arsitektur berubah.*
