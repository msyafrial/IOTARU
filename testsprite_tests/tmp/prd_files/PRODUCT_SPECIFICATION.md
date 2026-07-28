# IOTARU — Product Specification

> **IOTARU Teknologi Nusantara** — Integrated IoT Solutions for Smart Security & Monitoring

---

## 1. Product Overview

IOTARU is a comprehensive IoT platform that provides end-to-end solutions for smart security, monitoring, and automation. The platform connects hardware devices, edge gateways, and cloud services into a unified ecosystem for residential, commercial, and industrial deployments.

### 1.1 Mission

Deliver reliable, secure, and scalable IoT solutions that turn real-time data into smarter security, monitoring, and automation — built with local expertise for global standards.

### 1.2 Core Value Propositions

| Value | Description |
|-------|-------------|
| **End-to-End IoT Solution** | Hardware, firmware, connectivity, cloud, and dashboard — all from one provider |
| **Security-First Architecture** | TPM 2.0, secure boot, encrypted communication, and CSP-protected web platform |
| **Custom & Scalable** | Modular product line that scales from single-device to 500+ device deployments |
| **Local Expertise** | Indonesian-based engineering team with global technology partnerships |

---

## 2. Target Market

### 2.1 Market Segments

| Segment | Description |
|---------|-------------|
| **Smart Home** | Homeowners seeking security, comfort, and energy management |
| **Smart Office** | Corporate offices, co-working spaces, facilities management |
| **Smart City** | Municipal infrastructure, parking, lighting, environmental monitoring |
| **Industrial** | Manufacturing, energy, agriculture, and logistics operations |

### 2.2 Ideal Customers

- Homeowners modernizing their living space
- Families wanting better security and convenience
- Corporate offices optimizing energy and space usage
- Facilities managers reducing operational costs
- Municipalities deploying city-wide IoT infrastructure
- Industries requiring real-time monitoring and automation

---

## 3. Product Architecture

### 3.1 System Layers

```
┌─────────────────────────────────────────────────┐
│                  Cloud Platform                  │
│   Dashboard · API · Analytics · OTA Updates      │
├─────────────────────────────────────────────────┤
│               Connectivity Layer                 │
│   MQTT · LoRa · Zigbee · BLE · Wi-Fi · LTE      │
├─────────────────────────────────────────────────┤
│                Edge Gateway Layer                 │
│   Smart Hub · Smart Gateway · Mesh Gateway       │
├─────────────────────────────────────────────────┤
│               Device Layer                       │
│   Sensors · Cameras · Locks · Lights · Plugs     │
└─────────────────────────────────────────────────┘
```

### 3.2 Technology Stack

#### Hardware
| Technology | Purpose |
|------------|---------|
| STM32 Series | Industrial-grade microcontrollers for reliable systems |
| ESP32 | High-performance edge devices for IoT operations |
| Nordic nRF Series | Low-power wireless SoC for BLE and RF communication |
| Ebyte Modules | LoRa, Wi-Fi, BLE, and ZigBee wireless modules |
| SIMCom Modules | 5G, 4G, LPWA, and GNSS cellular connectivity |

#### Software & Protocols
| Technology | Purpose |
|------------|---------|
| FreeRTOS | Real-time operating system for stable multitasking |
| MQTT Protocol | Lightweight, secure data communication |
| Modbus RTU/TCP | Industrial protocol for field device integration |
| LoRa/LoRaWAN | Long-range, low-power wide-area connectivity |
| Bluetooth Low Energy | Short-range wireless for provisioning and control |
| Microservices Backend | Scalable data processing and device management |

#### Security
| Feature | Implementation |
|---------|---------------|
| TPM 2.0 | Hardware security module with tamper detection |
| Secure Boot | Verified firmware chain of trust |
| OTA Updates | Encrypted over-the-air firmware updates |
| CSP Headers | Content Security Policy on web platform |
| HSTS | HTTP Strict Transport Security enforcement |

---

## 4. Product Catalog

### 4.1 Product Categories

| Category | Products | Description |
|----------|----------|-------------|
| **Automation** | Smart Hub Pro, Smart Gateway, Smart Mesh Gateway, Smart Relay Gateway, Smart LoRa Gateway | Central control and connectivity hubs |
| **Security** | Smart Camera, Smart Lock, Smart Doorbell, Smart Alarm, Smart Guard, Smart Access | Surveillance, access control, and alarm systems |
| **Monitoring** | Smart Sensor Hub, Smart Air Quality, Smart Weather, Smart Energy, Smart Meter, Energy Monitor | Environmental and energy monitoring |
| **Smart Home** | Smart Light, Smart Plug, Smart Curtain, Smart Thermostat, Smart Display, Smart Speaker | Home automation and comfort devices |
| **Infrastructure** | Smart Battery, Smart Button, Smart EV Charger, Smart Solar, Smart Irrigation, Smart Parking | Specialized infrastructure solutions |

