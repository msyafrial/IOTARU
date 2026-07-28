import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const blog = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/blog',
  }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date().optional(),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

const products = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/products',
  }),
  schema: ({ image }) => z.object({
    title: z.string(),
    category: z.string(),
    featured: z.boolean().default(false),
    description: z.string(),
    image: image().optional(),
    gallery: z.array(image()).default([]),
    video: z.string().optional(),
    created: z.date().optional(),
  }),
});

const solutions = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/solutions',
  }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
  }),
});

export const collections = {
  blog,
  products,
  solutions,
};