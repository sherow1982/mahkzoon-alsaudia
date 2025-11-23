#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكربت إنشاء متجر مخزون السعودية الإلكتروني
ينشئ جميع الملفات والصفحات تلقائياً
"""

import os
import json
import shutil
from pathlib import Path

print("=" * 60)
print("🚀 بدء إنشاء متجر مخزون السعودية الإلكتروني")
print("=" * 60)

# 1. إنشاء المجلدات
folders = [
    'store',
    'store/css',
    'store/js',
    'store/data',
    'store/products',
    'store/legal'
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)
    print(f"✓ تم إنشاء: {folder}")

# 2. نسخ products.json
if os.path.exists('products.json'):
    shutil.copy('products.json', 'store/data/products.json')
    print("✓ تم نسخ products.json")
    
    # قراءة المنتجات للاستخدام لاحقاً
    with open('products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
else:
    print("⚠️ تحذير: ملف products.json غير موجود")
    products = []

# 3. إنشاء categories.json
categories_data = {
    "categories": [
        {"id": "electronics", "name": "إلكترونيات", "icon": "📱"},
        {"id": "home-kitchen", "name": "منزل ومطبخ", "icon": "🏠"},
        {"id": "beauty-care", "name": "جمال وعناية", "icon": "💄"},
        {"id": "sports-fitness", "name": "رياضة ولياقة", "icon": "⚽"},
        {"id": "fashion-accessories", "name": "أزياء وإكسسوارات", "icon": "👗"},
        {"id": "kids-toys", "name": "ألعاب أطفال", "icon": "🧸"}
    ]
}

with open('store/data/categories.json', 'w', encoding='utf-8') as f:
    json.dump(categories_data, f, ensure_ascii=False, indent=2)
print("✓ تم إنشاء categories.json")

# 4. إنشاء style.css
css_content = """:root {
  --primary-color: #2d5016;
  --secondary-color: #4a7c24;
  --accent-color: #f4a261;
  --text-color: #333;
  --light-bg: #f8f9fa;
  --white: #ffffff;
  --border-color: #dee2e6;
  --success-color: #28a745;
  --danger-color: #dc3545;
  --shadow: 0 2px 10px rgba(0,0,0,0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--light-bg);
  direction: rtl;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Header */
.header {
  background: var(--white);
  box-shadow: var(--shadow);
  position: sticky;
  top: 0;
  z-index: 1000;
  padding: 15px 0;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}

.logo h1 {
  color: var(--primary-color);
  font-size: 1.8rem;
  margin: 0;
}

.logo h1 a {
  color: inherit;
  text-decoration: none;
}

.main-nav ul {
  list-style: none;
  display: flex;
  gap: 25px;
  margin: 0;
}

.main-nav a {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 500;
  padding: 8px 15px;
  border-radius: 5px;
  transition: all 0.3s ease;
}

.main-nav a:hover,
.main-nav a.active {
  background: var(--primary-color);
  color: var(--white);
}

.search-box {
  display: flex;
  gap: 5px;
}

.search-box input {
  padding: 10px 15px;
  border: 2px solid var(--border-color);
  border-radius: 5px;
  width: 250px;
  font-size: 0.95rem;
}

.search-box button {
  padding: 10px 20px;
  background: var(--primary-color);
  color: var(--white);
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

/* Hero */
.hero {
  background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
  color: var(--white);
  padding: 80px 0;
  text-align: center;
}

.hero h2 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 30px;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 12px 30px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
  font-size: 1rem;
}

.btn-primary {
  background: var(--accent-color);
  color: var(--white);
}

.btn-primary:hover {
  background: #e76f51;
  transform: translateY(-2px);
}

/* Products Grid */
.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 30px;
  margin: 30px 0;
}

.product-card {
  background: var(--white);
  border-radius: 10px;
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: transform 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
}

.product-card img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}

.product-info {
  padding: 20px;
}

.product-info h3 {
  font-size: 1.1rem;
  margin-bottom: 10px;
  height: 50px;
  overflow: hidden;
}

.product-info h3 a {
  color: var(--text-color);
  text-decoration: none;
}

.product-price {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 15px 0;
}

.old-price {
  text-decoration: line-through;
  color: #999;
  font-size: 0.95rem;
}

.current-price {
  color: var(--success-color);
  font-size: 1.3rem;
  font-weight: bold;
}

.discount-badge {
  background: var(--danger-color);
  color: var(--white);
  padding: 3px 8px;
  border-radius: 3px;
  font-size: 0.85rem;
}

/* Cart */
.cart-table {
  width: 100%;
  background: var(--white);
  border-radius: 10px;
  margin: 30px 0;
}

.cart-table table {
  width: 100%;
  border-collapse: collapse;
}

.cart-table th,
.cart-table td {
  padding: 15px;
  text-align: center;
  border-bottom: 1px solid var(--border-color);
}

.cart-table th {
  background: var(--primary-color);
  color: var(--white);
}

.cart-summary {
  background: var(--white);
  padding: 30px;
  border-radius: 10px;
  max-width: 500px;
  margin: 30px auto;
}

.summary-row {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid var(--border-color);
}

.summary-row.total {
  font-size: 1.3rem;
  font-weight: bold;
  color: var(--primary-color);
}

