#!/bin/sh

sudo mv /etc/dhcpcd.conf /etc/dhcpcd.conf.ap
sudo mv /etc/dhcpcd.conf.station /etc/dhcpcd.conf
sleep 1
sudo systemctl stop dnsmasq
sleep 1
sudo systemctl stop hostapd
sleep 1
sudo systemctl restart dhcpcd
