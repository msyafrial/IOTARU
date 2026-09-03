# Runtime image — build dilakukan di GitHub Actions (npm run build).
# Image hanya membungkus hasil dist + dependency produksi.
FROM node:24-alpine

WORKDIR /app
ENV NODE_ENV=production \
    HOST=0.0.0.0 \
    PORT=4321

# Dependency produksi saja
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

# Hasil build dari CI (dist/client = aset statis, dist/server = SSR entry)
COPY dist ./dist

EXPOSE 4321
CMD ["node", "dist/server/entry.mjs"]
