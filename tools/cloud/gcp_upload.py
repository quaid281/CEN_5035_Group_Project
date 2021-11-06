import sys
from google.cloud import storage
import json

def upload_blob(bucket_name, key_file, source_file_name, destination_blob_name, blob_metadata):
    """Uploads a file to the bucket."""

    storage_client = storage.Client.from_service_account_json(json_credentials_path=key_file)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))
    print("Public url: https://{}.storage.googleapis.com/{}".format(bucket_name, destination_blob_name))

    blob = bucket.get_blob(destination_blob_name)
    blob.metadata = blob_metadata
    blob.patch()
    print("The metadata for the blob {} is {}".format(blob.name, blob.metadata))

if __name__ == "__main__":
    upload_blob(
        bucket_name=sys.argv[1],
        key_file = sys.argv[2],
        source_file_name=sys.argv[3],
        destination_blob_name=sys.argv[4],
        blob_metadata=json.loads(sys.argv[5])
    )
