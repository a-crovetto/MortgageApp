$(function () {
    $('#years-chart').highcharts({
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Wind speed during two days'
        },
        subtitle: {
            text: 'en 25 años'
        },
        xAxis: {
            min: 1,
            tickInterval: 1,
            labels: {
                overflow: 'justify'
            }
        },
        yAxis: {
            title: {
                text: 'Moneda ($)'
            },
            min: 0,
            minorGridLineWidth: 0,
            gridLineWidth: 0,
            alternateGridColor: null,
        },
        tooltip: {
            valueSuffix: ' $'
        },
        plotOptions: {
            spline: {
                lineWidth: 4,
                states: {
                    hover: {
                        lineWidth: 5
                    }
                },
                marker: {
                    enabled: false
                },
            }
        },
        series: [{
            name: 'Pago mensual',
            data: [8653,4477,3088,2395,1980,1705,1509,1363,1251,1161,1088,1028,978,935,899,867,840,816,794,
                   775,758,743,730,718,707
                   ],
                    pointStart: 1
        }],
        navigation: {
            menuItemStyle: {
                fontSize: '10px'
            }
        },
        credits: {
            enabled: false
        }
    });
});