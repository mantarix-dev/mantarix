from mantarix.core.protocol import Command

import mantarix as mx


def test_instance_no_attrs_set():
    r = mx.FilePicker()
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["filepicker"],
            attrs={"upload": "[]"},
            commands=[],
        )
    ], "Test failed"


def test_file_type_enum():
    r = mx.FilePicker()
    r.file_type = mx.FilePickerFileType.VIDEO
    assert isinstance(r.file_type, mx.FilePickerFileType)
    assert r.file_type == mx.FilePickerFileType.VIDEO
    assert r._get_attr("fileType") == "video"

    r = mx.FilePicker()
    r.file_type = "any"
    assert isinstance(r.file_type, str)
    assert r._get_attr("fileType") == "any"
