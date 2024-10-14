from google.cloud import bigquery

def get_bq_schema():
    """Define the schema for the BigQuery external table."""
    schema = [
        {"name": "tm_key_mth", "type": "STRING", "mode": "NULLABLE"},
        {"name": "tm_key_day", "type": "STRING", "mode": "NULLABLE"},
        {"name": "citizen_iden_uuid", "type": "STRING", "mode": "NULLABLE"},
        {"name": "idtype", "type": "STRING", "mode": "NULLABLE"},
        {"name": "amount", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "tax_amount", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "rev_amount", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "priceplan_code", "type": "STRING", "mode": "NULLABLE"},
        {"name": "dealer_flag", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "loyalty_id", "type": "STRING", "mode": "NULLABLE"},
        {"name": "identifier_id", "type": "STRING", "mode": "NULLABLE"},
        {"name": "identifier_desc", "type": "STRING", "mode": "NULLABLE"},
        {"name": "identifier_name", "type": "STRING", "mode": "NULLABLE"},
        {"name": "identifier_status", "type": "STRING", "mode": "NULLABLE"},
        {"name": "identifier_start_date", "type": "STRING", "mode": "NULLABLE"},
        {"name": "identifier_aging", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "bill_status", "type": "STRING", "mode": "NULLABLE"},
        {"name": "promoted_flag", "type": "NUMERIC", "mode": "NULLABLE"},
        {"name": "status", "type": "STRING", "mode": "NULLABLE"},
        {"name": "avg_amount", "type": "INT64", "mode": "NULLABLE"},
        {"name": "operator_name", "type": "STRING", "mode": "NULLABLE"}
    ]
    return schema