/* Footer */
.footer {
  background: var(--primary-color);
  color: var(--white);
  padding: 50px 0 20px;
  margin-top: 80px;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
}

.footer-section h3 {
  margin-bottom: 20px;
}

.footer-section ul {
  list-style: none;
}

.footer-section ul li {
  margin-bottom: 10px;
}

.footer-section a {
  color: var(--white);
  text-decoration: none;
  opacity: 0.9;
}

.footer-section a:hover {
  opacity: 1;
}

.footer-bottom {
  text-align: center;
  padding-top: 30px;
  border-top: 1px solid rgba(255,255,255,0.2);
}

/* Responsive */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
  }
  
  .main-nav ul {
    flex-direction: column;
    gap: 10px;
  }
  
  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}
"""

with open('store/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)
print("✓ تم إنشاء style.css")

# 5. إنشاء products.js
js_products = """// تحميل المنتجات
let products = [];

async function loadProducts() {
    try {
        const response = await fetch('data/products.json');
        products = await response.json();
        return products;
    } catch (error) {
        console.error('خطأ في تحميل المنتجات:', error);
        return [];
    }
}

function getProductById(id) {
    return products.find(p => p.id === parseInt(id));
}

function searchProducts(query) {
    const term = query.toLowerCase();
    return products.filter(p => p.title.toLowerCase().includes(term));
}

function filterByPrice(min, max) {
    return products.filter(p => p.sale_price >= min && p.sale_price <= max);
}

function sortProducts(productsArray, sortBy) {
    const sorted = [...productsArray];
    
    switch(sortBy) {
        case 'price-low':
            return sorted.sort((a, b) => a.sale_price - b.sale_price);
        case 'price-high':
            return sorted.sort((a, b) => b.sale_price - a.sale_price);
        case 'name':
            return sorted.sort((a, b) => a.title.localeCompare(b.title, 'ar'));
        default:
            return sorted;
    }
}

function calculateDiscount(price, salePrice) {
    return Math.round(((price - salePrice) / price) * 100);
}
"""

with open('store/js/products.js', 'w', encoding='utf-8') as f:
    f.write(js_products)
print("✓ تم إنشاء products.js")

# 6. إنشاء cart.js
js_cart = """// إدارة السلة
class ShoppingCart {
    constructor() {
        this.items = this.loadCart();
    }
    
    loadCart() {
        const saved = localStorage.getItem('cart');
        return saved ? JSON.parse(saved) : [];
    }
    
    saveCart() {
        localStorage.setItem('cart', JSON.stringify(this.items));
        this.updateCartUI();
    }
    
    addItem(productId, quantity = 1) {
        const product = getProductById(productId);
        if (!product) return false;
        
        const existing = this.items.find(item => item.id === productId);
        
        if (existing) {
            existing.quantity += quantity;
        } else {
            this.items.push({
                id: productId,
                title: product.title,
                price: product.sale_price,
                image: product.image_link,
                quantity: quantity
            });
        }
        
        this.saveCart();
        return true;
    }
    
    updateQuantity(productId, quantity) {
        const item = this.items.find(i => i.id === productId);
        if (item) {
            item.quantity = Math.max(1, quantity);
            this.saveCart();
        }
    }
    
    removeItem(productId) {
        this.items = this.items.filter(i => i.id !== productId);
        this.saveCart();
    }
    
    clearCart() {
        this.items = [];
        this.saveCart();
    }
    
    getTotal() {
        return this.items.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    }
    
    getItemCount() {
        return this.items.reduce((count, item) => count + item.quantity, 0);
    }
    
    updateCartUI() {
        const cartCount = document.getElementById('cart-count');
        if (cartCount) {
            cartCount.textContent = this.getItemCount();
        }
    }
}

const cart = new ShoppingCart();

function addToCart(productId, quantity = 1) {
    if (cart.addItem(productId, quantity)) {
        alert('تمت الإضافة للسلة بنجاح!');
    }
}

function updateCartCount() {
    cart.updateCartUI();
}
"""

with open('store/js/cart.js', 'w', encoding='utf-8') as f:
    f.write(js_cart)
print("✓ تم إنشاء cart.js")

# 7. إنشاء search.js
js_search = """// البحث
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    
    if (searchBtn) {
        searchBtn.addEventListener('click', performSearch);
    }
    
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') performSearch();
        });
    }
});

