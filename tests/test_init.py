from app.db import get_db


def test_database_schema_and_seed(app):
    """Test that all tables are created and seeded with sample products."""
    with app.app_context():
        db = get_db()
        
        # Verify categories count
        cat_count = db.execute("SELECT COUNT(*) AS count FROM categories").fetchone()['count']
        assert cat_count == 4, f"Expected 4 categories, found {cat_count}"

        # Verify products count
        prod_count = db.execute("SELECT COUNT(*) AS count FROM products").fetchone()['count']
        assert prod_count >= 10, f"Expected at least 10 products, found {prod_count}"

        # Verify table structure for orders and order_items
        tables = [row['name'] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
        assert 'categories' in tables
        assert 'products' in tables
        assert 'orders' in tables
        assert 'order_items' in tables


def test_health_check_endpoint(client):
    """Test the /api/health endpoint returns 200 with accurate status and counts."""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'ShopSphere'
    assert data['database'] == 'connected'
    assert data['categories_loaded'] == 4
    assert data['products_loaded'] >= 10


def test_homepage_rendering(client):
    """Test that the homepage renders successfully and includes ShopSphere branding and products."""
    response = client.get('/')
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'ShopSphere' in html
    assert 'NovaPulse Pro Smartwatch' in html
    assert 'AcousticZen ANC Headphones' in html
