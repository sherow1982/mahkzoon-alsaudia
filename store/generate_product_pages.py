#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path

with open('data/products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# ===== تحديث index.html مع زر "تحميل المزيد" =====
INDEX_HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>مخزون السعودية - متجرك الإلكتروني المميز</title>
<meta name="description" content="مخزون السعودية - متجر إلكتروني متخصص في بيع المنتجات عالية الجودة بأسعار تنافسية">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>
:root {{
  --primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --secondary: #2d3748;
  --accent: #f6ad55;
  --text: #1a202c;
  --light: #f7fafc;
  --border: #e2e8f0;
}}

* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

body {{
  font-family: 'Cairo', sans-serif;
  background: var(--light);
  color: var(--text);
  line-height: 1.8;
}}

.container {{
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}}

/* Header */
.header {{
  background: #fff;
  border-bottom: 3px solid transparent;
  border-image: var(--primary) 1;
  padding: 20px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}}

.header-content {{
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.logo {{
  font-size: 32px;
  font-weight: 900;
  background: var(--primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}}

.search-box {{
  flex: 1;
  margin: 0 40px;
  display: flex;
  gap: 10px;
}}

.search-box input {{
  flex: 1;
  padding: 12px 20px;
  border: 2px solid var(--border);
  border-radius: 10px;
  font-size: 15px;
  font-family: 'Cairo', sans-serif;
  transition: all 0.3s;
}}

.search-box input:focus {{
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}}

.search-box button {{
  padding: 12px 25px;
  background: var(--primary);
  color: #fff;
  border: none;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
}}

.search-box button:hover {{
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}}

.cart-icon {{
  font-size: 28px;
  cursor: pointer;
  position: relative;
  transition: transform 0.3s;
}}

.cart-icon:hover {{
  transform: scale(1.2);
}}

.cart-count {{
  position: absolute;
  top: -8px;
  right: -8px;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: #fff;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 12px;
}}

/* Hero Section */
.hero {{
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  padding: 80px 40px;
  border-radius: 20px;
  text-align: center;
  margin: 40px 0;
  box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
}}

.hero h1 {{
  font-size: 48px;
  font-weight: 900;
  margin-bottom: 20px;
}}

.hero p {{
  font-size: 20px;
  margin-bottom: 30px;
  opacity: 0.95;
}}

.hero-btn {{
  background: #fff;
  color: #667eea;
  padding: 15px 40px;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
}}

.hero-btn:hover {{
  transform: scale(1.05);
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}}

/* Section Title */
.section-title {{
  font-size: 36px;
  font-weight: 900;
  color: var(--secondary);
  margin: 50px 0 30px;
  text-align: center;
}}

/* Products Grid */
.products-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
  margin: 40px 0;
}}

.product-card {{
  background: #fff;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 20px rgba(0,0,0,0.08);
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: pointer;
  display: flex;
  flex-direction: column;
}}

.product-card:hover {{
  transform: translateY(-10px);
  box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
}}

.product-image-wrapper {{
  position: relative;
  overflow: hidden;
  height: 280px;
}}

.product-image {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s;
}}

.product-card:hover .product-image {{
  transform: scale(1.1);
}}

.product-badge {{
  position: absolute;
  top: 15px;
  left: 15px;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: #fff;
  padding: 8px 15px;
  border-radius: 20px;
  font-weight: 700;
  font-size: 14px;
  box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
}}

.product-info {{
  padding: 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
}}

.product-title {{
  font-size: 18px;
  font-weight: 700;
  color: var(--secondary);
  margin-bottom: 12px;
  min-height: 50px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}}

.product-rating {{
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  font-size: 14px;
}}

.stars {{
  color: #f6ad55;
  letter-spacing: 2px;
}}

.rating-count {{
  color: #718096;
  font-size: 13px;
}}

.product-price {{
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 20px;
}}

.price-now {{
  font-size: 24px;
  font-weight: 900;
  color: #667eea;
}}

.price-old {{
  font-size: 16px;
  color: #cbd5e0;
  text-decoration: line-through;
}}

.product-actions {{
  display: flex;
  gap: 10px;
  margin-top: auto;
}}

.btn-cart {{
  flex: 1;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  border: none;
  padding: 12px 15px;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
  font-family: 'Cairo', sans-serif;
}}

.btn-cart:hover {{
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}}

.btn-view {{
  flex: 1;
  background: var(--light);
  color: #667eea;
  border: 2px solid #667eea;
  padding: 12px 15px;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s;
  font-family: 'Cairo', sans-serif;
}}

.btn-view:hover {{
  background: #667eea;
  color: #fff;
}}

/* Load More Button */
.load-more-container {{
  text-align: center;
  margin: 60px 0;
}}

.load-more-btn {{
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  padding: 18px 50px;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 900;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
  font-family: 'Cairo', sans-serif;
}}

.load-more-btn:hover {{
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
}}

.load-more-btn:active {{
  transform: translateY(-2px);
}}

.load-more-icon {{
  font-size: 22px;
  transition: transform 0.3s;
}}

.load-more-btn:hover .load-more-icon {{
  transform: translateY(3px);
}}

.loading {{
  display: none;
  text-align: center;
  padding: 30px;
}}

.spinner {{
  border: 4px solid var(--light);
  border-top: 4px solid #667eea;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 0 auto;
}}

@keyframes spin {{
  0% {{ transform: rotate(0deg); }}
  100% {{ transform: rotate(360deg); }}
}}

.no-more {{
  text-align: center;
  padding: 30px;
  color: #718096;
  font-size: 16px;
  font-weight: 600;
}}

/* Footer */
.footer {{
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #fff;
  padding: 50px 40px 20px;
  margin-top: 80px;
  border-radius: 20px 20px 0 0;
  text-align: center;
}}

.footer p {{
  font-size: 14px;
  margin-bottom: 10px;
}}

@media (max-width: 768px) {{
  .header-content {{
    flex-direction: column;
    gap: 15px;
  }}
  
  .search-box {{
    margin: 15px 0;
    width: 100%;
  }}
  
  .hero {{
    padding: 40px 20px;
  }}
  
  .hero h1 {{
    font-size: 32px;
  }}
  
  .products-grid {{
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
  }}
  
  .load-more-btn {{
    padding: 15px 40px;
    font-size: 16px;
  }}
}}
</style>
</head>
<body>

<!-- Header -->
<header class="header">
  <div class="container">
    <div class="header-content">
      <a href="index.html" class="logo">مخزون السعودية</a>
      <div class="search-box">
        <input type="text" id="searchInput" placeholder="ابحث عن منتج...">
        <button onclick="performSearch()">🔍</button>
      </div>
      <div class="cart-icon" onclick="goToCart()">
        🛒
        <span class="cart-count" id="cartCount">0</span>
      </div>
    </div>
  </div>
</header>

<!-- Hero -->
<div class="container">
  <div class="hero">
    <h1>🎉 مرحباً بك في مخزون السعودية</h1>
    <p>تسوق أفضل المنتجات بأسعار لا تقبل المنافسة</p>
    <button class="hero-btn" onclick="document.querySelector('.products-grid').scrollIntoView({{behavior: 'smooth'}})">اكتشف المنتجات</button>
  </div>
</div>

<!-- Featured Products -->
<div class="container">
  <h2 class="section-title">⭐ المنتجات المميزة</h2>
  <div class="products-grid" id="productsGrid"></div>
  
  <div class="loading" id="loading">
    <div class="spinner"></div>
  </div>
  
  <div class="load-more-container">
    <button class="load-more-btn" id="loadMoreBtn" onclick="loadMore()">
      <span class="load-more-icon">⬇️</span>
      تحميل المزيد
    </button>
    <div class="no-more" id="noMore" style="display: none;">
      ✓ تم تحميل جميع المنتجات
    </div>
  </div>
</div>

<!-- Footer -->
<footer class="footer">
  <div class="container">
    <p>&copy; 2025 مخزون السعودية. جميع الحقوق محفوظة.</p>
    <p>شحن مجاني | إرجاع مجاني | الدفع عند الاستلام</p>
  </div>
</footer>

<script>
const allProducts = {products_json};
let displayedCount = 12;
const itemsPerLoad = 12;

function renderProducts(productsToRender, append = false) {{
  const grid = document.getElementById('productsGrid');
  
  if (!append) {{
    grid.innerHTML = '';
  }}
  
  const html = productsToRender.map(p => {{
    const discount = Math.round(((p.price - p.sale_price) / p.price) * 100);
    const slug = p.title.toLowerCase().replace(/[^\\w\\s-]/g, '').replace(/[-\\s]+/g, '-').trim('-');
    
    return `
      <div class="product-card">
        <div class="product-image-wrapper">
          <img src="${{p.image_link}}" alt="${{p.title}}" class="product-image">
          <span class="product-badge">-${{discount}}%</span>
        </div>
        <div class="product-info">
          <h3 class="product-title">${{p.title}}</h3>
          <div class="product-rating">
            <span class="stars">★★★★★</span>
            <span class="rating-count">(15)</span>
          </div>
          <div class="product-price">
            <span class="price-now">${{p.sale_price}} ر.س</span>
            <span class="price-old">${{p.price}} ر.س</span>
          </div>
          <div class="product-actions">
            <button class="btn-cart" onclick="addToCart(event, ${{p.id}})">🛒 أضف للسلة</button>
            <button class="btn-view" onclick="window.open('products/${{slug}}.html', '_blank'); event.stopPropagation();">شاهد المزيد</button>
          </div>
        </div>
      </div>
    `;
  }}).join('');
  
  if (append) {{
    grid.insertAdjacentHTML('beforeend', html);
  }} else {{
    grid.innerHTML = html;
  }}
}}

function loadMore() {{
  const loading = document.getElementById('loading');
  const loadBtn = document.getElementById('loadMoreBtn');
  const noMore = document.getElementById('noMore');
  
  loading.style.display = 'block';
  loadBtn.style.display = 'none';
  
  setTimeout(() => {{
    const nextProducts = allProducts.slice(displayedCount, displayedCount + itemsPerLoad);
    
    if (nextProducts.length === 0) {{
      loading.style.display = 'none';
      noMore.style.display = 'block';
      return;
    }}
    
    renderProducts(nextProducts, true);
    displayedCount += itemsPerLoad;
    
    loading.style.display = 'none';
    
    if (displayedCount >= allProducts.length) {{
      noMore.style.display = 'block';
    }} else {{
      loadBtn.style.display = 'inline-flex';
    }}
  }}, 600);
}}

function addToCart(e, productId) {{
  e.stopPropagation();
  const product = allProducts.find(p => p.id === productId);
  alert('✅ تم إضافة ' + product.title + ' للسلة!');
  updateCartCount();
}}

function updateCartCount() {{
  document.getElementById('cartCount').textContent = Math.floor(Math.random() * 5) + 1;
}}

function performSearch() {{
  const query = document.getElementById('searchInput').value.toLowerCase();
  const filtered = allProducts.filter(p => p.title.toLowerCase().includes(query));
  displayedCount = 12;
  renderProducts(filtered.slice(0, 12));
  
  const loadBtn = document.getElementById('loadMoreBtn');
  const noMore = document.getElementById('noMore');
  
  if (filtered.length <= 12) {{
    loadBtn.style.display = 'none';
    noMore.style.display = filtered.length === 0 ? 'block' : 'none';
  }} else {{
    loadBtn.style.display = 'inline-flex';
    noMore.style.display = 'none';
  }}
}}

function goToCart() {{
  alert('🛒 السلة قيد التطوير - سيتم إطلاقها قريباً!');
}}

document.getElementById('searchInput').addEventListener('keypress', function(e) {{
  if (e.key === 'Enter') performSearch();
}});

renderProducts(allProducts.slice(0, displayedCount));
updateCartCount();
</script>

</body>
</html>
"""

# حفظ index.html
with open('index.html', 'w', encoding='utf-8') as f:
    products_json = json.dumps(products, ensure_ascii=False)
    f.write(INDEX_HTML.format(products_json=products_json))

print("✅ تم تحديث index.html مع زر تحميل المزيد!")
