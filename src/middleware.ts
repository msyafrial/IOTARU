import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware((context, next) => {
  const response = next();

  // Wrap the response to add headers
  return new Promise((resolve) => {
    response.then((res) => {
      // Clone the response to modify headers
      const newResponse = new Response(res.body, res);

      newResponse.headers.set('X-Frame-Options', 'DENY');
      newResponse.headers.set('X-Content-Type-Options', 'nosniff');
      newResponse.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
      newResponse.headers.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(), payment=()');
      newResponse.headers.set('X-XSS-Protection', '1; mode=block');
      newResponse.headers.set('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');

      // CSP — allow only what's needed
      newResponse.headers.set(
        'Content-Security-Policy',
        [
          "default-src 'self'",
          "script-src 'self' 'unsafe-inline' 'unsafe-eval' https://www.youtube.com https://www.youtube-nocookie.com",
          "style-src 'self' 'unsafe-inline'",
          "font-src 'self' data:",
          "img-src 'self' data: https:",
          "frame-src https://www.youtube.com https://www.youtube-nocookie.com",
          "connect-src 'self'",
        ].join('; ')
      );

      resolve(newResponse);
    }).catch((err) => {
      resolve(new Response('Internal Server Error', { status: 500 }));
    });
  });
});
