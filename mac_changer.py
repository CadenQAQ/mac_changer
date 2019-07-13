#!/usr/bin/env python3

import subprocess
import optparse
import re

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

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(
        ["ifconfig", interface]).decode()  # ifconfig_result is a byte, .decode() make it a string

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)  # pythex

    if mac_address_search_result:

        return mac_address_search_result.group(0)  # if there are several items match the rule we can iterate thought them
    else:
        print("There is no mac address")

options = get_arguments()


current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))


change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)

else:
    print("[-] MAC address did not get changed")

