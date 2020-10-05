#!/bin/sh

mv /etc/dhcpcd.conf /etc/dhcpcd.conf.station
mv /etc/dhcpcd.conf.ap /etc/dhcpcd.conf
sudo systemctl start hostapd
sudo systemctl start dnsmasq
sudo systemctl restart dhcpcd