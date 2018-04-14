from string import Template


def main_body(male_data, female_data):

    html = """
        <head>
            <link rel="stylesheet" href="./css/style.css">
            <script src="./js/chart.js"></script>
    	    <script src="./js/utils.js"></script>
        </head>
        <body>   
            <div id="line">
                <canvas id="line-canvas"></canvas>
                <button id="maleOnly">Men</button>
                <button id="femaleOnly">Women</button>
                <button id="everyone">Everyone</button>
                <br>
                <button id="under18">Under 18</button>
                <button id="middleAge">18-35</button>
                <button id="culmination">35-50</button>
                <button id="elder">Above 50</button>
                <br>
            </div>  
             
            <div id="container">
                <div id="bars">
                    <canvas id="bars-canvas"></canvas>
                </div>
                <br><br><br><br><br>
                <div id="pie">
                    <canvas id="pie-canvas"></canvas>
                </div>
            </div>
            
            <br>
            
            <script>
                var main_data = [{
                    label: 'Male',
                    backgroundColor: window.chartColors.blue,
                    borderColor: window.chartColors.blue,
                    data: $male_data.total,
                    fill: false,
                },
                {
                    label: 'Female',
                    backgroundColor: window.chartColors.red,
                    borderColor: window.chartColors.red,
                    data: $female_data.total,
                    fill: false,
                }];
                var lineconfig = {
                    type: 'line',
                    data: {
                        labels: ['0', '4', '8', '12', '16', '20', '24'],
                        datasets: main_data
                    },
                    options: {
                        responsive: true,
                        tooltips: {
                            mode: 'i',
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
                
                document.getElementById('everyone').addEventListener('click', function() {
                    lineconfig.data.datasets = main_data;
                    window.myLine.update();
                });

                document.getElementById('maleOnly').addEventListener('click', function() {
                    lineconfig.data.datasets = [main_data[0]];
                    window.myLine.update();
                });

                document.getElementById('femaleOnly').addEventListener('click', function() {
                    lineconfig.data.datasets = [main_data[1]];
                    window.myLine.update();
                });

                document.getElementById('under18').addEventListener('click', function() {

                    for (var i = 0; i < lineconfig.data.datasets.length; ++i) {
                        var current_data = lineconfig.data.datasets[i].label;

                        if (current_data == 'Male') {
                            current_data = $male_data;
                        }
                        else {
                            current_data = $female_data;
                        }
                        lineconfig.data.datasets[i].data = current_data.under18;
                    }
                    window.myLine.update();
                });

                document.getElementById('middleAge').addEventListener('click', function() { 
                    for (var i = 0; i < lineconfig.data.datasets.length; ++i) {
                        var current_data = lineconfig.data.datasets[i].label;

                        if (current_data == 'Male') {
                            current_data = $male_data;
                        }
                        else {
                            current_data = $female_data;
                        }
                        lineconfig.data.datasets[i].data = current_data.middleAge;
                    }
                    window.myLine.update();
                });

                document.getElementById('culmination').addEventListener('click', function() {   
                    for (var i = 0; i < lineconfig.data.datasets.length; ++i) {
                        var current_data = lineconfig.data.datasets[i].label;

                        if (current_data == 'Male') {
                            current_data = $male_data;
                        }
                        else {
                            current_data = $female_data;
                        }
                        lineconfig.data.datasets[i].data = current_data.culmination;
                    }
                    window.myLine.update();
                });

                document.getElementById('elder').addEventListener('click', function() {
                    for (var i = 0; i < lineconfig.data.datasets.length; ++i) {
                        var current_data = lineconfig.data.datasets[i].label;

                        if (current_data == 'Male') {
                            current_data = $male_data;
                        }
                        else {
                            current_data = $female_data;
                        }
                        lineconfig.data.datasets[i].data = current_data.elder;
                    }
                    window.myLine.update();
                });
            
                var color = Chart.helpers.color;

                function add(a, b) {
                    return a + b;
                }
                
                var barsconfig = {
                    type: 'bar',
                    data: {
                        labels: ['under 18', '18-35', '35-50', '50 and older'],
                        datasets: [{
                            label: 'Male',
                            backgroundColor: Chart.helpers.color(window.chartColors.blue).alpha(0.5).rgbString(),
                            borderColor: window.chartColors.blue,
                            borderWidth: 1,
                            data: [
                                $male_data.under18.reduce(add, 0), 
                                $male_data.middleAge.reduce(add, 0), 
                                $male_data.culmination.reduce(add, 0), 
                                $male_data.elder.reduce(add, 0)]
                        }, {
                            label: 'Female',
                            backgroundColor: Chart.helpers.color(window.chartColors.red).alpha(0.5).rgbString(),
                            borderColor: window.chartColors.red,
                            borderWidth: 1,
                            data: [
                                $female_data.under18.reduce(add, 0), 
                                $female_data.middleAge.reduce(add, 0), 
                                $female_data.culmination.reduce(add, 0), 
                                $female_data.elder.reduce(add, 0)]
                        }]
                    },
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
                                $male_data.percentage,
                                $female_data.percentage
                            ],
                            backgroundColor: [
                                window.chartColors.blue,
                                window.chartColors.red,
                            ],
                        }],
                        labels: [
                            'Male',
                            'Female'
                        ]
                    },
                    options: {
                        responsive: true
                    }
                };
        
                window.onload = function() {
                    var piecontex = document.getElementById('pie-canvas').getContext('2d');
                    window.myPie = new Chart(piecontex, pieconfig);
                    
                    var barscontex = document.getElementById('bars-canvas').getContext('2d');
                    window.myBar = new Chart(barscontex, barsconfig);
                    
                    var linecontex = document.getElementById('line-canvas').getContext('2d');
                    window.myLine = new Chart(linecontex, lineconfig);
                }
            </script>
        </body>
        """
    return Template(html).safe_substitute(male_data=male_data, female_data=female_data)
