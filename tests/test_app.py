from src.main import show_hello


def test_hello():
    assert show_hello() == '<p>hello world<p>'
