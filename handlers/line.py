from aiohttp import web
from string import Template


def line(men_data, women_data):
    html = """
    <body>
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
        <br>
        <button id="under18">Under 18</button>
        <button id="middleAge">18-35</button>
        <button id="culmination">35-50</button>
        <button id="elder">Above 50</button>
        
        <script>
            var men_data = $men_data.total;
            var women_data = $women_data.total;
                        
            var config = {
                type: 'line',
                data: {
                    labels: ['1', '5', '9', '13', '17', '19', '23'],
                    datasets: [{
                        label: 'Men',
                        backgroundColor: window.chartColors.blue,
                        borderColor: window.chartColors.blue,
                        data: men_data,
                        fill: false,
                    },
                    {
                        label: 'Women',
                        backgroundColor: window.chartColors.red,
                        borderColor: window.chartColors.red,
                        data: women_data,
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
                        data: men_data,
                        fill: false,
                    },
                    {
                        label: 'Women',
                        backgroundColor: window.chartColors.red,
                        borderColor: window.chartColors.red,
                        data: women_data,
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
                        data: men_data,
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
                        data: women_data,
                        fill: false,
                    }]   
                config.data.datasets = women;
                window.myLine.update();
            });
            
            document.getElementById('under18').addEventListener('click', function() {   
                for (var index = 0; index < config.data.datasets.length; ++index) {
                    var current_data = config.data.datasets[index].label;
                    
                    if (current_data == 'Men') {
                        current_data = $men_data;
                    }
                    else {
                        current_data = $women_data;
                    }
                    config.data.datasets[index].data = current_data.under18;
                }
                window.myLine.update();
            });
            
            document.getElementById('middleAge').addEventListener('click', function() { 
                for (var index = 0; index < config.data.datasets.length; ++index) {
                    var current_data = config.data.datasets[index].label;
                    
                    if (current_data == 'Men') {
                        current_data = $men_data;
                    }
                    else {
                        current_data = $women_data;
                    }
                    config.data.datasets[index].data = current_data.middleAge;
                }
                window.myLine.update();
            });
            
            document.getElementById('culmination').addEventListener('click', function() {   
                for (var index = 0; index < config.data.datasets.length; ++index) {
                    var current_data = config.data.datasets[index].label;
                    
                    if (current_data == 'Men') {
                        current_data = $men_data;
                    }
                    else {
                        current_data = $women_data;
                    }
                    config.data.datasets[index].data = current_data.culmination;
                }
                window.myLine.update();
            });
            
            document.getElementById('elder').addEventListener('click', function() {
                for (var index = 0; index < config.data.datasets.length; ++index) {
                    var current_data = config.data.datasets[index].label;
                    
                    if (current_data == 'Men') {
                        current_data = $men_data;
                    }
                    else {
                        current_data = $women_data;
                    }
                    config.data.datasets[index].data = current_data.elder;
                }
                window.myLine.update();
            });
            
        </script>
        <script src="./js/chart.js"></script>
	    <script src="./js/utils.js"></script>
    </body>
    """
    return Template(html).safe_substitute(men_data=men_data, women_data=women_data)


async def line_chart_handler(data):

    # example for testing purposes

    men_data = {
        'under18':      ['4', '5', '0', '3', '3', '0', '1'],
        'middleAge':    ['3', '6', '2', '2', '4', '2', '6'],
        'culmination':  ['3', '2', '2', '2', '4', '0', '5'],
        'elder':        ['0', '2', '1', '1', '0', '1', '2'],
        'total':        ['10', '15', '5', '8', '11', '3', '14']
    }

    women_data = {
        'under18':      ['3', '8', '2', '1', '5', '1', '3'],
        'middleAge':    ['6', '11', '8', '8', '3', '0', '1'],
        'culmination':  ['5', '8', '3', '4', '2', '1', '0'],
        'elder':        ['1', '3', '2', '6', '5', '3', '4'],
        'total':        ['15', '30', '15', '19', '15', '5', '8']
    }

    return web.Response(body=line(men_data=men_data, women_data=women_data), content_type='text/html')
