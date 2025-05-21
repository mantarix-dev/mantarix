import mantarix as mx
from mantarix.core.protocol import Command


def test_instance_no_attrs_set():
    r = mx.AnimatedSwitcher(content=mx.Text("Hello!"))
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["animatedswitcher"],
            attrs={},
            commands=[],
        ),
        Command(
            indent=2,
            name=None,
            values=["text"],
            attrs={"n": "content", "value": "Hello!"},
            commands=[],
        ),
    ], "Test failed"


def test_switch_in_curve_enum():
    r = mx.AnimatedSwitcher(content=mx.Text("Hello!"))
    assert r.switch_in_curve is None
    assert r._get_attr("switchInCurve") is None

    r = mx.AnimatedSwitcher(
        content=mx.Text("Hello!"), switch_in_curve=mx.AnimationCurve.BOUNCE_IN
    )
    assert isinstance(r.switch_in_curve, mx.AnimationCurve)
    assert r.switch_in_curve == mx.AnimationCurve.BOUNCE_IN
    assert r._get_attr("switchInCurve") == "bounceIn"

    r = mx.AnimatedSwitcher(content=mx.Text("Hello!"), switch_in_curve="easeIn")
    assert isinstance(r.switch_in_curve, str)
    assert r._get_attr("switchInCurve") == "easeIn"


def test_switch_out_curve_enum():
    r = mx.AnimatedSwitcher(content=mx.Text("Hello!"))
    assert r.switch_out_curve is None
    assert r._get_attr("switchOutCurve") is None

    r = mx.AnimatedSwitcher(
        content=mx.Text("Hello!"), switch_out_curve=mx.AnimationCurve.BOUNCE_IN
    )
    assert isinstance(r.switch_out_curve, mx.AnimationCurve)
    assert r.switch_out_curve == mx.AnimationCurve.BOUNCE_IN
    assert r._get_attr("switchOutCurve") == "bounceIn"

    r = mx.AnimatedSwitcher(content=mx.Text("Hello!"), switch_out_curve="easeIn")
    assert isinstance(r.switch_out_curve, str)
    assert r._get_attr("switchOutCurve") == "easeIn"


def test_transition_enum():
    r = mx.AnimatedSwitcher(content=mx.Text("Hello!"))
    assert r.transition is None
    assert r._get_attr("transition") is None

    r = mx.AnimatedSwitcher(
        content=mx.Text("Hello!"), transition=mx.AnimatedSwitcherTransition.FADE
    )
    assert isinstance(r.transition, mx.AnimatedSwitcherTransition)
    assert r.transition == mx.AnimatedSwitcherTransition.FADE
    assert r._get_attr("transition") == "fade"

    r = mx.AnimatedSwitcher(content=mx.Text("Hello!"), transition="scale")
    assert isinstance(r.transition, str)
    assert r._get_attr("transition") == "scale"
