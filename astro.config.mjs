// @ts-check
import { defineConfig, passthroughImageService } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';
import node from '@astrojs/node';

// Dual-target: Cloudflare Workers / Pages vs Node.js Standalone (Docker / VPS).
// Otomatis aktif saat DEPLOY_TARGET='cloudflare' atau saat berjalan di Cloudflare build (CF_PAGES).
const isCloudflare =
  process.env.DEPLOY_TARGET?.trim().toLowerCase() === 'cloudflare' ||
  Boolean(process.env.CF_PAGES);

// https://astro.build/config
export default defineConfig({
  adapter: isCloudflare
    ? cloudflare({
        imageService: 'passthrough',
      })
    : node({ mode: 'standalone' }),
  image: {
    service: passthroughImageService(),
  },
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !page.includes('/error') && !page.includes('/404'),
    }),
  ],
  // Prefetch saat hover: halaman tujuan di-download di background sehingga
  // navigasi View Transitions terasa instan.
  prefetch: { prefetchAll: false, defaultStrategy: 'hover' },
  site: 'https://iotaru.com',
});