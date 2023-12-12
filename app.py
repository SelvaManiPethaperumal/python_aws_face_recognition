import flask
from flask import request, jsonify
from faceRecognition import faceRecognition


#app is object which will make the api run
app = flask.Flask(__name__)

#comment/uncomment the below link if you want to make the DEBUG mode on/off
app.config['DEBUG'] = False

@app.route('/get_face_id',methods = ['GET','POST'])
def searchFace():
    
    if request.method == 'GET':
        try:
                #the params name will contain the url which has the face
                url = request.args['name']
                collectionsName = 'SelvaMani' # Name Of the collection  
                return faceRecognition(url, collectionsName)
        except Exception as e:
                print(e)
                raise
        
        

        

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8015)


                


