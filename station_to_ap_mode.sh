#!/bin/sh

sudo mv /etc/dhcpcd.conf.ap /etc/dhcpcd.conf
sudo mv /etc/dhcpcd.conf /etc/dhcpcd.conf.station
sleep 1
sudo systemctl restart dhcpcd
sleep 1
sudo systemctl start hostapd
sleep 1
sudo systemctl start dnsmasq

