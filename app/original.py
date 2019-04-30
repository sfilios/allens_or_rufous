from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.staticfiles import StaticFiles
import uvicorn
from fastai import *
from fastai.vision import *

app = Starlette()
app.debug=True
app.mount('/static', StaticFiles(directory='static'))

model_file_url = 'https://www.dropbox.com/s/p1p9kixmpzic1f1/stage-2.pth?raw=1'
classes = ['allens', 'rufous']
path = Path(__file__).parent
print(path)

@app.route('/')
def homepage(request):
    return PlainTextResponse('Hello, world!')

@app.route('/user/me')
def user_me(request):
    username = "Stephen"
    return PlainTextResponse('Hello, %s!' % username)

@app.route('/user/{username}')
def user(request):
    username = request.path_params['username']
    return PlainTextResponse('Hello, %s' % username)

@app.websocket_route('/ws')
async def websocket_endpoint(websocket):
    await websocket.appect()
    await websocket.send_text('Hello, websocket!')
    await websocket.close()

@app.on_event('startup')
def startup():
    print('Ready to go')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port = 8000)
