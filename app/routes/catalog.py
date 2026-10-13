from flask import Blueprint, render_template, request, abort
from app.db import get_db

catalog_bp = Blueprint('catalog', __name__)


@catalog_bp.route('/')
def index():
    """ShopSphere Homepage - supports category filtering and live search queries."""
    db = get_db()
    
    search_query = request.args.get('q', '').strip()
    category_slug = request.args.get('category', '').strip()
    
    # Retrieve all categories for navigation
    categories = db.execute("SELECT * FROM categories ORDER BY name ASC").fetchall()
    
    # Build dynamic query for products
    sql = """
        SELECT p.*, c.name AS category_name, c.slug AS category_slug
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE 1=1
    """
    params = []
    
    if category_slug:
        sql += " AND c.slug = ?"
        params.append(category_slug)
        
    if search_query:
        sql += " AND (p.name LIKE ? OR p.description LIKE ?)"
        wildcard = f"%{search_query}%"
        params.extend([wildcard, wildcard])
        
    sql += " ORDER BY p.id ASC"
    products = db.execute(sql, params).fetchall()
    
    active_category = None
    if category_slug:
        for cat in categories:
            if cat['slug'] == category_slug:
                active_category = cat
                break

    return render_template(
        'index.html',
        categories=categories,
        products=products,
        search_query=search_query,
        category_slug=category_slug,
        active_category=active_category
    )


@catalog_bp.route('/product/<slug>')
def product_detail(slug):
    """Product detail page with full description, stock status, and related products."""
    db = get_db()
    
    product = db.execute(
        """
        SELECT p.*, c.name AS category_name, c.slug AS category_slug
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE p.slug = ?
        """,
        (slug,)
    ).fetchone()
    
    if not product:
        abort(404)
        
    # Related products from the same category
    related_products = db.execute(
        """
        SELECT p.*, c.name AS category_name, c.slug AS category_slug
        FROM products p
        JOIN categories c ON p.category_id = c.id
        WHERE p.category_id = ? AND p.id != ?
        LIMIT 4
        """,
        (product['category_id'], product['id'])
    ).fetchall()
    
    return render_template(
        'product.html',
        product=product,
        related_products=related_products
    )
