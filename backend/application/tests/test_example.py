from ....backend.application.database import DB_URL


def test_db_url():
    x = "postgresql://postgres:PW@backend_db:5432/postgres"
    assert DB_URL.format(pw="PW") == x
