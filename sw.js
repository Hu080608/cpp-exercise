/* 静态资源缓存：离线时仍可打开知识点与题库；编译功能需要联网。 */
const CACHE = 'cpplab-v1';
const ASSETS = [
  './', './index.html', './manifest.webmanifest', './assets/css/style.css',
  './assets/js/utils.js', './assets/js/sandbox.js', './assets/js/app.js',
  './assets/icon.svg', './data/knowledge.js', './data/downloads.js', './data/questions/manifest.json',
  './data/questions/ch1.json', './data/questions/ch2.json', './data/questions/ch3.json',
  './data/questions/ch4.json', './data/questions/ch5.json'
];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()).catch(() => self.skipWaiting()));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (url.origin !== location.origin || event.request.method !== 'GET') return;
  event.respondWith(caches.match(event.request).then(hit => hit || fetch(event.request).then(res => {
    const copy = res.clone();
    caches.open(CACHE).then(c => c.put(event.request, copy)).catch(() => {});
    return res;
  }).catch(() => caches.match('./index.html'))));
});
