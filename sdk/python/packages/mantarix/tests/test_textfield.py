import mantarix as mx
from mantarix.core.protocol import Command


def test_instance_no_attrs_set():
    r = mx.TextField()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["textfield"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_text_align_enum():
    r = mx.TextField(text_align=mx.TextAlign.LEFT)
    assert isinstance(r.text_align, mx.TextAlign)
    assert isinstance(r._get_attr("textAlign"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["textalign"] == "left"


def test_text_align_str():
    r = mx.TextField(text_align="left")
    assert isinstance(r.text_align, str)
    assert isinstance(r._get_attr("textAlign"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["textalign"] == "left"


def test_keyboard_type_enum():
    r = mx.TextField()
    assert r.keyboard_type is None
    assert r._get_attr("keyboardType") is None

    r = mx.TextField(keyboard_type=mx.KeyboardType.NONE)
    assert isinstance(r.keyboard_type, mx.KeyboardType)
    assert r.keyboard_type == mx.KeyboardType.NONE
    assert r._get_attr("keyboardType") == "none"

    r = mx.TextField(keyboard_type="phone")
    assert isinstance(r.keyboard_type, str)
    assert r._get_attr("keyboardType") == "phone"


def test_capitalization_enum():
    r = mx.TextField()
    assert r.capitalization is None
    assert r._get_attr("capitalization") is None

    r = mx.TextField(capitalization=mx.TextCapitalization.WORDS)
    assert isinstance(r.capitalization, mx.TextCapitalization)
    assert r.capitalization == mx.TextCapitalization.WORDS
    assert r._get_attr("capitalization") == "words"

    r = mx.TextField(capitalization="sentences")
    assert isinstance(r.capitalization, str)
    assert r._get_attr("capitalization") == "sentences"


def test_border_enum():
    r = mx.TextField()
    assert r.border is None
    assert r._get_attr("border") is None

    r = mx.TextField(border=mx.InputBorder.OUTLINE)
    assert isinstance(r.border, mx.InputBorder)
    assert r.border == mx.InputBorder.OUTLINE
    assert r._get_attr("border") == "outline"

    r = mx.TextField(border="none")
    assert isinstance(r.border, str)
    assert r._get_attr("border") == "none"


def test_bgcolor_sets_filled():
    r = mx.TextField()
    r.bgcolor = mx.Colors.BLUE
    cmd = r._build_add_commands()
    assert r.filled is not None and r.filled
    assert r._get_attr("filled") is not None and r._get_attr("filled")

    r = mx.TextField(bgcolor=mx.Colors.BLUE)
    cmd = r._build_add_commands()
    assert r.filled is not None and r.filled
    assert r._get_attr("filled") is not None and r._get_attr("filled")

    r = mx.TextField(bgcolor=mx.Colors.BLUE, filled=True)
    cmd = r._build_add_commands()
    assert r.filled is not None and r.filled
    assert r._get_attr("filled") is not None and r._get_attr("filled")

    r = mx.TextField(bgcolor=mx.Colors.BLUE, filled=False)
    cmd = r._build_add_commands()
    assert r.filled is not None and not r.filled
    assert r._get_attr("filled") is not None and not r._get_attr("filled")
