from flask import Blueprint, jsonify, render_template
from app.db import get_db

main_bp = Blueprint('main', __name__)


@main_bp.route('/api/health')
def health():
    """Health check endpoint for Docker container and Kubernetes liveness/readiness probes."""
    try:
        db = get_db()
        cat_count = db.execute("SELECT COUNT(*) AS count FROM categories").fetchone()['count']
        prod_count = db.execute("SELECT COUNT(*) AS count FROM products").fetchone()['count']
        
        return jsonify({
            "status": "healthy",
            "service": "ShopSphere",
            "version": "1.0.0",
            "database": "connected",
            "categories_loaded": cat_count,
            "products_loaded": prod_count
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500
