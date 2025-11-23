#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكريبت توليد Sitemap و Google Merchant Feed
"""

import json
import os
from datetime import datetime

def slugify(text):
    """تحويل النص إلى slug"""
    import re
    text = text.replace('...', '')
    forbidden_chars = ['*', ':', '?', '"', '<', '>', '|', '/', '\\', '\t', '\n', '\r']
    for char in forbidden_chars:
        text = text.replace(char, '')
    text = text.replace('(', '').replace(')', '').replace('.', '').replace(',', '')
    text = re.sub(r'\s+', ' ', text)
    text = text.replace(' ', '-')
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    text = text.lower()
    return text

def generate_sitemap(products):
    """توليد sitemap.xml"""
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # الصفحة الرئيسية
    xml += '  <url>\n'
    xml += '    <loc>https://mahkzoon-alsaudia.arabsad.com/</loc>\n'
    xml += f'    <lastmod>{today}</lastmod>\n'
    xml += '    <changefreq>daily</changefreq>\n'
    xml += '    <priority>1.0</priority>\n'
    xml += '  </url>\n'
    
    # صفحة المنتجات
    xml += '  <url>\n'
    xml += '    <loc>https://mahkzoon-alsaudia.arabsad.com/products.html</loc>\n'
    xml += f'    <lastmod>{today}</lastmod>\n'
    xml += '    <changefreq>daily</changefreq>\n'
    xml += '    <priority>0.9</priority>\n'
    xml += '  </url>\n'
    
    # صفحات المنتجات
    for product in products:
        slug = slugify(product['title'])
        xml += '  <url>\n'
        xml += f'    <loc>https://mahkzoon-alsaudia.arabsad.com/products/{slug}.html</loc>\n'
        xml += f'    <lastmod>{today}</lastmod>\n'
        xml += '    <changefreq>weekly</changefreq>\n'
        xml += '    <priority>0.8</priority>\n'
        xml += '  </url>\n'
    
    xml += '</urlset>'
    
    return xml

def generate_merchant_feed(products):
    """توليد Google Merchant Center feed.xml"""
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n'
    xml += '  <channel>\n'
    xml += '    <title>مخزون السعودية</title>\n'
    xml += '    <link>https://mahkzoon-alsaudia.arabsad.com</link>\n'
    xml += '    <description>متجر مخزون السعودية - منتجات متنوعة بأفضل الأسعار</description>\n\n'
    
    for product in products:
        slug = slugify(product['title'])
        title = product['title'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        xml += '    <item>\n'
        xml += f'      <g:id>{product["id"]}</g:id>\n'
        xml += f'      <g:title>{title}</g:title>\n'
        xml += f'      <g:description>{title} - منتج عالي الجودة متوفر الآن بأفضل الأسعار</g:description>\n'
        xml += f'      <g:link>https://mahkzoon-alsaudia.arabsad.com/products/{slug}.html</g:link>\n'
        xml += f'      <g:image_link>{product["image_link"]}</g:image_link>\n'
        xml += '      <g:condition>new</g:condition>\n'
        xml += '      <g:availability>in stock</g:availability>\n'
        xml += f'      <g:price>{product["sale_price"]} SAR</g:price>\n'
        xml += '      <g:brand>مخزون السعودية</g:brand>\n'
        xml += '      <g:gtin></g:gtin>\n'
        xml += f'      <g:mpn>{product["id"]}</g:mpn>\n'
        xml += '      <g:google_product_category>Home &amp; Garden</g:google_product_category>\n'
        xml += '      <g:product_type>منتجات عامة</g:product_type>\n'
        xml += '    </item>\n\n'
    
    xml += '  </channel>\n'
    xml += '</rss>'
    
    return xml

def main():
    """الدالة الرئيسية"""
    print("="*70)
    print("🗺️  سكريبت توليد Sitemap و Google Merchant Feed")
    print("="*70)
    
    # قراءة المنتجات
    if not os.path.exists('data/products.json'):
        print("❌ خطأ: ملف data/products.json غير موجود!")
        return
    
    with open('data/products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    print(f"✅ تم قراءة {len(products)} منتج\n")
    
    # توليد sitemap.xml
    print("📄 توليد sitemap.xml...")
    sitemap = generate_sitemap(products)
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("✅ تم إنشاء sitemap.xml\n")
    
    # توليد feed.xml
    print("📄 توليد feed.xml...")
    feed = generate_merchant_feed(products)
    with open('feed.xml', 'w', encoding='utf-8') as f:
        f.write(feed)
    print("✅ تم إنشاء feed.xml\n")
    
    print("="*70)
    print("✅ تم إنشاء الملفات بنجاح!")
    print("="*70)
    print("\n📌 الملفات:")
    print("   - sitemap.xml (للـ SEO)")
    print("   - feed.xml (لـ Google Merchant Center)")
    print("\n💡 ارفع الملفات:")
    print("   git add sitemap.xml feed.xml")
    print("   git commit -m 'إضافة: Sitemap و Google Merchant Feed'")
    print("   git push")
    print("\n")

if __name__ == "__main__":
    main()
