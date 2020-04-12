# from starlette.applications import Starlette
# from starlette.responses import JSONResponse
# from starlette.routing import Route


# async def homepage(request):
#     return JSONResponse({'hello': 'world'})


# app = Starlette(debug=True, routes=[
#     Route('/', homepage),
# ])


from starlette.responses import Response


async def app(scope, receive, send):
    #assert scope['type'] == 'http'
    response = Response('Hello, world!', media_type='text/plain')
    await response(scope, receive, send)

