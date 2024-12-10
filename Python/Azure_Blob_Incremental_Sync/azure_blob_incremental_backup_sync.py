from azure.storage.blob import BlobServiceClient

def sync_blob_storage():
    source_account_url = "https://<source-storage-account>.blob.core.windows.net/"
    dest_account_url = "https://<dest-storage-account>.blob.core.windows.net/"
    container_name = "container"
    source_client = BlobServiceClient(account_url=source_account_url, credential="<source-credentials>")
    dest_client = BlobServiceClient(account_url=dest_account_url, credential="<dest-credentials>")
    
    source_container = source_client.get_container_client(container_name)
    dest_container = dest_client.get_container_client(container_name)
    
    for blob in source_container.list_blobs():
        if not dest_container.get_blob_client(blob.name).exists():  # Simple existence check
            source_blob = source_container.get_blob_client(blob.name)
            dest_blob = dest_container.get_blob_client(blob.name)
            dest_blob.start_copy_from_url(source_blob.url)
