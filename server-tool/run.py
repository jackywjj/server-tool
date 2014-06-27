import os
import json

from flask import Flask
app = Flask(__name__)

bin_path = os.path.join(os.path.dirname(__file__), "bin")

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/server/cpu/')
def server_cpu():
	html = {}
	command = os.path.join(bin_path, "check_cpu.sh")
	result = os.popen(command).readlines()
	tmp =[]
	for n in result:
		x = format(decimal.Decimal(n), ".6f")
		tmp.append(str(x))
	html['load_1'] = tmp[0]
	html['load_5'] = tmp[1]
	html['load_15'] = tmp[2]
	return json.dumps(html)

@app.route('/server/memory/')
def server_memory():
	html = {}
	command = os.path.join(bin_path, "check_mem.sh")
	result = os.popen(command).readlines()
	tmp = result[0].split(' ')

	html['total'] = tmp[0].strip()
	html['used'] = tmp[1].strip()
	html['free'] = tmp[2].strip()
	return json.dumps(html)

@app.route('/server/disk/')
def server_disk():
	html = {}
	command = os.path.join(bin_path, "check_disk.sh")
	result = os.popen(command).readlines()
	html['disk_left'] = result[0].strip()
	html['disk_percent'] = result[1].strip()
	return json.dumps(html)

@app.route('/server/nginx/')
def server_nginx():
	html = {}
	command = os.path.join(bin_path, "check_nginx.sh")
	result = os.popen(command).readlines()
	html['nginx'] = result[0].strip()
	return json.dumps(html)

@app.route('/server/mysql/')
def server_mysql():
	html = {}
	command = os.path.join(bin_path, "check_mysql.sh")
	result = os.popen(command).readlines()
	html['mysql'] = result[0].strip()
	return json.dumps(html)

@app.route('/server/phpfpm/')
def server_phpfpm():
	html = {}
	command = os.path.join(bin_path, "check_php.sh")
	result = os.popen(command).readlines()
	html['phpfpm'] = result[0].strip()
	return json.dumps(html)

@app.route('/server/gunicorn/')
def server_gunicorn():
	html = {}
	command = os.path.join(bin_path, "check_gunicorn.sh")
	result = os.popen(command).readlines()
	html['gunicorn'] = result[0].strip()
	return json.dumps(html)

if __name__ == '__main__':
	app.debug = True
	app.run()