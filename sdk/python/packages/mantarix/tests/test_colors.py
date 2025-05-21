import mantarix as mx


def test_material_colors_random_with_weights_and_exclude():
    """Test random material color selection with weights and exclusion list."""
    results = [
        mx.Colors.random(
            exclude=[mx.Colors.RED],
            weights={mx.Colors.BLUE: 150},
        )
        for _ in range(1000)
    ]
    assert mx.Colors.RED not in results
    assert mx.Colors.BLUE in results


def test_cupertino_colors_random_with_weights_and_exclude():
    """Test random cupertino color selection with weights and exclusion list."""
    results = [
        mx.CupertinoColors.random(
            exclude=[mx.CupertinoColors.SYSTEM_RED],
            weights={mx.CupertinoColors.SEPARATOR: 150},
        )
        for _ in range(1000)
    ]
    assert mx.CupertinoColors.SYSTEM_RED not in results
    assert mx.CupertinoColors.SEPARATOR in results
