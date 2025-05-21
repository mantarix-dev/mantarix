from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.Row()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["row"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_alignment_enum():
    r = mx.Row(alignment=mx.MainAxisAlignment.SPACE_AROUND)
    assert isinstance(r.alignment, mx.MainAxisAlignment)
    assert isinstance(r._get_attr("alignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["alignment"] == "spaceAround"


def test_alignment_str():
    r = mx.Row(alignment="center")
    assert isinstance(r.alignment, str)
    assert isinstance(r._get_attr("alignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["alignment"] == "center"


def test_vertical_alignment_enum():
    r = mx.Row(vertical_alignment=mx.CrossAxisAlignment.STRETCH)
    assert isinstance(r.vertical_alignment, mx.CrossAxisAlignment)
    assert isinstance(r._get_attr("verticalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["verticalalignment"] == "stretch"


def test_vertical_alignment_str():
    r = mx.Row(vertical_alignment="center")
    assert isinstance(r.vertical_alignment, str)
    assert isinstance(r._get_attr("verticalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["verticalalignment"] == "center"


def test_scroll_enum():
    r = mx.Row()
    assert r.scroll is None
    assert r._get_attr("scroll") is None

    r = mx.Row(scroll=mx.ScrollMode.ALWAYS)
    assert isinstance(r.scroll, mx.ScrollMode)
    assert r.scroll == mx.ScrollMode.ALWAYS
    assert r._get_attr("scroll") == "always"

    r = mx.Row(scroll="adaptive")
    assert isinstance(r.scroll, str)
    assert r._get_attr("scroll") == "adaptive"

    r = mx.Row(scroll=True)
    assert isinstance(r.scroll, bool)
    assert r._get_attr("scroll") == "auto"

    r = mx.Row(scroll=False)
    assert isinstance(r.scroll, bool)
    assert r._get_attr("scroll") is None
