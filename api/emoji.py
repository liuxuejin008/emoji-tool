import traceback

from sanic import response, Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def index(request, path=""):
    print(path)
    return json({'hello': path})


@app.route('/user')
async def user(request):
    return json({'hello': "1234546"})

@app.route('/ann')
async def ann(request):
    return json({'hello': "123454678"})

#if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8088)
