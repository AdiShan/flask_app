#!/bin/sh

sudo systemctl restart dhcpcd
sudo systemctl start hostapd
sudo systemctl start dnsmasq


