#! /usr/bin/env python3
#
# Wait for NETCONF call-home connection from Orbit/Orbit-X on the given
# local host address/port, establish connection using public-key based
# authentication, retrieve its running config (in XML format) and write
# it to a file.
#
# $ ./get_config_pka_ch.py 192.168.1.7 4334 nms <path-to-id_rsa> <path-to-ssh-config>

import sys, os, warnings
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager
import xmltodict
import json

import logging
#logging.basicConfig(level=logging.DEBUG)

def demo(host, port, user, key_filename, ssh_config):
     with manager.call_home(
        host=host,
        port=port,
        username=user,
        key_filename=key_filename,
        allow_agent=False,
        look_for_keys=False,
        hostkey_verify=False,
        ssh_config=ssh_config,
        timeout=180,
        device_params = {'name':'orbit'}) as m:
        # read serial number of Orbit
        sn = m.get(filter=('xpath',"/system/serial-number-platform")).data_xml
        sn = xmltodict.parse(sn)
        sn = sn['data']['system']['serial-number-platform']['#text']
        print('Device S/N:', sn)

        # get configuration and write it in <sn>.xml file.
        c = m.get_config(source='running').data_xml
        c = json.dumps(xmltodict.parse(c))
        with open("%s.json" % sn, 'w') as f:
            f.write(c)

if __name__ == '__main__':
    demo(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5])
