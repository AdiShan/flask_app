from flask import Flask, redirect, url_for, request, render_template, flash
import configparser
import os

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('device_info.ini')


def station_to_ap_mode():
    os.system('sh station_to_ap_mode.sh')


def ap_to_station_mode():
    os.system('sh ap_to_station_mode.sh')


def fetch_details(ipaddress):
    for section in config.sections():
        if config.get(section, 'ip_address', fallback='') == ipaddress:
            print('fetch success %s' % section)
            return section

    return None


def submit_details(ipaddress, command=''):
    sl_no = len(config.sections())

    for section in config.sections():
        if config.get(section, 'ip_address', fallback=False) == ipaddress:
            config.set(section, 'latest_command', command)
            with open('device_info.ini', 'w') as configfile:
                print('rewrite success %s' % section)
                config.write(configfile)
            return section

    name = 'DEVICE' + str(sl_no + 1)
    config.add_section(name)
    config.set(name, 'ip_address', ipaddress)
    config.set(name, 'latest_command', command)
    with open('device_info.ini', 'w') as configfile:
        print('create success %s' % name)
        config.write(configfile)
    return name


@app.route('/all_devices')
def all_devices():
    return render_template('display_all.html', config=config)


@app.route('/device/<device_name>', methods=['POST', 'GET'])
def device_display(device_name):
    print('displaying %s' % device_name)
    ipaddress = config[device_name]['ip_address']
    command = config[device_name]['latest_command']

    if request.method == 'POST':
        new_command = request.form['newcommand']
        device_name = submit_details(ipaddress, new_command)
        return redirect(url_for('device_display', device_name=device_name))

    return render_template('device_display.html', name=device_name, ipaddress=ipaddress, command=command)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form['button'] == 'Search':
            print('in ip search')
            ip = request.form['ip']
            device_name = fetch_details(ip)
            return redirect(url_for('device_display', device_name=device_name))
            # device_display(device_name)

        elif request.form['button'] == 'Submit':
            print('in ip create')
            ip = request.form['ip']
            command = request.form['command']
            device_name = submit_details(ip, command)
            return redirect(url_for('device_display', device_name=device_name))

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
