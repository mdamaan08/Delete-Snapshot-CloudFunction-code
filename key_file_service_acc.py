import os
from google.oauth2.credentials import Credentials
from google.cloud import storage

# set the path to the service account key file
path_to_key_file = “ravindra.json”  #OR 'C:/Users/Coditas/Desktop/abc.json' on such format

# create credentials object
creds = Credentials.from_service_account_file(path_to_key_file, scopes=[“https://www.googleapis.com/auth/devstorage.full_control”])

# create a client object
client = storage.Client(credentials=creds)

# specify the name of the bucket you want to create
bucket_name = “my-new-bucket”

# create the bucket
bucket = client.create_bucket(bucket_name)

# print the bucket’s name
print(“Bucket {} created.“.format(bucket.name))




#Python Code to work with key file of service account to authenticate.
from google.cloud import compute
from googleapiclient import discovery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('C:/Users/Coditas/Desktop/abc.json')
service = discovery.build('compute', 'v1', credentials=credentials)

project = 'amazing-office-372104'
request = service.snapshots().list(project=project)
response = request.execute()

for snapshot in response['items']:
	instance_creation_date=snapshot['creationTimestamp'][0:10].split("-")
	id=snapshot['name']