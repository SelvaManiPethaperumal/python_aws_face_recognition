from awsFaceRecognitionConfig import config
from flask import jsonify

# Get AWS Rekognition client and S3 bucket name from configuration
client, bucketName = config()

def faceRecognition(url, collectionsName):
   	# Get the list of existing collections
    collection_list = collectionList()
    
    # If the specified collection does not exist, create it
    if collectionsName not in collection_list:
        result = createCollection(collectionsName)

        # If the status is not 200, return an error saying unable to create collection
        if result != '200':
            response = [{'face_id': 'No Face', 'Existance': 0}]
            return jsonify(response)

    # Extract image name from the URL
    url_list = url.split('/')
    image_name = url_list[-1]

    # Compare the face in the image with the specified collection
    face_id = compareFace(collectionsName, image_name)

    # If no face is found in the image, return appropriate response
    if face_id == 'NOFACE':
        response = [{'face_id': 'No Face', 'Existance': 0}]
        return jsonify(response)

    # If a face is found, return the face ID and existence status
    elif face_id is not None:
        response = [{'face_id': face_id, 'Existance': 1}]
        return jsonify(response)

    # If face not found, add the face to the collection and return response
    else:
        face_id = faceKey(image_name, collectionsName)
        response = [{'face_id': face_id, 'Existance': 0}]
        return jsonify(response)


def collectionList():
    """Function for getting the collection list"""
    # Get the response which will have the list of collections
    response = client.list_collections()

    # Retrieve the collection ids and store them in a list
    collections = response['CollectionIds']
    collection_list = [collection for collection in collections]

    # Return the list of collection ids
    return collection_list


def createCollection(collectionName):
    """Create a new collection with the given name"""
    # Get the response of creating the collection
    response = client.create_collection(CollectionId=collectionName)

    # Return the status code as a string
    return str(response['StatusCode'])


def compareFace(collectionName, image_name):
    """Compare the face in the image with the faces in the specified collection"""
    # Set the accuracy at which the face should be recognized
    threshold = 90

    # Set the maximum number of faces to be searched
    maxFaces = 1

    try:
        # Search for faces in the specified collection using the image
        response = client.search_faces_by_image(
            CollectionId=collectionName,
            Image={'S3Object': {'Bucket': bucketName, 'Name': image_name}},
            FaceMatchThreshold=threshold,
            MaxFaces=maxFaces
        )

    # If any error occurs, return 'NOFACE'
    except Exception as e:
        return 'NOFACE'

    # Retrieve face matches from the response
    faceMatches = response['FaceMatches']
    face_key = None

    # Load the face_id if a match is found, else let it be None
    for match in faceMatches:
        face_key = match['Face']['FaceId']

    # Return the face_id
    return face_key


def faceKey(image_path, collectionName):
    """Add a face to the specified collection and return the face_id"""
    # Get the response for indexing the faces in the specified collection with the image
    response = client.index_faces(
        CollectionId=collectionName,
        Image={'S3Object': {'Bucket': bucketName, 'Name': image_path}},
        ExternalImageId=image_path,
        MaxFaces=1,
        QualityFilter="AUTO",
        DetectionAttributes=['DEFAULT']
    )

    face_id = None

    # Load the face_id from the response
    for faceRecord in response['FaceRecords']:
        face_id = faceRecord['Face']['FaceId']

    # Return the face_id
    return face_id
