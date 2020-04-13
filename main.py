from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from datetime import datetime


async def homepage(request):
    now = datetime.now()
    ts = now.isoformat()
    return JSONResponse({'hello': 'world', 'ts': ts})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])


# async def app(scope, receive, send):
#    #assert scope['type'] == 'http'
#    response = Response('Hello, world!', media_type='text/plain')
#    await response(scope, receive, send)
