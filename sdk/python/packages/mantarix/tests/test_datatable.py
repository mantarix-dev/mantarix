import mantarix as mx
from mantarix.core.protocol import Command


def test_datatable_instance_no_attrs_set():
    r = mx.DataTable(columns=[mx.DataColumn(label=mx.Text("Header"))])
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(indent=0, name=None, values=["datatable"], attrs={}, commands=[]),
        Command(indent=2, name=None, values=["datacolumn"], attrs={}, commands=[]),
        Command(
            indent=4,
            name=None,
            values=["text"],
            attrs={"n": "label", "value": "Header"},
            commands=[],
        ),
    ], "Test failed"


def test_datarow_instance_no_attrs_set():
    r = mx.DataRow(cells=[mx.DataCell(content=mx.Text("Cell"))])
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(indent=0, name=None, values=["datarow"], attrs={}, commands=[]),
        Command(indent=2, name=None, values=["datacell"], attrs={}, commands=[]),
        Command(
            indent=4, name=None, values=["text"], attrs={"value": "Cell"}, commands=[]
        ),
    ], "Test failed"


def test_datarow_color_literal_material_state_as_string():
    r = mx.DataRow(cells=[mx.DataCell(content=mx.Text("Cell"))], color="yellow")
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["datarow"],
            attrs={"color": '{"":"yellow"}'},
            commands=[],
        ),
        Command(indent=2, name=None, values=["datacell"], attrs={}, commands=[]),
        Command(
            indent=4, name=None, values=["text"], attrs={"value": "Cell"}, commands=[]
        ),
    ], "Test failed"


def test_datarow_color_multiple_material_states_as_strings():
    r = mx.DataRow(
        cells=[mx.DataCell(content=mx.Text("Cell"))],
        color={"selected": "red", "hovered": "blue", "": "yellow"},
    )
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["datarow"],
            attrs={"color": '{"selected":"red","hovered":"blue","":"yellow"}'},
            commands=[],
        ),
        Command(indent=2, name=None, values=["datacell"], attrs={}, commands=[]),
        Command(
            indent=4, name=None, values=["text"], attrs={"value": "Cell"}, commands=[]
        ),
    ], "Test failed"


def test_datarow_color_multiple_material_states():
    r = mx.DataRow(
        cells=[mx.DataCell(content=mx.Text("Cell"))],
        color={
            mx.ControlState.SELECTED: "red",
            mx.ControlState.HOVERED: "blue",
            mx.ControlState.DEFAULT: "yellow",
        },
    )
    assert isinstance(r, mx.Control)
    assert r._build_add_commands() == [
        Command(
            indent=0,
            name=None,
            values=["datarow"],
            attrs={"color": '{"selected":"red","hovered":"blue","":"yellow"}'},
            commands=[],
        ),
        Command(indent=2, name=None, values=["datacell"], attrs={}, commands=[]),
        Command(
            indent=4, name=None, values=["text"], attrs={"value": "Cell"}, commands=[]
        ),
    ], "Test failed"
