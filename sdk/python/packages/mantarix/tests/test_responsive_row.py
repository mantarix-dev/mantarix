from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.ResponsiveRow()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["responsiverow"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_alignment_enum():
    r = mx.ResponsiveRow(alignment=mx.MainAxisAlignment.SPACE_AROUND)
    assert isinstance(r.alignment, mx.MainAxisAlignment)
    assert isinstance(r._get_attr("alignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["alignment"] == "spaceAround"


def test_alignment_str():
    r = mx.ResponsiveRow(alignment="center")
    assert isinstance(r.alignment, str)
    assert isinstance(r._get_attr("alignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["alignment"] == "center"


def test_vertical_alignment_enum():
    r = mx.ResponsiveRow(vertical_alignment=mx.CrossAxisAlignment.STRETCH)
    assert isinstance(r.vertical_alignment, mx.CrossAxisAlignment)
    assert isinstance(r._get_attr("verticalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["verticalalignment"] == "stretch"


def test_vertical_alignment_str():
    r = mx.ResponsiveRow(vertical_alignment="center")
    assert isinstance(r.vertical_alignment, str)
    assert isinstance(r._get_attr("verticalAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["verticalalignment"] == "center"
