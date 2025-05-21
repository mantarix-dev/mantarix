from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.Markdown()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["markdown"],
            attrs={},
            commands=[],
        )
    ], "Test failed"


def test_extension_set_enum():
    r = mx.Markdown()
    assert r.extension_set is None
    assert r._get_attr("extensionSet") is None

    r = mx.Markdown(extension_set=mx.MarkdownExtensionSet.COMMON_MARK)
    assert isinstance(r.extension_set, mx.MarkdownExtensionSet)
    assert r.extension_set == mx.MarkdownExtensionSet.COMMON_MARK
    assert r._get_attr("extensionSet") == "commonMark"

    r = mx.Markdown(extension_set="none")
    assert isinstance(r.extension_set, str)
    assert r._get_attr("extensionSet") == "none"