function performSearch() {
    const query = document.getElementById('search-input').value.trim();
    if (query) {
        window.location.href = `products.html?search=${encodeURIComponent(query)}`;
    }
}
"""

with open('store/js/search.js', 'w', encoding='utf-8') as f:
    f.write(js_search)
print("✓ تم إنشاء search.js")

# 8. إنشاء index.html
html_index = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="مخزون السعودية - متجرك الإلكتروني المميز للمنتجات عالية الجودة بأفضل الأسعار">
    <title>مخزون السعودية - المتجر الإلكتروني</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <h1>مخزون السعودية</h1>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="index.html" class="active">الرئيسية</a></li>
                        <li><a href="products.html">المنتجات</a></li>
                        <li><a href="cart.html">السلة (<span id="cart-count">0</span>)</a></li>
                        <li><a href="account.html">حسابي</a></li>
                    </ul>
                </nav>
                <div class="search-box">
                    <input type="text" id="search-input" placeholder="ابحث عن منتج...">
                    <button id="search-btn">🔍</button>
                </div>
            </div>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h2>مرحباً بك في مخزون السعودية</h2>
            <p>اكتشف مجموعة واسعة من المنتجات عالية الجودة بأسعار تنافسية</p>
            <a href="products.html" class="btn btn-primary">تصفح المنتجات</a>
        </div>
    </section>

    <section class="products">
        <div class="container">
            <h2 style="text-align: center; margin: 50px 0 30px; color: var(--primary-color);">منتجات مميزة</h2>
            <div id="featured-products" class="products-grid"></div>
        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>عن مخزون السعودية</h3>
                    <p>متجرك الإلكتروني المميز للمنتجات عالية الجودة</p>
                </div>
                <div class="footer-section">
                    <h3>خدمة العملاء</h3>
                    <ul>
                        <li><a href="legal/contact.html">اتصل بنا</a></li>
                        <li><a href="legal/shipping-policy.html">سياسة الشحن</a></li>
                        <li><a href="legal/return-policy.html">سياسة الاسترجاع</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>الصفحات القانونية</h3>
                    <ul>
                        <li><a href="legal/terms.html">الشروط والأحكام</a></li>
                        <li><a href="legal/privacy-policy.html">سياسة الخصوصية</a></li>
                        <li><a href="legal/refund-policy.html">سياسة الاسترداد</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 مخزون السعودية. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>

    <script src="js/products.js"></script>
    <script src="js/cart.js"></script>
    <script src="js/search.js"></script>
    <script>
        loadProducts().then(products => {
            const featured = products.sort(() => 0.5 - Math.random()).slice(0, 8);
            document.getElementById('featured-products').innerHTML = featured.map(p => `
                <div class="product-card">
                    <a href="products/product-${p.id}.html">
                        <img src="${p.image_link}" alt="${p.title}" loading="lazy">
                    </a>
                    <div class="product-info">
                        <h3><a href="products/product-${p.id}.html">${p.title}</a></h3>
                        <div class="product-price">
                            <span class="old-price">${p.price} ر.س</span>
                            <span class="current-price">${p.sale_price} ر.س</span>
                        </div>
                        <button class="btn btn-primary" onclick="addToCart(${p.id})">أضف للسلة</button>
                    </div>
                </div>
            `).join('');
            updateCartCount();
        });
    </script>
</body>
</html>
"""

with open('store/index.html', 'w', encoding='utf-8') as f:
    f.write(html_index)
print("✓ تم إنشاء index.html")

# 9. إنشاء products.html
html_products = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>المنتجات - مخزون السعودية</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <h1><a href="index.html">مخزون السعودية</a></h1>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="index.html">الرئيسية</a></li>
                        <li><a href="products.html" class="active">المنتجات</a></li>
                        <li><a href="cart.html">السلة (<span id="cart-count">0</span>)</a></li>
                        <li><a href="account.html">حسابي</a></li>
                    </ul>
                </nav>
                <div class="search-box">
                    <input type="text" id="search-input" placeholder="ابحث عن منتج...">
                    <button id="search-btn">🔍</button>
                </div>
            </div>
        </div>
    </header>

    <div class="container" style="margin: 40px auto;">
        <h1 style="color: var(--primary-color); margin-bottom: 30px;">جميع المنتجات</h1>
        
        <div style="margin-bottom: 20px;">
            <label>ترتيب حسب: </label>
            <select id="sort-select" style="padding: 10px; border-radius: 5px;">
                <option value="">الافتراضي</option>
                <option value="price-low">السعر: من الأقل للأعلى</option>
                <option value="price-high">السعر: من الأعلى للأقل</option>
                <option value="name">الاسم</option>
            </select>
        </div>
        
        <div id="products-list" class="products-grid"></div>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2025 مخزون السعودية. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>

    <script src="js/products.js"></script>
    <script src="js/cart.js"></script>
    <script src="js/search.js"></script>
    <script>
        let allProducts = [];
        
        loadProducts().then(products => {
            allProducts = products;
            displayProducts(products);
            updateCartCount();
        });
        
        function displayProducts(products) {
            document.getElementById('products-list').innerHTML = products.map(p => `
                <div class="product-card">
                    <a href="products/product-${p.id}.html">
                        <img src="${p.image_link}" alt="${p.title}" loading="lazy">
                    </a>
                    <div class="product-info">
                        <h3><a href="products/product-${p.id}.html">${p.title}</a></h3>
                        <div class="product-price">
                            <span class="old-price">${p.price} ر.س</span>
                            <span class="current-price">${p.sale_price} ر.س</span>
                        </div>
                        <button class="btn btn-primary" onclick="addToCart(${p.id})">أضف للسلة</button>
                    </div>
                </div>
            `).join('');
        }
        
        document.getElementById('sort-select').addEventListener('change', function() {
            const sorted = sortProducts(allProducts, this.value);
            displayProducts(sorted);
        });
    </script>
