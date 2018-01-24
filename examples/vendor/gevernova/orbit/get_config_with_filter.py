#! /usr/bin/env python3
#
# Connect to the Orbit/Orbit-X NETCONF server using password based
# authentication, retrieve its running config (in XML format) using an
# XPath filter, and write it to a file.
#
# $ ./get_config_with_filter.py 192.168.1.1 admin admin

import sys, os, warnings
from lxml import etree
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

import logging
#logging.basicConfig(level=logging.DEBUG)

FILTER_XPATH = (
    "/*["
    "not(self::logging) and "
    "not(self::nacm) and "
    "not(self::services) and "
    "not(self::product-features) and "
    "not(self::SNMP-COMMUNITY-MIB) and "
    "not(self::SNMP-NOTIFICATION-MIB) and "
    "not(self::SNMP-TARGET-MIB) and "
    "not(self::SNMP-USER-BASED-SIM-MIB) and "
    "not(self::SNMP-VIEW-BASED-ACM-MIB) and "
    "not(self::SNMPv2-MIB)"
    "] | "
    "/services/*[not(self::snmp) and not(self::io)] | "
    "/services/snmp/*[not(self::notify)] | "
    "/services/io/pin | /services/io/enabled | "
    "/logging/*[not(self::default-event-rule) and not(self::default-alarm-output)]"
)


def demo(host, user, passwd):
     with manager.connect(
        host=host,
        port=830,
        username=user,
        password=passwd,
        allow_agent=False,
        look_for_keys=False,
        hostkey_verify=False,
        device_params = {'name':'orbit'}) as m:
        reply = m.get_config(source='running', filter=('xpath', FILTER_XPATH))
        data_element = reply.data_ele
        if data_element is None:
            raise RuntimeError("No <data> element returned in NETCONF reply")

        config_element = etree.Element('config')
        config_element.set('xmlns', 'http://tail-f.com/ns/config/1.0')
        for child in list(data_element):
            config_element.append(child)

        config_xml = etree.tostring(config_element, pretty_print=True, encoding='unicode')
        with open("%s.xml" % host, 'w') as f:
            f.write(config_xml)

if __name__ == '__main__':
    demo(sys.argv[1], sys.argv[2], sys.argv[3])
