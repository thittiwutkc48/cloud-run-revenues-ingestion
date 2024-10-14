# from google.cloud import storage

# def read_gcs_file(bucket_name, file_name):
#     """Read the file from Google Cloud Storage."""
#     client = storage.Client()
#     bucket = client.get_bucket(bucket_name)
#     blob = bucket.blob(file_name)
#     return blob.download_as_string()
