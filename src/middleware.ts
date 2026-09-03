import { defineMiddleware } from 'astro:middleware';

/**
 * Security headers applied to every response.
 *
 * CSP notes:
 * - 'unsafe-inline' is still required for scripts because Astro inlines small
 *   island scripts and the preloader/loader bootstrap use inline <script>.
 *   (A nonce-based CSP would require rendering every script tag through the
 *   middleware, which is not practical for static/prerendered pages.)
 * - 'unsafe-eval' has been removed; nothing in the bundle needs it.
 * - WASM is allowed via 'wasm-unsafe-eval' for libraries that may need it.
 */
const SECURITY_HEADERS: Record<string, string> = {
  'X-Frame-Options': 'DENY',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), payment=()',
  'X-XSS-Protection': '1; mode=block',
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
  'Cross-Origin-Opener-Policy': 'same-origin',
  'Content-Security-Policy': [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' 'wasm-unsafe-eval' https://www.youtube.com https://www.youtube-nocookie.com",
    "style-src 'self' 'unsafe-inline'",
    "font-src 'self' data:",
    "img-src 'self' data: blob: https:",
    "media-src 'self' blob:",
    "frame-src https://www.youtube.com https://www.youtube-nocookie.com",
    "frame-ancestors 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "object-src 'none'",
    "connect-src 'self'",
  ].join('; '),
};

export const onRequest = defineMiddleware((context, next) => {
  return next()
    .then((response) => {
      for (const [header, value] of Object.entries(SECURITY_HEADERS)) {
        response.headers.set(header, value);
      }
      return response;
    })
    .catch((err) => {
      // Log errors so failures are visible in server logs instead of a silent 500.
      console.error(`[middleware] Error handling ${context.url.pathname}:`, err);
      return new Response('Internal Server Error', { status: 500 });
    });
});
