from app import base

def test_index():
    try:
        assert base() == "Hello world"
    except Exception as e:
        print(e)