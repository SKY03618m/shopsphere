import os
import tempfile
import pytest
from app import create_app
from app.db import init_db, seed_db


@pytest.fixture
def app():
    """Create and configure a clean application instance for testing."""
    db_fd, db_path = tempfile.mkstemp(suffix='_test.db')

    test_app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
        'SECRET_KEY': 'test-secret-key'
    })

    with test_app.app_context():
        init_db()
        seed_db()

    yield test_app

    os.close(db_fd)
    if os.path.exists(db_path):
        try:
            os.unlink(db_path)
        except OSError:
            pass



@pytest.fixture
def client(app):
    """Test client for issuing HTTP requests."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """CLI runner for testing Flask CLI commands."""
    return app.test_cli_runner()
