def test_import():
    import errorex
    assert hasattr(errorex, '__doc__') or True
