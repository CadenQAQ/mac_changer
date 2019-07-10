#!/usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()  # OptionParser is a class, and parser is an instance
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("Please specify an interface, use --help for more info.")  # if the user does not input the int
    elif not options.new_mac:
        parser.error("Please specify a new mac, use --help for more info.") # if the user does not input the mac

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



options = get_arguments()
change_mac(options.interface, options.new_mac)

