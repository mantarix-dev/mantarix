import mantarix as mx


def test_material_icons_random_with_weights_and_exclude():
    """Test random material icon selection with weights and exclusion list."""
    results = [
        mx.Icons.random(
            exclude=[mx.Icons.FAVORITE],
            weights={mx.Icons.SCHOOL: 150},
        )
        for _ in range(1000)
    ]
    assert mx.Icons.FAVORITE not in results
    assert mx.Icons.SCHOOL in results


def test_cupertino_icons_random_with_weights_and_exclude():
    """Test random cupertino icon selection with weights and exclusion list."""
    results = [
        mx.CupertinoIcons.random(
            exclude=[mx.CupertinoIcons.CAMERA],
            weights={mx.CupertinoIcons.TABLE: 150},
        )
        for _ in range(1000)
    ]
    assert mx.CupertinoIcons.CAMERA not in results
    assert mx.CupertinoIcons.TABLE in results
