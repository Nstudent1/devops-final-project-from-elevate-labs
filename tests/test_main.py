from app.main import home

def test_home():
    assert home() == {"message": "CI/CD Pipeline Working!"}
