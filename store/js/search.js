// البحث
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
