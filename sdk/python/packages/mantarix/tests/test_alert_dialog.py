import mantarix as mx
from mantarix.core.protocol import Command


def test_instance_no_attrs_set():
    r = mx.AlertDialog(title=mx.Text("Title"))
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["alertdialog"],
            attrs={"modal": "false", "open": "false"},
            commands=[],
        ),
        Command(
            indent=2,
            name=None,
            values=["text"],
            attrs={"n": "title", "value": "Title"},
            commands=[],
        ),
    ], "Test failed"


def test_alignment_enum():
    r = mx.AlertDialog(
        title=mx.Text("Title"), actions_alignment=mx.MainAxisAlignment.SPACE_AROUND
    )
    assert isinstance(r.actions_alignment, mx.MainAxisAlignment)
    assert isinstance(r._get_attr("actionsAlignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["actionsalignment"] == "spaceAround"


def test_alignment_str():
    r = mx.AlertDialog(title=mx.Text("Title"), actions_alignment="center")
    assert isinstance(r.actions_alignment, str)
    assert isinstance(r._get_attr("actionsalignment"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["actionsalignment"] == "center"
