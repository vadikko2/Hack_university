from aiohttp import web
from string import Template


def line(men_data, women_data):
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
        
        <button id="menOnly">Men</button>
        <button id="womenOnly">Women</button>
        <button id="everyone">Everyone</button>
        
        <button id="under18">Under 18</button>
        <button id="middleAge">18-35</button>
        <button id="culmination">35-50</button>
        <button id="elder">Above 50</button>

        <script>
            var config = {
                type: 'line',
                data: {
                    labels: ['1', '5', '9', '13', '17', '19', '23'],
                    datasets: [{
                        label: 'Men',
                        backgroundColor: window.chartColors.blue,
                        borderColor: window.chartColors.blue,
                        data: [$men_data],
                        fill: false,
                    },
                    {
                        label: 'Women',
                        backgroundColor: window.chartColors.red,
                        borderColor: window.chartColors.red,
                        data: [$women_data],
                        fill: false,
                    }]
                },
                options: {
                    responsive: true,
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
            
            var colorNames = Object.keys(window.chartColors);

            document.getElementById('everyone').addEventListener('click', function() {
                var all = [{
                        label: 'Men',
                        backgroundColor: window.chartColors.blue,
                        borderColor: window.chartColors.blue,
                        data: [$men_data],
                        fill: false,
                    },
                    {
                        label: 'Women',
                        backgroundColor: window.chartColors.red,
                        borderColor: window.chartColors.red,
                        data: [$women_data],
                        fill: false,
                    }]
    
                config.data.datasets = all;
                window.myLine.update();
            });
            
            document.getElementById('menOnly').addEventListener('click', function() {
                var men = [{
                        label: 'Men',
                        backgroundColor: window.chartColors.blue,
                        borderColor: window.chartColors.blue,
                        data: [$men_data],
                        fill: false,
                    }]
    
                config.data.datasets = men;
                window.myLine.update();
            });
            
            document.getElementById('womenOnly').addEventListener('click', function() {
                var women = [{
                        label: 'Women',
                        backgroundColor: window.chartColors.red,
                        borderColor: window.chartColors.red,
                        data: [$women_data],
                        fill: false,
                    }]
    
                config.data.datasets = women;
                window.myLine.update();
            });
            
            
        </script>
    </body>
    """
    return Template(html).safe_substitute(men_data=men_data, women_data=women_data)


async def line_chart_handler(data):
    return web.Response(body=line(men_data='10, 15, 5, 8, 11, 3, 14', women_data='7, 17, 3, 14, 4, 7, 11'),
                        content_type='text/html')
