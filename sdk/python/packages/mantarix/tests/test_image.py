from mantarix.core.protocol import Command

import mantarix as mx


def test_image_add():
    i = mx.Image(
        src="https://www.w3schools.com/css/img_5terre.jpg",
    )
    assert isinstance(i, mx.Control)
    assert isinstance(i, mx.Image)
    assert i._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["image"],
            attrs={
                "src": "https://www.w3schools.com/css/img_5terre.jpg",
            },
            commands=[],
        )
    ], "Test failed"


def test_color_blend_mode_enum():
    r = mx.Image(color_blend_mode=mx.BlendMode.LIGHTEN)
    assert isinstance(r.color_blend_mode, mx.BlendMode)
    assert isinstance(r._get_attr("colorBlendMode"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["colorblendmode"] == "lighten"


def test_color_blend_mode_str():
    r = mx.Image(color_blend_mode="darken")
    assert isinstance(r.color_blend_mode, str)
    assert isinstance(r._get_attr("colorBlendMode"), str)
    cmd = r._build_add_commands()
    assert cmd[0].attrs["colorblendmode"] == "darken"


def test_repeat_enum():
    r = mx.Image()
    assert r.repeat is None
    assert r._get_attr("repeat") is None

    r = mx.Image(repeat=mx.ImageRepeat.REPEAT)
    assert isinstance(r.repeat, mx.ImageRepeat)
    assert r.repeat == mx.ImageRepeat.REPEAT
    assert r._get_attr("repeat") == "repeat"

    r = mx.Image(repeat="repeatX")
    assert isinstance(r.repeat, str)
    assert r._get_attr("repeat") == "repeatX"


def test_fit_enum():
    r = mx.Image()
    assert r.fit is None
    assert r._get_attr("fit") is None

    r = mx.Image(fit=mx.ImageFit.FILL)
    assert isinstance(r.fit, mx.ImageFit)
    assert r.fit == mx.ImageFit.FILL
    assert r._get_attr("fit") == "fill"

    r = mx.Image(fit="none")
    assert isinstance(r.fit, str)
    assert r._get_attr("fit") == "none"
