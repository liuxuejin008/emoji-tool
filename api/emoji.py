import traceback

from sanic import response, Sanic
from sanic.response import json

app = Sanic("emoji")


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


@app.route('/hotel.order.status.change.callback')
async def ann(request):
    data = request.get_json()
    print(data)
    return json({'code': 0,"message":"成功"})


@app.route('/hotel.poi.info.change.callback')
async def ann(request):
    data = request.get_json()
    print(data)
    return json({'code': 0,"message":"成功"})

@app.route('/hotel.product.info.change.callback')
async def ann(request):
    data = request.get_json()
    print(data)
    return json({'code': 0,"message":"成功"})


#if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8088)
