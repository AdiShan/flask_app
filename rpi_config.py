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


def fetch_current_mode():
    if config.get('MODE', 'ap') == 'True':
        mode = 'Access Point'
        print('in AP mode')
    else:
        mode = 'Station'
        print('in Station mode')

    return mode


def set_current_mode(mode):
    if mode == 'Station':
        config.set('MODE', 'ap', 'True')
    elif mode == 'Access Point':
        config.set('MODE', 'ap', 'False')


@app.route('/rpi_mode', methods=['POST', 'GET'])
def rpi_mode():
    mode = fetch_current_mode()
    if request.method == 'POST':
        print('post')
        if request.form['button']:
            print('button successful')
            if mode == 'Station':
                station_to_ap_mode()
            else:
                ap_to_station_mode()
            set_current_mode(mode)

        mode = fetch_current_mode()
    return render_template('toggle.html', mode=mode)


if __name__ == '__main__':
    app.run(debug=True)