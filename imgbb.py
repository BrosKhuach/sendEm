import base64
import requests

apiKey = '6f763617b237732428f0bf2f654701ac' # insert your API key

print("imgBB API Uploader")
print("API Key: " + apiKey)
fileLocation = input("Enter file location: ")

with open(fileLocation, "rb") as file:
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": apiKey,
        "image": base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)

app = Flask(__name__)

if res.status_code == 200:
    print("Server Response: " + str(res.status_code))
    print("Image Successfully Uploaded")
else:
    print("ERROR")
    print("Server Response: " + str(res.status_code))
    if __name__ == '__main__':
        app.run()