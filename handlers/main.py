from aiohttp import web
from string import Template


def main_body(men_data, women_data):

    html = """
        <body>
            <script src="./js/chart.js"></script>
    	    <script src="./js/utils.js"></script>

            <style>
                line-canvas{
                    -moz-user-select: none;
                    -webkit-user-select: none;
                    -ms-user-select: none;
                },
                bars-canvas {
                    -moz-user-select: none;
                    -webkit-user-select: none;
                    -ms-user-select: none;
                },
                #container {width: 100%;}
                #bars  {float:left;}
                #pie  {float:right;}
            </style>

            <div style="width:100%;" align="center">
                <canvas id="line-canvas"></canvas>
                <button id="menOnly">Men</button>
                <button id="womenOnly">Women</button>
                <button id="everyone">Everyone</button>
                <br>
                <button id="under18">Under 18</button>
                <button id="middleAge">18-35</button>
                <button id="culmination">35-50</button>
                <button id="elder">Above 50</button>
                <br>
            </div>  
             
            <div id="container">
                <div id="bars" style="width: 60%;">
                    <canvas id="bars-canvas"></canvas>
                </div>
                <br><br><br><br><br>
                <div id="pie" style="width: 40%">
                    <canvas id="pie-canvas"></canvas>
                </div>
            </div>
            <br>
            <script>
                var lineconfig = {
                    type: 'line',
                    data: {
                        labels: ['1', '5', '9', '13', '17', '19', '23'],
                        datasets: [{
                            label: 'Men',
                            backgroundColor: window.chartColors.blue,
                            borderColor: window.chartColors.blue,
                            data: $men_data.total,
                            fill: false,
                        },
                        {
                            label: 'Women',
                            backgroundColor: window.chartColors.red,
                            borderColor: window.chartColors.red,
                            data: $women_data.total,
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
    
                var colorNames = Object.keys(window.chartColors);

                document.getElementById('everyone').addEventListener('click', function() {
                    var all = [{
                            label: 'Men',
                            backgroundColor: window.chartColors.blue,
                            borderColor: window.chartColors.blue,
                            data: $men_data.total,
                            fill: false,
                        },
                        {
                            label: 'Women',
                            backgroundColor: window.chartColors.red,
                            borderColor: window.chartColors.red,
                            data: $women_data.total,
                            fill: false,
                        }] 
                    lineconfig.data.datasets = all;
                    window.myLine.update();
                });

                document.getElementById('menOnly').addEventListener('click', function() {
                    var men = [{
                            label: 'Men',
                            backgroundColor: window.chartColors.blue,
                            borderColor: window.chartColors.blue,
                            data: $men_data.total,
                            fill: false,
                        }]
                    lineconfig.data.datasets = men;
                    window.myLine.update();
                });

                document.getElementById('womenOnly').addEventListener('click', function() {
                    var women = [{
                            label: 'Women',
                            backgroundColor: window.chartColors.red,
                            borderColor: window.chartColors.red,
                            data: $women_data.total,
                            fill: false,
                        }]   
                    lineconfig.data.datasets = women;
                    window.myLine.update();
                });

                document.getElementById('under18').addEventListener('click', function() {

                    for (var index = 0; index < lineconfig.data.datasets.length; ++index) {
                        var current_data = lineconfig.data.datasets[index].label;

                        if (current_data == 'Men') {
                            current_data = $men_data;
                        }
                        else {
                            current_data = $women_data;
                        }
                        lineconfig.data.datasets[index].data = current_data.under18;
                    }
                    window.myLine.update();
                });

                document.getElementById('middleAge').addEventListener('click', function() { 
                    for (var index = 0; index < lineconfig.data.datasets.length; ++index) {
                        var current_data = lineconfig.data.datasets[index].label;

                        if (current_data == 'Men') {
                            current_data = $men_data;
                        }
                        else {
                            current_data = $women_data;
                        }
                        lineconfig.data.datasets[index].data = current_data.middleAge;
                    }
                    window.myLine.update();
                });

                document.getElementById('culmination').addEventListener('click', function() {   
                    for (var index = 0; index < lineconfig.data.datasets.length; ++index) {
                        var current_data = lineconfig.data.datasets[index].label;

                        if (current_data == 'Men') {
                            current_data = $men_data;
                        }
                        else {
                            current_data = $women_data;
                        }
                        lineconfig.data.datasets[index].data = current_data.culmination;
                    }
                    window.myLine.update();
                });

                document.getElementById('elder').addEventListener('click', function() {
                    for (var index = 0; index < lineconfig.data.datasets.length; ++index) {
                        var current_data = lineconfig.data.datasets[index].label;

                        if (current_data == 'Men') {
                            current_data = $men_data;
                        }
                        else {
                            current_data = $women_data;
                        }
                        lineconfig.data.datasets[index].data = current_data.elder;
                    }
                    window.myLine.update();
                });
            
                var color = Chart.helpers.color;

                function add(a, b) {
                    return a + b;
                }
                  
                var barChartData = {
                    labels: ['under 18', '18-35', '35-50', '50 and older'],
                    datasets: [{
                        label: 'Men',
                        backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
                        borderColor: window.chartColors.blue,
                        borderWidth: 1,
                        data: [$men_data.under18.reduce(add, 0), $men_data.middleAge.reduce(add, 0), $men_data.culmination.reduce(add, 0), $men_data.elder.reduce(add, 0)]
                    }, {
                        label: 'Women',
                        backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
                        borderColor: window.chartColors.red,
                        borderWidth: 1,
                        data: [$women_data.under18.reduce(add, 0), $women_data.middleAge.reduce(add, 0), $women_data.culmination.reduce(add, 0), $women_data.elder.reduce(add, 0)]
                    }]
                };     
                
                var barsconfig = {
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
                };
                
                var pieconfig = {
                    type: 'pie',
                    data: {
                        datasets: [{
                            data: [
                                $men_data.percentage,
                                $women_data.percentage
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
                    var piectx = document.getElementById('pie-canvas').getContext('2d');
                    window.myPie = new Chart(piectx, pieconfig);
                    
                    var barsctx = document.getElementById('bars-canvas').getContext('2d');
                    window.myBar = new Chart(barsctx, barsconfig);
                    
                    var linectx = document.getElementById('line-canvas').getContext('2d');
                    window.myLine = new Chart(linectx, lineconfig);
                }
            </script>
        </body>
        """
    return Template(html).safe_substitute(men_data=men_data, women_data=women_data)
