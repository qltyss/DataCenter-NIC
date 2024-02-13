import requests

def handle_api_call(image_data, recog_url):
    try:
        response = requests.post(recog_url, json={'image': image_data})
        print(response.json())
    except Exception as e:
        print("Error in API call:", e)