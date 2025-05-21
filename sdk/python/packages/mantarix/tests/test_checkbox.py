from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.Checkbox()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["checkbox"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_label_position_enum():
    r = mx.Checkbox(label_position=mx.LabelPosition.LEFT)
    assert isinstance(r.label_position, mx.LabelPosition)
    assert isinstance(r._get_attr("labelPosition"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["labelposition"] == "left"


def test_label_position_str():
    r = mx.Checkbox(label_position="left")
    assert isinstance(r.label_position, str)
    assert isinstance(r._get_attr("labelPosition"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["labelposition"] == "left"
