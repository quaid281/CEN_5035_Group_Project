
import sys
from google.cloud import storage

def upload_blob(bucket_name, key_file, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""

    storage_client = storage.Client.from_service_account_json(json_credentials_path=key_file)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))
    print("Public url: https://{}.storage.googleapis.com/{}".format(bucket_name, destination_blob_name))


if __name__ == "__main__":
    upload_blob(
        bucket_name=sys.argv[1],
        key_file = sys.argv[2],
        source_file_name=sys.argv[3],
        destination_blob_name=sys.argv[4],
    )
