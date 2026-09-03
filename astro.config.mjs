// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import node from '@astrojs/node';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  adapter: node({ mode: 'standalone' }),
  integrations: [
    mdx(),
    sitemap(),
  ],
  // Prefetch saat hover: halaman tujuan di-download di background sehingga
  // navigasi View Transitions terasa instan.
  prefetch: { prefetchAll: false, defaultStrategy: 'hover' },
  site: 'https://iotaru.com',
});