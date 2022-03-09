function drawEnvData() {
    csvData = ''
    fetch('/environdata')
        .then(response => response.json())
        .then(graphDraw)
}

function drawEnvSelectedDate(date) {
    fetch('/environdata/' + date)
        .then(response => response.json())
        .then(graphDraw)
}

function graphDraw(envData) {
    timestamps = ['timestamp']
    temps = ['temperature']
    presses = ['pressure']
    humids = ['humidity']

    for (let idx in envData) {
        timestamps.push(envData[idx]['timestamp'])
        temps.push(parseFloat(envData[idx]['temp']))
        presses.push(parseFloat(envData[idx]['press']))
        humids.push(parseFloat(envData[idx]['humid']))
    }

    let chart = c3.generate({
        bindto: '#chart',
        size: { width: window.width, height: 600 },
        data: {
            x: 'timestamp',
            xFormat: '%Y-%m-%d-%H-%M-%S',
            columns: [
                timestamps,
                temps,
                presses,
                humids,
            ],
            axes: {
                'temperature': 'y',
                'humidity': 'y',
                'pressure': 'y2',
            },
            colors: {
                'temperature': '#ff0000',
                'humidity': '#0000ff',
                'pressure': '#00ff00'
            },
        },
        axis: {
            x: {
                type: 'timeseries',
                localtime: true,
                tick: {
                    format: '%Y-%m-%d-%H-%M-%S'
                },
                label: {
                    text: '記録時間',
                    position: 'outer-center'

                }
            },
            y: {
                label: {
                    text: '温度/℃・湿度/%',
                    position: 'outer-middle'
                }
            },
            y2: {
                label: {
                    text: '気圧/hPa',
                    position: 'outer-middle'
                },
                show: true
            }
        },
        subchart: {
            show: true
        }
    })

}




window.onload = function () {
    drawEnvData()
    const splitDate = document.getElementById('splitDate')
    splitDate.addEventListener('change', function () {
        drawEnvSelectedDate(splitDate.value)
    })

}

window.onresize = function () {
    drawEnvData()
}