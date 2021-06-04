from django.contrib.sitemaps import Sitemap

class MySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    