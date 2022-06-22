url = 'https://api.imgbb.com/1/upload'
key = '232565fc1a4f0d24578d9aeadc0b43ab'

app = Flask(__name__)

app = requests.post(
    url, 
    data = {
        'key': key, 
        'image':b64encode(open('a.png', 'rb').read()),
        'name': 'a.png',
    }
)
if __name__ == '__main__':
    app.run()