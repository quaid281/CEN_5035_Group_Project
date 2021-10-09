from google.cloud import storage
import argparse

def list_blobs_with_prefix(bucket_name, keyfile, prefix):
    #Lists all the blobs in the bucket that begin with the prefix.
    storage_client = storage.Client.from_service_account_json(json_credentials_path=keyfile)
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix)

    print("Files in bucket {} with prefix '{}' ".format(bucket_name, prefix))
    for blob in blobs:
        print("{} {} bytes ".format(blob.name,blob.size))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', required=True, type=str)
    parser.add_argument('--keyfile', required=True, type=str)
    parser.add_argument('--prefix', type=str,default='')
    args = parser.parse_args()
    list_blobs_with_prefix(
        bucket_name = args.bucket,
        keyfile = args.keyfile,
        prefix = args.prefix
    )