</body>
</html>
"""

with open('store/products.html', 'w', encoding='utf-8') as f:
    f.write(html_products)
print("✓ تم إنشاء products.html")

# 10. إنشاء cart.html
html_cart = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>السلة - مخزون السعودية</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <h1><a href="index.html">مخزون السعودية</a></h1>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="index.html">الرئيسية</a></li>
                        <li><a href="products.html">المنتجات</a></li>
                        <li><a href="cart.html" class="active">السلة (<span id="cart-count">0</span>)</a></li>
                        <li><a href="account.html">حسابي</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <div class="container" style="margin: 40px auto;">
        <h1 style="color: var(--primary-color);">سلة التسوق</h1>
        
        <div id="cart-items" class="cart-table"></div>
        
        <div id="cart-summary" class="cart-summary"></div>
        
        <div style="text-align: center; margin: 30px 0;">
            <a href="checkout.html" class="btn btn-primary" style="padding: 15px 40px; font-size: 1.1rem;">إتمام الطلب</a>
            <a href="products.html" class="btn" style="background: #6c757d; color: white; margin-right: 15px;">متابعة التسوق</a>
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2025 مخزون السعودية. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>

    <script src="js/products.js"></script>
    <script src="js/cart.js"></script>
    <script>
        function displayCart() {
            const cartItems = document.getElementById('cart-items');
            const cartSummary = document.getElementById('cart-summary');
            
            if (cart.items.length === 0) {
                cartItems.innerHTML = '<p style="text-align: center; padding: 50px;">السلة فارغة</p>';
                cartSummary.innerHTML = '';
                return;
            }
            
            cartItems.innerHTML = `
                <table>
                    <thead>
                        <tr>
                            <th>المنتج</th>
                            <th>السعر</th>
                            <th>الكمية</th>
                            <th>الإجمالي</th>
                            <th>حذف</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${cart.items.map(item => `
                            <tr>
                                <td>
                                    <div style="display: flex; align-items: center; gap: 15px;">
                                        <img src="${item.image}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 5px;">
                                        <span>${item.title}</span>
                                    </div>
                                </td>
                                <td>${item.price} ر.س</td>
                                <td>
                                    <input type="number" value="${item.quantity}" min="1" 
                                        onchange="cart.updateQuantity(${item.id}, this.value); displayCart();"
                                        style="width: 60px; padding: 5px; text-align: center;">
                                </td>
                                <td>${(item.price * item.quantity).toFixed(2)} ر.س</td>
                                <td>
                                    <button onclick="cart.removeItem(${item.id}); displayCart();" 
                                        style="background: var(--danger-color); color: white; border: none; padding: 8px 15px; border-radius: 5px; cursor: pointer;">
                                        حذف
                                    </button>
                                </td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            `;
            
            const total = cart.getTotal();
            const shipping = total > 300 ? 0 : 25;
            const finalTotal = total + shipping;
            
            cartSummary.innerHTML = `
                <h3>ملخص الطلب</h3>
                <div class="summary-row">
                    <span>المجموع الفرعي:</span>
                    <span>${total.toFixed(2)} ر.س</span>
                </div>
                <div class="summary-row">
                    <span>الشحن:</span>
                    <span>${shipping === 0 ? 'مجاناً' : shipping + ' ر.س'}</span>
                </div>
                <div class="summary-row total">
                    <span>الإجمالي:</span>
                    <span>${finalTotal.toFixed(2)} ر.س</span>
                </div>
                ${total < 300 ? '<p style="color: #666; font-size: 0.9rem; margin-top: 10px;">شحن مجاني للطلبات فوق 300 ريال</p>' : ''}
            `;
        }
        
        updateCartCount();
        displayCart();
    </script>
</body>
</html>
"""

with open('store/cart.html', 'w', encoding='utf-8') as f:
    f.write(html_cart)
print("✓ تم إنشاء cart.html")

