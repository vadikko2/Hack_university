from aiohttp import web
from handlers.pie import pie_chart_handler
from handlers.line import line_chart_handler
from handlers.bars import bars_chart_handler
from handlers.main import main_body
import json
import asyncio


if __name__ == '__main__':
    app = web.Application()

    app.router.add_static(prefix='/js/', path='./js/')
    app.router.add_static(prefix='/css/', path='./css/')

    app.router.add_route('GET', '/pie', pie_chart_handler)
    app.router.add_route('GET', '/line', line_chart_handler)
    app.router.add_route('GET', '/bars', bars_chart_handler)

    '''
        localhost:8080/pie - pie chart with men/women percentage
        localhost:8080/line - line chart with granular options selection
        localhost:8080/bars - bars chart with men/women number by age
        
        localhost:8080/ - main screen with big line chart above and bars chart below to the left and pie to the right
    '''

    '''male_data = {
        'under18': [4, 5, 0, 3, 3, 0, 1],
        'middleAge': [3, 6, 2, 2, 4, 2, 6],
        'culmination': [3, 2, 2, 2, 4, 0, 5],
        'elder': [0, 2, 1, 1, 0, 1, 2],
        'total': [10, 15, 5, 8, 11, 3, 14],
        'percentage': 66 * 100 / (66 + 107)
    }

    female_data = {
        'under18': [3, 8, 2, 1, 5, 1, 3],
        'middleAge': [6, 11, 8, 8, 3, 0, 1],
        'culmination': [5, 8, 3, 4, 2, 1, 0],
        'elder': [1, 3, 2, 6, 5, 3, 4],
        'total': [15, 30, 15, 19, 15, 5, 8],
        'percentage': 107 * 100 / (66 + 107)
    }'''

    male_data = json.load(open('male.json', 'r'))
    female_data = json.load(open('female.json', 'r'))


    async def main_handler(data):
        return web.Response(body=main_body(male_data=male_data, female_data=female_data), content_type='text/html')


    app.router.add_route('GET', '/', main_handler)

    loop = asyncio.get_event_loop()
    handler = app.make_handler()

    server = loop.create_server(handler, 'localhost', 8081)

    loop.run_until_complete(server)
    loop.run_forever()
