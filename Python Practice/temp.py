def plot_image(image_url,size=(12,9)):
	
	# Download an image from url and display it on the notebook
	urllib.request.urlretrieve(image_url,"image.jpg")
	image = cv2.imread("image.jpg")

	# If image in color then correct the color coding to BGR to RGB
	if len(image.shape) == 3:
		image =  cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	rcParams["figure.figsize"] = size[0],size[1]

	plt.axis("off")
	plt.imshow(image,cmap="Grey_r")
	plt.show()


def analyze_img(url, apikey = my_apikey):
	json_result = visrec.classify(url = url, threshold = '0.6', classifier_ids = 'default').get_result()

	json_classes = json_result['images'][0]['classifiers'][0]['classes']

	df = json_normalize(json_classes).sort_values('score', acending=False).reset_index(drop=True)

	return df

import json
with open(".zip",'rb') as ...., open(".zip",'rb') as .... , open(".zip",'rb') as ..... :
	response = visrec.create_classifier(name='foodclassifier', positive_examples = {""=, ""=, ""=})

print(json.dumps(response.get_result(),indent=2))