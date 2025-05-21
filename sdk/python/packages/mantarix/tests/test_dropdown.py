from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.Dropdown()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["dropdown"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_border_enum():
    r = mx.Dropdown()
    assert r.border is None
    assert r._get_attr("border") is None

    r = mx.Dropdown(border=mx.InputBorder.OUTLINE)
    assert isinstance(r.border, mx.InputBorder)
    assert r.border == mx.InputBorder.OUTLINE
    assert r._get_attr("border") == "outline"

    r = mx.Dropdown(border="none")
    assert isinstance(r.border, str)
    assert r._get_attr("border") == "none"
