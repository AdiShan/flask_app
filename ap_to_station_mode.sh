#!/bin/sh

mv /etc/dhcpcd.conf /etc/dhcpcd.conf.ap
mv /etc/dhcpcd.conf.station /etc/dhcpcd.conf
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
sudo systemctl restart dhcpcd