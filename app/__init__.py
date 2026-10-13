import os
from flask import Flask, session
from app.config import Config


def create_app(test_config=None):
    """Application factory for ShopSphere."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    if test_config:
        app.config.from_mapping(test_config)

    # Ensure the instance directory exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Register Database hooks
    from app import db
    db.init_app(app)

    # Register custom Jinja filters
    from app.utils import format_inr
    app.jinja_env.filters['inr'] = format_inr

    # Register Blueprints
    from app.routes.main import main_bp
    from app.routes.catalog import catalog_bp
    from app.routes.cart import cart_bp
    from app.routes.checkout import checkout_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(catalog_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)

    @app.context_processor
    def inject_global_vars():
        cart = session.get('cart', {})
        cart_count = sum(int(qty) for qty in cart.values() if isinstance(qty, (int, str)) and str(qty).isdigit())
        return {
            'app_name': 'ShopSphere',
            'project_title': 'Distributed Commerce Platform: A DevOps-Driven E-Commerce Application',
            'cart_count': cart_count
        }

    return app
