import functions_framework
import os
from google.cloud import bigquery
# from schema.schema import get_bq_schema  
from dotenv import load_dotenv
from helper.bigquery_helper import create_external_table_from_gcs

@functions_framework.cloud_event
def ingest_revenues_data(cloud_event):
    data = cloud_event.data
    load_dotenv()

    bucket_name = data["bucket"]
    file_name = data["name"]
   
    project_id = os.getenv('PROJECT_ID')
    dataset_id = os.getenv('DATASET_ID')
    bucket_name = os.getenv('BUCKET_NAME')
    table_name = os.getenv('TABLE_NAME')
    prefix_name_st = os.getenv('PREFIX_NAME_ST')
    prefix_name_nd = os.getenv('PREFIX_NAME_ND')
 
    if prefix_name_st == file_name.split("/")[0] and prefix_name_nd == file_name.split("/")[1]:
        if not file_name.endswith(".parquet"):
            print(f"Ignoring file {file_name}. Only parquet files are processed.")
            return
        try:
            create_external_table_from_gcs(project_id, bucket_name, dataset_id, table_name, file_name)
            print(f"Successfully created external table for {file_name}.")
        except Exception as e:
            print(f"Error creating external table for {file_name}: {e}")
    else:
        print(f"Ignoring file {file_name}. Only subfolder {prefix_name_nd} in {bucket_name} are processed.")
        return
