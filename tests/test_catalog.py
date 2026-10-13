def test_homepage_catalog_listing(client):
    """Test that catalog lists categories, products, and prices in Indian Rupees (₹)."""
    response = client.get('/')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'ShopSphere' in html
    assert 'Electronics' in html
    assert 'NovaPulse Pro Smartwatch' in html
    assert '₹2,999' in html
    assert '$' not in html


def test_category_filter(client):
    """Test filtering products by category slug."""
    response = client.get('/?category=electronics')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'NovaPulse Pro Smartwatch' in html
    assert 'AcousticZen ANC Headphones' in html
    assert 'Classic Vintage Washed Denim Jacket' not in html


def test_product_search_success(client):
    """Test searching for products with matching keywords."""
    response = client.get('/?q=Webcam')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'StreamVision 4K Ultra HD Webcam' in html
    assert '₹3,499' in html
    assert 'Denim Jacket' not in html


def test_product_search_empty(client):
    """Test searching for non-existent keywords returns empty state."""
    response = client.get('/?q=NonExistentDevice12345')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'No Products Found' in html


def test_product_detail_page(client):
    """Test viewing a specific product's detail page with INR price and tax info."""
    response = client.get('/product/novapulse-pro-smartwatch')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'NovaPulse Pro Smartwatch' in html
    assert '₹2,999' in html
    assert 'Inclusive of all taxes' in html
    assert 'In Stock' in html
    assert 'Product Overview' in html
    assert '$' not in html


def test_product_detail_404(client):
    """Test viewing a non-existent product slug returns HTTP 404."""
    response = client.get('/product/non-existent-product')
    assert response.status_code == 404
