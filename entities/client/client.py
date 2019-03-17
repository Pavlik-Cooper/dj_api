import requests
import os

ENDPOINT = "http://localhost:8000/api/create/"

image_url = os.path.join(os.getcwd(), "adonis.jpeg")


def upload_img(method='post',data={}, is_json=True,img_path=image_url):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
    if img_path is not None:
        headers['content-type'] = 'multipart/form-data'
        with open(img_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, url=ENDPOINT,data=data,files=file_data)
    else:
        r = requests.request(method, url=ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


upload_img(
    data={"user": 1, "title": "foo", "content": "bar"},
    is_json=False,
    img_path=image_url
)