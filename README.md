This is the Script  for Face recognition in Python Flask 

AWS Face recognition

	AWS Face Recognition is a service provided by Amazon Web Services (AWS) that enables you to add facial analysis and recognition capabilities to your applications. It's a part of the Amazon Rekognition service, which is a fully managed computer vision service.

	With AWS Face Recognition, you can perform various tasks related to facial analysis, such as:

	Face Detection: Identify and locate faces within an image.

	Face Comparison: Compare faces to determine if they are the same person.

	Face Search: Search for faces in a collection of images.

	Face Indexing: Index faces in a collection for efficient searching.

	Emotion Detection: Identify facial expressions to determine emotions.

	Age and Gender Estimation: Estimate the likely age range and gender of a person.

	To use AWS Face Recognition, you need to set up an AWS account, create a Rekognition collection, and then use the Rekognition API to interact with the service. AWS provides SDKs for various programming languages, making it easier to integrate face recognition into your applications.

	Keep in mind that while AWS Face Recognition provides powerful features, you'll incur costs based on your usage, so be sure to check the AWS pricing details for Rekognition.


faceRecognition.py

    The faceRecognition file handle the recognition concept

 awsFaceRecognitionConfig.py

    You should configuate the below details 
        regionName = 'ap-south-1'
		accessKey = 'Your accessKey'
		secretAccesKey = 'Your secretAccesKey'
		bucketName = 'Your bucketName'

Install Packgage 
	
	pip3 install urllib3==2.1.0
	pip3 install boto3