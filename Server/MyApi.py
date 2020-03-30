from flask import Flask, request
from flask_restful import Resource, Api
import base64
import cv2

app = Flask(__name__)
api = Api(app)

# A Rest Api which returns fixed information
class first(Resource):
	def get(self):
		return {"about":"Made By Kunal Saraf"}

# A Rest Api which takes parameters and returns result after working on parameters
class second(Resource):
	def get(self,num1,num2):
		return {"Product":num1*num2}

# A Rest Api which works on both GET and POST methods
class third(Resource):
	def get(self):
		return {"about":"Made By Kunal Saraf"}
	def post(self):
		# Requesting json file from caller
		my_json_file = request.get_json()

		# Printing the received json file
		print(my_json_file)
		
		# Storing the file in the server after decoding the encoded image
		file_name = 'My_image.' + my_json_file['ext']
		img = open(file_name,'wb')
		img.write(base64.b64decode(my_json_file['media']))
		img.close()
		
		# Reopening the file using opencv and converting from rgb to grey and saving it back
		new_img = cv2.imread(file_name)
		gray_img = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
		cv2.imwrite(file_name,gray_img)

		# Reopening the file and encoding it
		with open(file_name,'rb') as img_file:
			string_of_image = base64.b64encode(img_file.read()).decode("utf-8")

		# Converting the file into python dictionary so that it can be sent as json object
		new_json_data = {'ext':my_json_file['ext'], 'media':string_of_image}
		# Printing the dictionary
		print(new_json_data)

		# Returning the json object back to caller
		return new_json_data, 201

api.add_resource(first,'/')
api.add_resource(second,'/second/<int:num1>,<int:num2>')
api.add_resource(third,'/third')

if __name__ == '__main__':
	app.run(debug=True)