# 11. إنشاء checkout.html
html_checkout = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>إتمام الطلب - مخزون السعودية</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .checkout-container {
            display: grid;
            grid-template-columns: 1.5fr 1fr;
            gap: 30px;
            margin: 40px auto;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid var(--border-color);
            border-radius: 5px;
            font-size: 1rem;
        }
        @media (max-width: 768px) {
            .checkout-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <h1><a href="index.html">مخزون السعودية</a></h1>
                </div>
            </div>
        </div>
    </header>

    <div class="container checkout-container">
        <div style="background: white; padding: 30px; border-radius: 10px;">
            <h2 style="color: var(--primary-color); margin-bottom: 30px;">معلومات الشحن</h2>
            <form id="checkout-form">
                <div class="form-group">
                    <label>الاسم الكامل *</label>
                    <input type="text" id="full-name" required>
                </div>
                <div class="form-group">
                    <label>رقم الجوال *</label>
                    <input type="tel" id="phone" required>
                </div>
                <div class="form-group">
                    <label>جوال بديل</label>
                    <input type="tel" id="alternate-phone">
                </div>
                <div class="form-group">
                    <label>البريد الإلكتروني</label>
                    <input type="email" id="email">
                </div>
                <div class="form-group">
                    <label>العنوان الكامل *</label>
                    <textarea id="address" rows="3" required></textarea>
                </div>
                <div class="form-group">
                    <label>المدينة *</label>
                    <input type="text" id="city" required>
                </div>
                <div class="form-group">
                    <label>ملاحظات إضافية</label>
                    <textarea id="notes" rows="3"></textarea>
                </div>
                <button type="submit" class="btn btn-primary" style="width: 100%; padding: 15px;">إرسال الطلب عبر واتساب</button>
            </form>
        </div>
        
        <div>
            <div class="cart-summary">
                <h3>ملخص الطلب</h3>
                <div id="order-summary"></div>
            </div>
        </div>
    </div>

    <script src="js/products.js"></script>
    <script src="js/cart.js"></script>
    <script>
        function displayOrderSummary() {
            const container = document.getElementById('order-summary');
            const total = cart.getTotal();
            const shipping = total > 300 ? 0 : 25;
            const finalTotal = total + shipping;
            
            container.innerHTML = `
                <div style="margin-bottom: 20px;">
                    ${cart.items.map(item => `
                        <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--border-color);">
                            <span>${item.title} × ${item.quantity}</span>
                            <span>${(item.price * item.quantity).toFixed(2)} ر.س</span>
                        </div>
                    `).join('')}
                </div>
                <div class="summary-row">
                    <span>المجموع الفرعي:</span>
                    <span>${total.toFixed(2)} ر.س</span>
                </div>
                <div class="summary-row">
                    <span>الشحن:</span>
                    <span>${shipping === 0 ? 'مجاناً' : shipping + ' ر.س'}</span>
                </div>
                <div class="summary-row total">
                    <span>الإجمالي:</span>
                    <span>${finalTotal.toFixed(2)} ر.س</span>
                </div>
            `;
        }
        
        document.getElementById('checkout-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const data = {
                name: document.getElementById('full-name').value,
                phone: document.getElementById('phone').value,
                alternatePhone: document.getElementById('alternate-phone').value,
                email: document.getElementById('email').value,
                address: document.getElementById('address').value,
                city: document.getElementById('city').value,
                notes: document.getElementById('notes').value
            };
            
            let message = `🛍️ *طلب جديد من مخزون السعودية*\\n\\n`;
            message += `👤 *الاسم:* ${data.name}\\n`;
            message += `📱 *الجوال:* ${data.phone}\\n`;
            if (data.alternatePhone) message += `📞 *جوال بديل:* ${data.alternatePhone}\\n`;
            if (data.email) message += `📧 *البريد:* ${data.email}\\n`;
            message += `📍 *العنوان:* ${data.address}\\n`;
            message += `🏙️ *المدينة:* ${data.city}\\n`;
            if (data.notes) message += `📝 *ملاحظات:* ${data.notes}\\n`;
            
            message += `\\n📦 *المنتجات:*\\n`;
            cart.items.forEach((item, i) => {
                message += `${i+1}. ${item.title}\\n`;
                message += `   الكمية: ${item.quantity} × ${item.price} ر.س\\n\\n`;
            });
            
            const total = cart.getTotal();
            const shipping = total > 300 ? 0 : 25;
            message += `💰 *الإجمالي:* ${(total + shipping).toFixed(2)} ر.س`;
            
            const whatsappNumber = '966XXXXXXXXX'; // ضع رقمك هنا
            const url = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
            
            window.open(url, '_blank');
            
            setTimeout(() => {
                cart.clearCart();
                alert('تم إرسال طلبك! شكراً لك');
                window.location.href = 'index.html';
            }, 1000);
        });
        
        displayOrderSummary();
        updateCartCount();
    </script>
</body>
</html>
"""

with open('store/checkout.html', 'w', encoding='utf-8') as f:
    f.write(html_checkout)
print("✓ تم إنشاء checkout.html")

# 12. إنشاء account.html
html_account = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>حسابي - مخزون السعودية</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <h1><a href="index.html">مخزون السعودية</a></h1>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="index.html">الرئيسية</a></li>
                        <li><a href="products.html">المنتجات</a></li>
                        <li><a href="cart.html">السلة (<span id="cart-count">0</span>)</a></li>
                        <li><a href="account.html" class="active">حسابي</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <div class="container" style="margin: 40px auto; text-align: center; padding: 100px 20px;">
        <h1 style="color: var(--primary-color);">حسابي</h1>
        <p style="font-size: 1.2rem; color: #666; margin: 20px 0;">هذه الصفحة قيد التطوير</p>
        <a href="products.html" class="btn btn-primary">تصفح المنتجات</a>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2025 مخزون السعودية. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>

    <script src="js/cart.js"></script>
    <script>updateCartCount();</script>
</body>
</html>
"""

with open('store/account.html', 'w', encoding='utf-8') as f:
    f.write(html_account)
print("✓ تم إنشاء account.html")

