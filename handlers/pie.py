from aiohttp import web
from string import Template


def pie(men, women):
    html = """
    <body>
        <div style="width:25%">
            <canvas id="pie-canvas"></canvas>
        </div>
        <script src="./js/chart.js"></script>
        <script src="./js/utils.js"></script>
        <script>
            var config = {
                type: 'pie',
                data: {
                    datasets: [{
                        data: [
                            $men,
                            $women
                        ],
                        backgroundColor: [
                            window.chartColors.blue,
                            window.chartColors.red,
                        ],
                    }],
                    labels: [
                        'Men',
                        'Women'
                    ]
                },
                options: {
                    responsive: true
                }
            };
    
            window.onload = function() {
                var ctx = document.getElementById('pie-canvas').getContext('2d');
                window.myPie = new Chart(ctx, config);
            };
        </script>
    </body>
    """
    return Template(html).safe_substitute(men=men, women=women)


async def pie_chart_handler(data):
    return web.Response(body=pie(men=70, women=30), content_type='text/html')
