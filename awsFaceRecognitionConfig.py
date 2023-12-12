import boto3

def config():

	regionName = 'ap-south-1'
	accessKey = 'Your accessKey'
	secretAccesKey = 'Your secretAccesKey'
	bucketName = 'Your bucketName'
	client = boto3.client('rekognition',
						region_name=regionName,
						aws_access_key_id=accessKey,
						aws_secret_access_key=secretAccesKey
						)
	return [client, bucketName]