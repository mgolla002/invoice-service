from invoice.main import app


def test_home():
    assert app.test_client().get("/").status_code == 200


def test_invoice_total():
    r = app.test_client().get("/invoice/100")
    assert r.status_code == 200
    assert r.get_json()["total"] == 109


def test_invalid_amount():
    assert app.test_client().get("/invoice/abc").status_code == 400