### 4.2 Featured Products

#### IOTARU Smart Hub Pro
- **Category:** Automation
- **Description:** Professional-grade IoT hub with redundant connectivity and enterprise security
- **Connectivity:** Dual LTE + Gigabit Ethernet
- **Device Support:** Up to 500 devices
- **Processor:** Quad-core ARM Cortex-A72
- **Memory:** 4GB RAM / 64GB NVMe
- **Security:** TPM 2.0 / Secure Boot

#### IOTARU Smart Camera
- **Category:** Security
- **Description:** AI-powered security camera with night vision and real-time alerts
- **Resolution:** 4K Ultra HD (3840x2160)
- **Night Vision:** 30m Infrared
- **Connectivity:** Wi-Fi 6 / Ethernet
- **Storage:** Cloud + MicroSD (256GB)
- **Power:** PoE / 12V DC

#### IOTARU Smart Sensor Hub
- **Category:** Monitoring
- **Description:** Multi-purpose sensor hub for environmental monitoring
- **Sensors:** Temperature, Humidity, VOC, PM2.5, Motion
- **Range:** 50m indoor / 100m outdoor
- **Connectivity:** Zigbee 3.0 / Wi-Fi
- **Battery:** 2x AA (2-year lifespan)
- **Dimensions:** 70 x 70 x 25mm

---

## 5. Solutions

### 5.1 Smart Home

Complete IoT ecosystem for modern connected homes — automate lighting, security, climate, and energy management from a single platform.

**Included Components:**
- Central Hub (Zigbee, Z-Wave, BLE, Wi-Fi)
- Smart Sensors (motion, door/window, temperature, humidity, air quality)
- Smart Locks (biometric and app-controlled)
- Smart Lighting (automated scenes, scheduling, ambient control)
- Energy Monitor (real-time consumption tracking, anomaly alerts)

**Key Benefits:**
| Benefit | Impact |
|---------|--------|
| Unified Control | Manage all devices from one mobile app |
| Energy Savings | Reduce electricity bills by up to 30% |
| Security First | 24/7 monitoring with instant push notifications |
| Voice Ready | Works with Google Assistant, Alexa, Siri |
| Offline Capable | Local automation without internet |

### 5.2 Smart Office

Intelligent workplace management with occupancy sensing, energy optimization, and employee safety monitoring.

**Included Components:**
- Occupancy Sensors (desk and room utilization)
- Climate Control (automated HVAC management)
- Smart Lighting (daylight-adaptive, occupancy-based)
- Air Quality Monitor (CO2, PM2.5, VOC, temperature)
- Access Control (badge-based entry, visitor management)

**Key Benefits:**
| Benefit | Impact |
|---------|--------|
| Cost Reduction | Cut energy costs by 25-40% |
| Space Optimization | Data-driven room and desk utilization insights |
| Employee Safety | Real-time air quality alerts |
| Compliance | Automated health and safety logging |
| Analytics Dashboard | Visual reports on space, energy, and environment |

### 5.3 Smart City

Comprehensive urban IoT infrastructure for monitoring, managing, and optimizing city services.

**Key Capabilities:**
- Environmental monitoring (air quality, noise, weather)
- Smart parking and traffic management
- Public safety and surveillance
- Energy-efficient street lighting
- Waste management optimization
- Water quality monitoring

---

## 6. Web Platform

### 6.1 Technology

| Component | Technology |
|-----------|-----------|
| Framework | Astro 7.0.3 |
| Language | TypeScript 6.0 |
| Content | MDX (Markdown + JSX) |
| Adapter | @astrojs/node (standalone) |
| Styling | Custom CSS + Bootstrap |
| Animations | GSAP, ScrollTrigger, SplitText |
| Search Engine | Sitemap integration |

### 6.2 Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Hero, product carousel, technology stack, about, features, CTA, FAQ |
| Products | `/products/` | Searchable, filterable product catalog with pagination |
| Product Detail | `/products/[slug]` | Individual product specifications and details |
| Solutions | `/solutions/` | Solution overview with hero and solution cards |
| Solution Detail | `/solutions/[slug]` | Individual solution details and benefits |
| Blog | `/blog/` | Technical articles and IoT guides |
| Blog Post | `/blog/[slug]` | Individual blog articles |
| Contact | `/contact/` | Contact form with mailto integration |
| 404 | `/404` | Custom error page |

