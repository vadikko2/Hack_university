from aiohttp import web
from handlers.main import main_body
import json
import asyncio


def main():
    app = web.Application()

    app.router.add_static(prefix='/js/', path='./js/')
    app.router.add_static(prefix='/css/', path='./css/')

    male_data = json.load(open('male.json', 'r'))
    female_data = json.load(open('female.json', 'r'))

    async def main_handler(data):
        return web.Response(body=main_body(male_data=male_data, female_data=female_data), content_type='text/html')

    app.router.add_route('GET', '/', main_handler)

    loop = asyncio.get_event_loop()
    handler = app.make_handler()

    server = loop.create_server(handler, 'localhost', 8082)

    loop.run_until_complete(server)
    loop.run_forever()


if __name__ == '__main__':
    main()
