from app.db import get_db


def test_checkout_redirect_when_cart_empty(client):
    """Test that checkout redirects to cart if no products have been selected."""
    response = client.get('/checkout', follow_redirects=True)
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Your shopping cart is empty' in html


def test_checkout_form_validation_errors(client):
    """Test customer form validation with invalid/missing details."""
    # Add product 1 to cart
    client.post('/cart/add/1', data={'quantity': 1})

    # Submit with empty fields
    response = client.post('/checkout', data={
        'customer_name': '',
        'customer_email': 'invalid-email',
        'customer_phone': '',
        'shipping_address': ''
    }, follow_redirects=True)

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Please provide a valid full name' in html
    assert 'Please provide a valid email address' in html


def test_order_placement_and_database_persistence(app, client):
    """Test full checkout flow with INR pricing, SQLite persistence, and receipt rendering."""
    # 1. Add products to cart
    # NovaPulse Pro Smartwatch (₹2,999 * 2 = ₹5,998)
    client.post('/cart/add/1', data={'quantity': 2})
    # ApexKey Mechanical Keyboard (₹2,199 * 1 = ₹2,199)
    client.post('/cart/add/3', data={'quantity': 1})

    # 2. Submit valid Indian checkout form
    response = client.post('/checkout', data={
        'customer_name': 'Atharv Kothawale',
        'customer_email': 'atharv@college.edu',
        'customer_phone': '9876543210',
        'shipping_address': 'Flat 402, Shivajinagar, Pune, Maharashtra - 411005',
        'payment_method': 'Cash on Delivery'
    }, follow_redirects=True)

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert 'Order Confirmed!' in html
    assert 'Atharv Kothawale' in html
    assert 'NovaPulse Pro Smartwatch' in html
    assert 'ApexKey RGB Mechanical Keyboard' in html
    assert 'CONFIRMED' in html
    assert '₹8,606.85' in html
    assert '$' not in html

    # 3. Verify SQLite persistence in actual database
    with app.app_context():
        db = get_db()
        order = db.execute("SELECT * FROM orders WHERE customer_name = ?", ('Atharv Kothawale',)).fetchone()
        assert order is not None
        assert order['customer_email'] == 'atharv@college.edu'
        assert abs(order['total_amount'] - 8606.85) < 0.01

        # Verify order items
        order_items = db.execute("SELECT * FROM order_items WHERE order_id = ?", (order['id'],)).fetchall()
        assert len(order_items) == 2
        names = [item['product_name'] for item in order_items]
        assert 'NovaPulse Pro Smartwatch' in names
        assert 'ApexKey RGB Mechanical Keyboard' in names
        
        # Verify unit prices in INR
        for item in order_items:
            if item['product_name'] == 'NovaPulse Pro Smartwatch':
                assert item['unit_price'] == 2999.0
            elif item['product_name'] == 'ApexKey RGB Mechanical Keyboard':
                assert item['unit_price'] == 2199.0


def test_order_confirmation_404(client):
    """Test that requesting non-existent order tracking returns 404."""
    response = client.get('/order/confirmation/SS-FAKE-999999')
    assert response.status_code == 404