### 6.3 Features

- **Preloader:** Custom loading animation with hero background detection
- **Glass Navbar:** Floating glass-morphism navigation with scroll effects
- **Mobile Menu:** Slide-in menu with backdrop blur and stagger animations
- **Product Carousel:** Horizontal scrolling product showcase with navigation
- **Product Search:** Full-text search with category filtering
- **Responsive Design:** Mobile-first responsive layout
- **Critical CSS:** Inlined above-the-fold styles for fast first paint
- **Self-Hosted Fonts:** Inter Tight variable font (no external CDN)
- **Security Headers:** CSP, HSTS, X-Frame-Options, and more

### 6.4 Performance Optimizations

| Optimization | Implementation |
|-------------|---------------|
| Critical CSS | Inlined above-the-fold styles (~15KB) |
| Async CSS | Non-critical CSS loaded via media="print" pattern |
| Image Optimization | WebP format, lazy loading, Astro Image component |
| Script Bundling | Deferred script loading, no render-blocking |
| Font Loading | Self-hosted woff2 with font-display: swap |
| Hero Priority | Eager loading with fetchpriority="high" |
| Preloader | Dismisses on hero background ready (not window.load) |
| Bootstrap Grid | Critical grid rules inlined to prevent layout shift |

### 6.5 Security

| Header | Value |
|--------|-------|
| Content-Security-Policy | default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; font-src 'self' data:; img-src 'self' data: https:; frame-src https://www.youtube.com |
| X-Frame-Options | DENY |
| X-Content-Type-Options | nosniff |
| Referrer-Policy | strict-origin-when-cross-origin |
| Permissions-Policy | camera=(), microphone=(), geolocation=(), payment=() |
| Strict-Transport-Security | max-age=31536000; includeSubDomains |

---

## 7. Content Collections

### 7.1 Blog

Technical articles and IoT guides for knowledge sharing and SEO.

| Article | Tags |
|---------|------|
| Getting Started with IoT | IoT, beginner, setup |
| IoT Security Best Practices | Security, encryption, authentication |
| Smart Home Guide | Smart Home, automation, setup |

### 7.2 Products

31 product entries across 5 categories with MDX content including features, specifications, and images.

### 7.3 Solutions

3 solution entries (Smart Home, Smart Office, Smart City) with detailed descriptions, components, and benefits.

---

## 8. Deployment

### 8.1 Build

```bash
npm run build    # Production build to ./dist/
npm run preview  # Preview build locally
```

### 8.2 Runtime

- **Node.js:** >= 22.12.0
- **Adapter:** @astrojs/node (standalone)
- **Output:** Server-side rendered (SSR) + static prerendering
- **Site URL:** https://iotaru.com

### 8.3 Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| HOST | 127.0.0.1 | Server host |
| PORT | 4321 | Server port |
| NODE_ENV | production | Environment mode |

---

## 9. Analytics & Monitoring

### 9.1 Performance Metrics

| Metric | Target |
|--------|--------|
| First Contentful Paint | < 1.5s |
| Largest Contentful Paint | < 2.5s |
| Total Blocking Time | < 300ms |
| Cumulative Layout Shift | < 0.1 |
| Time to Interactive | < 3.0s |

### 9.2 SEO

- Canonical URLs via `Astro.url` and `Astro.site`
- Open Graph meta tags (og:title, og:description, og:image)
- Twitter Card meta tags
- Auto-generated sitemap (`sitemap-index.xml` + `sitemap-0.xml`)
- Semantic HTML structure

---

## 10. Roadmap

### 10.1 Completed

- [x] Product catalog with 31 products and search/filter
- [x] Solutions pages (Smart Home, Smart Office, Smart City)
- [x] Blog with MDX content
- [x] Glass-morphism navbar with mobile menu
- [x] Critical CSS optimization
- [x] Self-hosted Google Fonts
- [x] Security headers and CSP
- [x] Responsive design (mobile-first)
- [x] Product pagination
- [x] Custom 404 page
- [x] Sitemap generation

### 10.2 Planned

- [ ] User authentication and dashboard
- [ ] Real-time device monitoring dashboard
- [ ] Contact form backend integration
- [ ] Newsletter subscription
- [ ] Multi-language support (ID/EN)
- [ ] Dark mode toggle
- [ ] Product comparison tool
- [ ] Live chat integration
- [ ] Analytics dashboard
- [ ] API documentation

---

*Document generated for IOTARU Teknologi Nusantara*
*Version: 1.0 | Date: July 2026*
