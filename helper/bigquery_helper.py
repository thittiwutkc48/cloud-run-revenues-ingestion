from google.cloud import bigquery
from google.api_core.exceptions import NotFound


def delete_table_if_exists(project_id, dataset_id, table_name):
    bigquery_client = bigquery.Client()
    table_id = f"{project_id}.{dataset_id}.{table_name}"
    
    try:
        bigquery_client.get_table(table_id)
        bigquery_client.delete_table(table_id)
        print(f"Deleted table {table_id}")
    except NotFound:
        print(f"Table {table_id} not found, skipping deletion.")


def create_external_table_from_gcs(project_id, bucket_name, dataset_id, table_name, file_name):
    gcs_uri = f"gs://{bucket_name}/{file_name}"
    
    bigquery_client = bigquery.Client()
    
    # Delete the old table if it exists
    delete_table_if_exists(project_id, dataset_id, table_name)
    
    # Proceed to create the new table
    table_id = f"{project_id}.{dataset_id}.{table_name}"
    
    external_config = bigquery.ExternalConfig("PARQUET")
    external_config.source_uris = [gcs_uri]
    
    # Set the external data configuration to autodetect schema
    external_config.autodetect = True
    
    # Create a table without a predefined schema
    table = bigquery.Table(table_id)
    table.external_data_configuration = external_config
    
    table = bigquery_client.create_table(table)
    
    print(f"Created external table {table_id} pointing to {gcs_uri} with auto-detected schema")
    return table

# def create_external_table_from_gcs(project_id, bucket_name, dataset_id, table_name, file_name):
#     gcs_uri = f"gs://{bucket_name}/{file_name}"
    
#     bigquery_client = bigquery.Client()
    
#     # Delete the old table if it exists
#     delete_table_if_exists(project_id, dataset_id, table_name)
    
#     # Proceed to create the new table
#     table_id = f"{project_id}.{dataset_id}.{table_name}"
    
#     external_config = bigquery.ExternalConfig("PARQUET")
#     external_config.source_uris = [gcs_uri]
    
#     schema = get_bq_schema()  # Assuming you have this function defined
    
#     table = bigquery.Table(table_id, schema=schema)
#     table.external_data_configuration = external_config
    
#     table = bigquery_client.create_table(table)
    
#     print(f"Created external table {table_id} pointing to {gcs_uri}")
#     return table