import base64
import requests
import json

# Initializing the needful
img_location = 'index.jpeg'
file_extention = img_location.split('.')[1]
url = 'http://127.0.0.1:5000/third'

# Opening the image and encoding it so that it can be transferred
with open(img_location,'rb') as img_file:
	string_of_image = base64.b64encode(img_file.read()).decode("utf-8")

# Converting the data into dictionary so that it can be transferred as json to server
my_json_data = {'ext':file_extention, 'media':string_of_image}

# Making a post request to server and sending the json file created above
response_sent_by_server = requests.post(url, json = my_json_data)

# Converting response json file received from server to python dictionary
my_dict = json.loads(response_sent_by_server.text)

# Saving the image sent by sever
file_name = 'My_image.' + my_dict['ext']
img = open(file_name,'wb')
img.write(base64.b64decode(my_dict['media']))
img.close()