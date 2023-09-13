from gw_dsl_parser import get_sql_from_payload


def test_core_function():
    payload = {"workflow": [{"type": "view", "query": [{"op": "aggregate", "groupBy": [], "measures": [{"field": "*", "agg": "count", "asFieldKey": "count"}]}]}]}
    table_name = "test_table"
    assert get_sql_from_payload(table_name, payload) == "SELECT count(*) AS count FROM test_table"
