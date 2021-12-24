from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)
csv_file_path = '../data/environ.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/environdata/')
@app.route('/environdata/<dateStr>')
def environdata(dateStr=None):
    with open(csv_file_path, 'r') as f:
        rawData = f.read()
        dataList = rawData.split('\n')[:-1]
        envDicts = [data_line_to_env_dict(dataLine) for dataLine in dataList]
        dateNow = datetime.now()
        splitDate = datetime(dateNow.year, dateNow.month, dateNow.day, 0, 0, 0)

        if dateStr != None:
            splitDate = datetime.strptime(dateStr, "%Y-%m-%d")

        splitDateEnd = datetime(splitDate.year, splitDate.month, splitDate.day, 23, 59, 59)
        viewableDicts = []

        for envDict in envDicts:
            dateTarget = datetime.strptime(envDict['timestamp'], '%Y-%m-%d-%H-%M-%S')
            print(dateTarget)
            if splitDate < dateTarget and dateTarget < splitDateEnd:
                viewableDicts.append(envDict)
            
        print(viewableDicts)
        return jsonify(viewableDicts)


def data_line_to_env_dict(data_line):
    data_splitted = data_line.split(',')
    return {'timestamp': data_splitted[0], 'temp': data_splitted[1], 'press': data_splitted[2], 'humid': data_splitted[3]}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)