from aiohttp import web
from string import Template


def bars(men_data, women_data):
    html = """
    <body>
        <script src="./js/chart.js"></script>
	    <script src="./js/utils.js"></script>
	    
        <style>
            bars-canvas {
                -moz-user-select: none;
                -webkit-user-select: none;
                -ms-user-select: none;
            }
        </style>
        
        <div style="width: 75%;">
            <canvas id="bars-canvas"></canvas>
        </div>
        
        <script>
            var color = Chart.helpers.color;
            var barChartData = {
                labels: ['under 18', '18-35', '35-50', '50 and older'],
                datasets: [{
                    label: 'Men',
                    backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
                    borderColor: window.chartColors.blue,
                    borderWidth: 1,
                    data: [$men_data]
                }, {
                    label: 'Women',
                    backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
                    borderColor: window.chartColors.red,
                    borderWidth: 1,
                    data: [$women_data]
                }]
            };
    
            window.onload = function() {
                var ctx = document.getElementById('bars-canvas').getContext('2d');
                window.myBar = new Chart(ctx, {
                    type: 'bar',
                    data: barChartData,
                    options: {
                        responsive: true,
                        legend: {
                            position: 'top',
                        },
                        title: {
                            display: true,
                        }
                    }
                });
            };     
        </script>
    </body>
    """
    return Template(html).safe_substitute(men_data=men_data, women_data=women_data)


async def bars_chart_handler(data):
    return web.Response(body=bars(men_data='18, 24, 13, 9', women_data='17, 19, 16, 5'), content_type='text/html')
