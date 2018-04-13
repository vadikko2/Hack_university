from aiohttp import web
from string import Template


def line(data):
    html = """
    <body>
        <script src="./js/chart.js"></script>
	    <script src="./js/utils.js"></script>
        <style>
            canvas{
                -moz-user-select: none;
                -webkit-user-select: none;
                -ms-user-select: none;
            }
        </style>
        <div style="width:75%;">
            <canvas id="canvas"></canvas>
        </div>
        <script>
            var config = {
                type: 'line',
                data: {
                    labels: ['1', '5', '9', '13', '17', '19', '23'],
                    datasets: [{
                        label: 'Testing',
                        backgroundColor: window.chartColors.red,
                        borderColor: window.chartColors.red,
                        data: [$data],
                        fill: false,
                    }]
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false,
                    },
                    hover: {
                        mode: 'nearest',
                        intersect: true
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Hours'
                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                                labelString: 'Visitors'
                            }
                        }]
                    }
                }
            };
    
            window.onload = function() {
                var ctx = document.getElementById('canvas').getContext('2d');
                window.myLine = new Chart(ctx, config);
            };
        </script>
    </body>
    """
    return Template(html).safe_substitute(data=data)


async def line_chart_handler(data):
    return web.Response(body=line('10, 15, 5, 8, 11, 3, 14'), content_type='text/html')
