import mantarix as mx
from mantarix.core.protocol import Command


def test_instance_no_attrs_set():
    r = mx.NavigationRail()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["navigationrail"],
            attrs={"rtl": "false"},
            commands=[],
        )
    ], "Test failed"


def test_extension_set_enum():
    r = mx.NavigationRail()
    assert r.label_type is None
    assert r._get_attr("labelType") is None

    r = mx.NavigationRail(label_type=mx.NavigationRailLabelType.SELECTED)
    assert isinstance(r.label_type, mx.NavigationRailLabelType)
    assert r.label_type == mx.NavigationRailLabelType.SELECTED
    assert r._get_attr("labelType") == "selected"

    r = mx.NavigationRail(label_type="none")
    assert isinstance(r.label_type, str)
    assert r._get_attr("labelType") == "none"
