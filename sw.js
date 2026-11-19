/*
 * PECTAA Smart Practice Portal — offline-first service worker.
 * Pre-caches the complete split portal so all 16 data parts are available offline.
 */
const APP_CACHE = 'pectaa-mcqs-v51';
const FONT_CACHE = 'pectaa-fonts-v1';
const PART_VERSION = '20261119-offline-v51';
const PARTS = Array.from({length:16}, (_,i) =>
  `./.portal-deploy-parts/part-${String(i+1).padStart(3,'0')}.txt?v=${PART_VERSION}`
);
const APP_SHELL = ['./','./index.html','./manifest.webmanifest','./icon.svg',...PARTS];
const FONT_HOSTS = new Set(['fonts.googleapis.com','fonts.gstatic.com']);

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(APP_CACHE);
    // Core portal files are required for offline operation; fail install if any part is missing.
    for (const path of APP_SHELL) {
      try {
        const response = await fetch(path, {cache:'reload'});
        if (!response.ok) throw new Error('HTTP '+response.status+' for '+path);
        await cache.put(path, response);
      } catch (error) {
        if (PARTS.includes(path) || path === './index.html' || path === './') throw error;
        // Optional manifest/icon files must not block installation.
      }
    }
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys
      .filter(key => key.startsWith('pectaa-mcqs-') && key !== APP_CACHE)
      .map(key => caches.delete(key)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  const sameOrigin = url.origin === self.location.origin;
  const googleFont = FONT_HOSTS.has(url.hostname);
  if (!sameOrigin && !googleFont) return;

  if (googleFont) {
    event.respondWith((async () => {
      const cache = await caches.open(FONT_CACHE);
      const cached = await cache.match(request);
      if (cached) return cached;
      try {
        const response = await fetch(request);
        if (response.ok || response.type === 'opaque') cache.put(request,response.clone()).catch(()=>{});
        return response;
      } catch (_) {
        return new Response('',{status:503,statusText:'Font unavailable offline'});
      }
    })());
    return;
  }

  if (request.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const response = await fetch(request);
        if (response.ok) {
          const cache = await caches.open(APP_CACHE);
          await cache.put('./index.html',response.clone());
        }
        return response;
      } catch (_) {
        const cache = await caches.open(APP_CACHE);
        return (await cache.match(request)) || (await cache.match('./index.html')) || (await cache.match('./'));
      }
    })());
    return;
  }

  event.respondWith((async () => {
    const cache = await caches.open(APP_CACHE);
    const cached = await cache.match(request);
    if (cached) return cached;
    try {
      const response = await fetch(request);
      if (response.ok) cache.put(request,response.clone()).catch(()=>{});
      return response;
    } catch (_) {
      return new Response('This portal resource is not available offline yet. Please connect to the internet once and reload the portal.',{
        status:503,statusText:'Offline resource not cached',headers:{'Content-Type':'text/plain; charset=utf-8'}
      });
    }
  })());
});
