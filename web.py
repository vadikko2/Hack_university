from aiohttp import web
from handlers.pie import pie_chart_handler
from handlers.line import line_chart_handler
from handlers.bars import bars_chart_handler
import asyncio


if __name__ == '__main__':

    app = web.Application()

    app.router.add_static(prefix='/js/', path='./js/')
    app.router.add_route('GET', '/pie', pie_chart_handler)
    app.router.add_route('GET', '/line', line_chart_handler)
    app.router.add_route('GET', '/bars', bars_chart_handler)

    loop = asyncio.get_event_loop()
    handler = app.make_handler()

    server = loop.create_server(handler, 'localhost', 8080)

    loop.run_until_complete(server)
    loop.run_forever()
