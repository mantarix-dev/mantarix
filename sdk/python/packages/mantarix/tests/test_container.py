import mantarix as mx
from mantarix.core.protocol import Command


def test_instance_no_attrs_set():
    r = mx.Container()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["container"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_gradient():
    c = mx.Container(
        gradient=mx.LinearGradient(
            colors=[],
            tile_mode="mirror",
        )
    )
    cmd = c._build_add_commands()
    assert (
        cmd[0].attrs["gradient"]
        == '{"colors":[],"tile_mode":"mirror","begin":{"x":-1,"y":0},"end":{"x":1,"y":0},"type":"linear"}'
    )

    c = mx.Container(
        gradient=mx.LinearGradient(
            colors=[],
            tile_mode=mx.GradientTileMode.REPEATED,
        )
    )
    cmd = c._build_add_commands()
    assert (
        cmd[0].attrs["gradient"]
        == '{"colors":[],"tile_mode":"repeated","begin":{"x":-1,"y":0},"end":{"x":1,"y":0},"type":"linear"}'
    )

    c = mx.Container(
        gradient=mx.LinearGradient(
            colors=[],
        )
    )
    cmd = c._build_add_commands()
    assert (
        cmd[0].attrs["gradient"]
        == '{"colors":[],"tile_mode":"clamp","begin":{"x":-1,"y":0},"end":{"x":1,"y":0},"type":"linear"}'
    )


def test_blend_mode_enum():
    r = mx.Container(blend_mode=mx.BlendMode.LIGHTEN, bgcolor=mx.Colors.RED)
    assert isinstance(r.blend_mode, mx.BlendMode)
    assert isinstance(r._get_attr("blendMode"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["blendmode"] == "lighten"


def test_blend_mode_str():
    r = mx.Container(blend_mode="darken", bgcolor=mx.Colors.RED)
    assert isinstance(r.blend_mode, str)
    assert isinstance(r._get_attr("blendMode"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["blendmode"] == "darken"


def test_clip_behavior_enum():
    r = mx.Container()
    assert r.clip_behavior is None
    assert r._get_attr("clipBehavior") is None

    r = mx.Container(clip_behavior=mx.ClipBehavior.ANTI_ALIAS)
    assert isinstance(r.clip_behavior, mx.ClipBehavior)
    assert r.clip_behavior == mx.ClipBehavior.ANTI_ALIAS
    assert r._get_attr("clipBehavior") == "antiAlias"

    r = mx.Container(clip_behavior="none")
    assert isinstance(r.clip_behavior, str)
    assert r._get_attr("clipBehavior") == "none"


def test_image_repeat_enum():
    r = mx.Container()
    assert r.image_repeat is None
    assert r._get_attr("imageRepeat") is None

    r = mx.Container(image_repeat=mx.ImageRepeat.REPEAT)
    assert isinstance(r.image_repeat, mx.ImageRepeat)
    assert r.image_repeat == mx.ImageRepeat.REPEAT
    assert r._get_attr("imageRepeat") == "repeat"

    r = mx.Container(image_repeat="repeatX")
    assert isinstance(r.image_repeat, str)
    assert r._get_attr("imageRepeat") == "repeatX"


def test_image_fit_enum():
    r = mx.Container()
    assert r.image_fit is None
    assert r._get_attr("imageFit") is None

    r = mx.Container(image_fit=mx.ImageFit.FILL)
    assert isinstance(r.image_fit, mx.ImageFit)
    assert r.image_fit == mx.ImageFit.FILL
    assert r._get_attr("imageFit") == "fill"

    r = mx.Container(image_fit="none")
    assert isinstance(r.image_fit, str)
    assert r._get_attr("imageFit") == "none"
