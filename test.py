# import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string('DefaultEndpointsProtocol=https;AccountName=hrc;AccountKey=jhbig1PYOQGibCigtf8QjKk4FZgUYbqALDg+n1w4vp8tMGiY4YIXZdA3MjPn4HSbgK+qPf4QM5MqFNvlriOw5A==;EndpointSuffix=core.windows.net')

# Create a unique name for the container
container_name = 'dev'

# Create the container
# container_client = blob_service_client.create_container(container_name)


# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob='1/test.csv')

print("\nUploading to Azure Storage as blob:\n\t")

# Upload the created file
with open('test.csv', "rb") as data:
    blob_client.upload_blob(data)


print(blob_client.download_blob().readall())


# create data
head = ["col1" , "col2" , "col3"]
value = [[1 , 2 , 3],[4,5,6] , [8 , 7 , 9]]
df = pd.DataFrame (value, columns = head)
output = df.to_csv (index=False, encoding = "utf-8")
print(output)

connection_string=''
# Instantiate a new BlobServiceClient using a connection string
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
# Instantiate a new ContainerClient
container_client = blob_service_client.get_container_client('mycsv')
try:
   # Create new Container in the service
   container_client.create_container()
   properties = container_client.get_container_properties()
except ResourceExistsError:
   print("Container already exists.")

# Instantiate a new BlobClient
blob_client = container_client.get_blob_client("output.csv")
# upload data
blob_client.upload_blob(output, blob_type="BlockBlob")