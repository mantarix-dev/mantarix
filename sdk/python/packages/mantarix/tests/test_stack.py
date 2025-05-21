from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.Stack()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["stack"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_clip_behavior_enum():
    r = mx.Stack()
    assert r.clip_behavior is None
    assert r._get_attr("clipBehavior") is None

    r = mx.Stack(clip_behavior=mx.ClipBehavior.ANTI_ALIAS)
    assert isinstance(r.clip_behavior, mx.ClipBehavior)
    assert r.clip_behavior == mx.ClipBehavior.ANTI_ALIAS
    assert r._get_attr("clipBehavior") == "antiAlias"

    r = mx.Stack(clip_behavior="none")
    assert isinstance(r.clip_behavior, str)
    assert r._get_attr("clipBehavior") == "none"
