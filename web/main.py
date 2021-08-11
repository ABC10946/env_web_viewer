from flask import Flask, render_template, jsonify

app = Flask(__name__)
csv_file_path = '../data/environ.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/environdata')
def environdata():
    with open(csv_file_path, 'r') as f:
        raw_data = f.read()
        data_list = raw_data.split('\n')[:-1]
        env_dicts = [data_line_to_env_dict(data_line) for data_line in data_list]
        return jsonify(env_dicts)


def data_line_to_env_dict(data_line):
    data_splitted = data_line.split(',')
    return {'timestamp': data_splitted[0], 'temp': data_splitted[1], 'press': data_splitted[2], 'humid': data_splitted[3]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)