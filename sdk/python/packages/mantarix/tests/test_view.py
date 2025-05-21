from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.View()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["view"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_horizontal_alignment_enum():
    r = mx.View(horizontal_alignment=mx.CrossAxisAlignment.STRETCH)
    assert isinstance(r.horizontal_alignment, mx.CrossAxisAlignment)
    assert isinstance(r._get_attr("horizontalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["horizontalalignment"] == "stretch"


def test_horizontal_alignment_str():
    r = mx.View(horizontal_alignment="center")
    assert isinstance(r.horizontal_alignment, str)
    assert isinstance(r._get_attr("horizontalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["horizontalalignment"] == "center"


def test_vertical_alignment_enum():
    r = mx.View(vertical_alignment=mx.MainAxisAlignment.CENTER)
    assert isinstance(r.vertical_alignment, mx.MainAxisAlignment)
    assert isinstance(r._get_attr("verticalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["verticalalignment"] == "center"


def test_vertical_alignment_str():
    r = mx.View(vertical_alignment="center")
    assert isinstance(r.vertical_alignment, str)
    assert isinstance(r._get_attr("verticalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["verticalalignment"] == "center"


def test_scroll_enum():
    r = mx.View()
    assert r.scroll is None
    assert r._get_attr("scroll") is None

    r = mx.View(scroll=mx.ScrollMode.ALWAYS)
    assert isinstance(r.scroll, mx.ScrollMode)
    assert r.scroll == mx.ScrollMode.ALWAYS
    assert r._get_attr("scroll") == "always"

    r = mx.View(scroll="adaptive")
    assert isinstance(r.scroll, str)
    assert r._get_attr("scroll") == "adaptive"

    r = mx.View(scroll=True)
    assert isinstance(r.scroll, bool)
    assert r._get_attr("scroll") == "auto"

    r = mx.View(scroll=False)
    assert isinstance(r.scroll, bool)
    assert r._get_attr("scroll") is None