# 13. إنشاء الصفحات القانونية
legal_pages = {
    'privacy-policy.html': ('سياسة الخصوصية', '''
        <p>نحن في مخزون السعودية نلتزم بحماية خصوصيتك وبياناتك الشخصية.</p>
        
        <h2>جمع المعلومات</h2>
        <p>نقوم بجمع المعلومات التالية:</p>
        <ul>
            <li>الاسم الكامل</li>
            <li>رقم الجوال</li>
            <li>البريد الإلكتروني</li>
            <li>عنوان الشحن</li>
        </ul>
        
        <h2>استخدام المعلومات</h2>
        <p>نستخدم معلوماتك لـ:</p>
        <ul>
            <li>معالجة طلباتك</li>
            <li>التواصل معك بخصوص طلبك</li>
            <li>تحسين خدماتنا</li>
        </ul>
        
        <h2>حماية البيانات</h2>
        <p>نستخدم إجراءات أمنية لحماية بياناتك من الوصول غير المصرح به.</p>
        
        <h2>مشاركة المعلومات</h2>
        <p>لا نشارك معلوماتك الشخصية مع أطراف ثالثة إلا للضرورة القصوى لإتمام طلبك.</p>
    '''),
    
    'terms.html': ('الشروط والأحكام', '''
        <p>مرحباً بك في مخزون السعودية. باستخدامك لموقعنا، فإنك توافق على الشروط والأحكام التالية:</p>
        
        <h2>استخدام الموقع</h2>
        <ul>
            <li>يجب أن تكون بالغاً (18 عاماً أو أكثر) لاستخدام الموقع</li>
            <li>يجب تقديم معلومات صحيحة ودقيقة</li>
            <li>ممنوع استخدام الموقع لأغراض غير قانونية</li>
        </ul>
        
        <h2>الأسعار والمنتجات</h2>
        <ul>
            <li>جميع الأسعار بالريال السعودي</li>
            <li>نحتفظ بالحق في تعديل الأسعار دون إشعار مسبق</li>
            <li>نبذل قصارى جهدنا لضمان دقة أوصاف المنتجات</li>
        </ul>
        
        <h2>الطلبات والدفع</h2>
        <ul>
            <li>الطلب ملزم بعد التأكيد</li>
            <li>نحتفظ بالحق في رفض أي طلب</li>
            <li>الدفع عند الاستلام</li>
        </ul>
        
        <h2>المسؤولية</h2>
        <p>لا نتحمل المسؤولية عن:</p>
        <ul>
            <li>أي أضرار ناتجة عن سوء استخدام المنتجات</li>
            <li>التأخير في التوصيل بسبب ظروف خارجة عن إرادتنا</li>
        </ul>
    '''),
    
    'shipping-policy.html': ('سياسة الشحن', '''
        <h2>مدة التوصيل</h2>
        <ul>
            <li>داخل الرياض: 1-2 يوم عمل</li>
            <li>المدن الرئيسية الأخرى: 2-3 أيام عمل</li>
            <li>المناطق النائية: 3-5 أيام عمل</li>
        </ul>
        
        <h2>تكلفة الشحن</h2>
        <ul>
            <li>الطلبات فوق 300 ريال: شحن مجاني</li>
            <li>الطلبات أقل من 300 ريال: 25 ريال</li>
        </ul>
        
        <h2>تتبع الشحنة</h2>
        <p>سيتم إرسال رسالة نصية تحتوي على رقم تتبع الشحنة بمجرد شحن طلبك.</p>
        
        <h2>عدم توفر المستلم</h2>
        <p>في حالة عدم توفر المستلم:</p>
        <ul>
            <li>سيتم محاولة التوصيل مرة أخرى في اليوم التالي</li>
            <li>بعد 3 محاولات فاشلة، سيتم إلغاء الطلب</li>
        </ul>
    '''),
    
    'return-policy.html': ('سياسة الاسترجاع والاستبدال', '''
        <h2>شروط الاسترجاع</h2>
        <p>يمكنك إرجاع المنتج خلال 14 يوماً من تاريخ الاستلام بشرط:</p>
        <ul>
            <li>أن يكون المنتج بحالته الأصلية</li>
            <li>عدم استخدام المنتج</li>
            <li>توفر العبوة والملحقات الأصلية</li>
            <li>توفر الفاتورة</li>
        </ul>
        
        <h2>المنتجات المستثناة</h2>
        <p>لا يمكن إرجاع:</p>
        <ul>
            <li>منتجات العناية الشخصية المفتوحة</li>
            <li>المنتجات الغذائية</li>
            <li>المنتجات التي تم تخصيصها</li>
        </ul>
        
        <h2>الاستبدال</h2>
        <p>يمكن استبدال المنتج بمنتج آخر من نفس القيمة أو أعلى خلال 14 يوماً.</p>
        
        <h2>إجراءات الإرجاع</h2>
        <ol>
            <li>التواصل مع خدمة العملاء</li>
            <li>إرسال صور للمنتج</li>
            <li>الحصول على موافقة الإرجاع</li>
            <li>شحن المنتج للعنوان المحدد</li>
            <li>استرداد المبلغ خلال 7-10 أيام عمل</li>
        </ol>
    '''),
    
    'refund-policy.html': ('سياسة الاسترداد', '''
        <h2>مدة الاسترداد</h2>
        <p>سيتم استرداد المبلغ خلال 7-10 أيام عمل من تاريخ استلام المنتج المرتجع.</p>
        
        <h2>طريقة الاسترداد</h2>
        <ul>
            <li>تحويل بنكي مباشر</li>
            <li>رصيد في المتجر</li>
            <li>نفس طريقة الدفع الأصلية (إن أمكن)</li>
        </ul>
        
        <h2>الرسوم</h2>
        <ul>
            <li>في حالة عيب في المنتج: استرداد كامل + تكلفة الشحن</li>
            <li>في حالة تغيير الرأي: استرداد قيمة المنتج فقط</li>
        </ul>
        
        <h2>الإلغاء</h2>
        <p>يمكن إلغاء الطلب مجاناً قبل الشحن. بعد الشحن تطبق سياسة الإرجاع.</p>
    '''),
    
    'contact.html': ('اتصل بنا', '''
        <div class="contact-info">
            <p><strong>📍 العنوان:</strong> الرياض، المملكة العربية السعودية</p>
            <p><strong>📱 الجوال:</strong> <a href="tel:+966XXXXXXXXX">+966 XX XXX XXXX</a></p>
            <p><strong>📧 البريد:</strong> <a href="mailto:info@mahkzoon-sa.com">info@mahkzoon-sa.com</a></p>
            <p><strong>⏰ ساعات العمل:</strong> السبت - الخميس: 9 صباحاً - 6 مساءً</p>
        </div>
        
        <h2>راسلنا</h2>
        <form style="max-width: 600px; margin: 30px auto;">
            <div class="form-group">
                <label>الاسم</label>
                <input type="text" required>
            </div>
            <div class="form-group">
                <label>البريد الإلكتروني</label>
                <input type="email" required>
            </div>
            <div class="form-group">
                <label>الموضوع</label>
                <input type="text" required>
            </div>
            <div class="form-group">
                <label>الرسالة</label>
                <textarea rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">إرسال</button>
        </form>
    ''')
}

