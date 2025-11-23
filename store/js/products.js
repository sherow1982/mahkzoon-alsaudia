// تحميل المنتجات
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
