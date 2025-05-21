from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.Column()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["column"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_alignment_enum():
    r = mx.Column(alignment=mx.MainAxisAlignment.SPACE_AROUND)
    assert isinstance(r.alignment, mx.MainAxisAlignment)
    assert isinstance(r._get_attr("alignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["alignment"] == "spaceAround"


def test_alignment_str():
    r = mx.Column(alignment="center")
    assert isinstance(r.alignment, str)
    assert isinstance(r._get_attr("alignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["alignment"] == "center"


def test_horizontal_alignment_enum():
    r = mx.Column(horizontal_alignment=mx.CrossAxisAlignment.STRETCH)
    assert isinstance(r.horizontal_alignment, mx.CrossAxisAlignment)
    assert isinstance(r._get_attr("horizontalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["horizontalalignment"] == "stretch"


def test_horizontal_alignment_str():
    r = mx.Column(horizontal_alignment="center")
    assert isinstance(r.horizontal_alignment, str)
    assert isinstance(r._get_attr("horizontalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["horizontalalignment"] == "center"


def test_scroll_enum():
    r = mx.Column()
    assert r.scroll is None
    assert r._get_attr("scroll") is None

    r = mx.Column(scroll=mx.ScrollMode.ALWAYS)
    assert isinstance(r.scroll, mx.ScrollMode)
    assert r.scroll == mx.ScrollMode.ALWAYS
    assert r._get_attr("scroll") == "always"

    r = mx.Column(scroll="adaptive")
    assert isinstance(r.scroll, str)
    assert r._get_attr("scroll") == "adaptive"

    r = mx.Column(scroll=True)
    assert isinstance(r.scroll, bool)
    assert r._get_attr("scroll") == "auto"

    r = mx.Column(scroll=False)
    assert isinstance(r.scroll, bool)
    assert r._get_attr("scroll") is None
