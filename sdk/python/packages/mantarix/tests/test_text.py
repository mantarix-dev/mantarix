import mantarix as mx
from mantarix.core.protocol import Command


def test_instance_no_attrs_set():
    r = mx.Text()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["text"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_text_align_enum():
    r = mx.Text()
    assert r.text_align is None
    assert r._get_attr("textAlign") is None

    r = mx.Text(text_align=mx.TextAlign.RIGHT)
    assert isinstance(r.text_align, mx.TextAlign)
    assert r.text_align == mx.TextAlign.RIGHT
    assert r._get_attr("textAlign") == "right"

    r = mx.Text(text_align="left")
    assert isinstance(r.text_align, str)
    assert r._get_attr("textAlign") == "left"


def test_text_style_enum():
    r = mx.Text()
    assert r.style is None
    assert r._get_attr("style") is None

    r = mx.Text(style=mx.TextThemeStyle.DISPLAY_LARGE)
    assert isinstance(r.style, mx.TextThemeStyle)
    assert r.style == mx.TextThemeStyle.DISPLAY_LARGE
    assert r._get_attr("style") == "displayLarge"

    r = mx.Text(style="bodyMedium")
    assert isinstance(r.style, str)
    assert r._get_attr("style") == "bodyMedium"


def test_text_overflow_enum():
    r = mx.Text()
    assert r.overflow is None
    assert r._get_attr("overflow") is None

    r = mx.Text(overflow=mx.TextOverflow.ELLIPSIS)
    assert isinstance(r.overflow, mx.TextOverflow)
    assert r.overflow == mx.TextOverflow.ELLIPSIS
    assert r._get_attr("overflow") == "ellipsis"

    r = mx.Text(overflow="fade")
    assert isinstance(r.overflow, str)
    assert r._get_attr("overflow") == "fade"


def test_weight_enum():
    r = mx.Text()
    assert r.weight is None
    assert r._get_attr("weight") is None

    r = mx.Text(weight=mx.FontWeight.BOLD)
    assert isinstance(r.weight, mx.FontWeight)
    assert r.weight == mx.FontWeight.BOLD
    assert r._get_attr("weight") == "bold"

    r = mx.Text(weight="w100")
    assert isinstance(r.weight, str)
    assert r._get_attr("weight") == "w100"