# إنشاء الصفحات القانونية
for filename, (title, content) in legal_pages.items():
    legal_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - مخزون السعودية</title>
    <link rel="stylesheet" href="../css/style.css">
    <style>
        .legal-content {{
            max-width: 900px;
            margin: 40px auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            line-height: 1.8;
        }}
        .legal-content h1 {{
            color: var(--primary-color);
            margin-bottom: 30px;
        }}
        .legal-content h2 {{
            color: var(--secondary-color);
            margin: 25px 0 15px;
        }}
        .legal-content ul, .legal-content ol {{
            margin: 15px 0 15px 30px;
        }}
        .legal-content li {{
            margin-bottom: 10px;
        }}
        .contact-info {{
            background: var(--light-bg);
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        .form-group {{
            margin-bottom: 20px;
        }}
        .form-group label {{
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }}
        .form-group input,
        .form-group textarea {{
            width: 100%;
            padding: 12px;
            border: 2px solid var(--border-color);
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <h1><a href="../index.html">مخزون السعودية</a></h1>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="../index.html">الرئيسية</a></li>
                        <li><a href="../products.html">المنتجات</a></li>
                        <li><a href="../cart.html">السلة</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <div class="legal-content">
        <h1>{title}</h1>
        {content}
        
        <p style="margin-top: 40px; padding-top: 20px; border-top: 2px solid var(--border-color); color: #666;">
            آخر تحديث: نوفمبر 2025
        </p>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2025 مخزون السعودية. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    
    with open(f'store/legal/{filename}', 'w', encoding='utf-8') as f:
        f.write(legal_html)
    print(f"✓ تم إنشاء {filename}")

# 14. توليد صفحات المنتجات
print("\n" + "="*60)
print("📦 توليد صفحات المنتجات الفردية...")
print("="*60)

import random

saudi_names = [
    "عبدالله محمد", "فاطمة أحمد", "سارة عبدالعزيز", "خالد سعيد",
    "نورة إبراهيم", "محمد حسن", "مريم علي", "أحمد يوسف",
    "هند عبدالرحمن", "سلطان ناصر", "ريم فيصل", "عمر صالح",
    "لطيفة عبدالله", "فهد خالد", "منى سعود", "بندر أحمد"
]

comments = [
    "منتج ممتاز وجودة عالية، أنصح بالشراء بشدة",
    "جيد جداً، التوصيل كان سريع والمنتج كما في الوصف",
    "راضي عن المنتج والسعر مناسب جداً",
    "جودة ممتازة وسعر تنافسي، سأشتري مرة أخرى",
    "منتج رائع، يستحق التجربة والثمن",
    "وصل بسرعة وبحالة ممتازة، شكراً لكم",
    "أفضل من المتوقع بكثير، راضي جداً",
    "ممتاز للاستخدام اليومي، أنصح به",
    "جودة عالية والسعر ممتاز مقارنة بالمحلات",
    "تجربة شراء رائعة، المنتج يستحق"
]

for product in products:
    discount = round(((product['price'] - product['sale_price']) / product['price']) * 100)
    
    # توليد تقييمات
    num_reviews = random.randint(4, 7)
    reviews_html = ""
    
    for i in range(num_reviews):
        name = random.choice(saudi_names)
        rating = random.randint(4, 5)
        date = f"2025-11-{random.randint(10, 22)}"
        comment = random.choice(comments)
        
        reviews_html += f"""
        <div style="background: var(--light-bg); padding: 20px; border-radius: 8px; margin-bottom: 15px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <strong style="color: var(--primary-color);">{name}</strong>
                <span style="color: #999; font-size: 0.9rem;">{date}</span>
            </div>
            <div style="color: #ffa500; margin-bottom: 10px;">{"⭐" * rating}</div>
            <p>{comment}</p>
        </div>
        """
    
    product_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{product['title']} - متوفر بسعر {product['sale_price']} ريال في مخزون السعودية">
    <title>{product['title']} - مخزون السعودية</title>
    <link rel="stylesheet" href="../css/style.css">
    <style>
        .product-detail {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            margin: 40px auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
        }}
        .product-image img {{
            width: 100%;
            border-radius: 10px;
        }}
        .product-info h1 {{
            color: var(--primary-color);
            margin-bottom: 20px;
        }}
        .quantity-selector {{
            display: flex;
            align-items: center;
            gap: 15px;
            margin: 25px 0;
        }}
        .quantity-selector button {{
            width: 40px;
            height: 40px;
            border: 2px solid var(--primary-color);
            background: white;
            color: var(--primary-color);
            font-size: 1.2rem;
            border-radius: 5px;
            cursor: pointer;
        }}
        .quantity-selector input {{
            width: 60px;
            text-align: center;
            padding: 10px;
            border: 2px solid var(--border-color);
            border-radius: 5px;
        }}
        .product-actions {{
            display: flex;
            gap: 15px;
            margin: 30px 0;
        }}
        .info-box {{
            background: var(--light-bg);
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        .info-box p {{
            margin: 10px 0;
        }}
        @media (max-width: 768px) {{
            .product-detail {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <h1><a href="../index.html">مخزون السعودية</a></h1>
                </div>
                <nav class="main-nav">
                    <ul>
                        <li><a href="../index.html">الرئيسية</a></li>
                        <li><a href="../products.html">المنتجات</a></li>
                        <li><a href="../cart.html">السلة (<span id="cart-count">0</span>)</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <div class="container product-detail">
        <div class="product-image">
            <img src="{product['image_link']}" alt="{product['title']}">
        </div>
        
        <div class="product-info">
            <h1>{product['title']}</h1>
            
            <div class="product-price" style="margin: 20px 0;">
                <span class="old-price" style="font-size: 1.2rem;">{product['price']} ر.س</span>
                <span class="current-price" style="font-size: 1.8rem;">{product['sale_price']} ر.س</span>
                <span class="discount-badge">-{discount}%</span>
            </div>
            
            <p style="line-height: 1.8; color: #666; margin: 20px 0;">
                {product['title']} - منتج عالي الجودة متوفر الآن بسعر مميز.
                احصل عليه الآن واستمتع بأفضل العروض والجودة العالية.
            </p>
            
            <div class="quantity-selector">
                <label style="font-weight: 600;">الكمية:</label>
                <button onclick="decreaseQty()">-</button>
                <input type="number" id="qty" value="1" min="1">
                <button onclick="increaseQty()">+</button>
            </div>
            
            <div class="product-actions">
                <button class="btn btn-primary" onclick="addToCartWithQty()" style="flex: 1; padding: 15px;">
                    أضف للسلة
                </button>
                <button class="btn" onclick="buyNow()" style="flex: 1; padding: 15px; background: var(--secondary-color); color: white;">
                    اشتر الآن
                </button>
            </div>
            
            <div class="info-box">
                <p>✅ شحن مجاني للطلبات فوق 300 ريال</p>
                <p>🔄 إمكانية الإرجاع خلال 14 يوم</p>
                <p>🚚 توصيل سريع خلال 2-4 أيام عمل</p>
                <p>💳 الدفع عند الاستلام</p>
            </div>
        </div>
    </div>
    
    <div class="container" style="margin: 50px auto;">
        <div style="background: white; padding: 40px; border-radius: 10px;">
            <h2 style="color: var(--primary-color); margin-bottom: 30px;">تقييمات العملاء</h2>
            {reviews_html}
        </div>
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2025 مخزون السعودية. جميع الحقوق محفوظة.</p>
            </div>
        </div>
    </footer>

    <script src="../js/products.js"></script>
    <script src="../js/cart.js"></script>
    <script>
        const productId = {product['id']};
        
        function increaseQty() {{
            const input = document.getElementById('qty');
            input.value = parseInt(input.value) + 1;
        }}
        
        function decreaseQty() {{
            const input = document.getElementById('qty');
            if (parseInt(input.value) > 1) {{
                input.value = parseInt(input.value) - 1;
            }}
        }}
        
        function addToCartWithQty() {{
            const qty = parseInt(document.getElementById('qty').value);
            loadProducts().then(() => {{
                if (cart.addItem(productId, qty)) {{
                    alert('تمت الإضافة للسلة بنجاح!');
                    updateCartCount();
                }}
            }});
        }}
        
        function buyNow() {{
            addToCartWithQty();
            setTimeout(() => {{
                window.location.href = '../checkout.html';
            }}, 500);
        }}
        
        loadProducts().then(() => updateCartCount());
    </script>
</body>
</html>
"""
    
    filename = f'store/products/product-{product["id"]}.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(product_html)
    
    if product['id'] % 50 == 0:
        print(f"✓ تم إنشاء {product['id']} صفحة...")

print(f"✓ تم إنشاء {len(products)} صفحة منتج")

# الانتهاء
print("\n" + "="*60)
print("✅ تم إنشاء المتجر بنجاح!")
print("="*60)
print(f"\n📂 الموقع في المجلد: store/")
print(f"📊 عدد المنتجات: {len(products)}")
print(f"\n🌐 لفتح المتجر:")
print(f"   افتح الملف: store/index.html")
print("\n💡 ملاحظة: لا تنسى تعديل رقم الواتساب في ملف checkout.html")
print("="*60)
