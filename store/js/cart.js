// إدارة السلة
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
