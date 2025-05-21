from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.NavigationBar()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["navigationbar"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_extension_set_enum():
    r = mx.NavigationBar()
    assert r.label_behavior is None
    assert r._get_attr("labelBehavior") is None

    r = mx.NavigationBar(label_behavior=mx.NavigationBarLabelBehavior.ALWAYS_SHOW)
    assert isinstance(r.label_behavior, mx.NavigationBarLabelBehavior)
    assert r.label_behavior == mx.NavigationBarLabelBehavior.ALWAYS_SHOW
    assert r._get_attr("labelBehavior") == "alwaysShow"

    r = mx.NavigationBar(label_behavior="alwaysHide")
    assert isinstance(r.label_behavior, str)
    assert r._get_attr("labelBehavior") == "alwaysHide"
