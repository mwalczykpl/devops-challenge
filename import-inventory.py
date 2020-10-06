#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Author: mwalczyk@gmail.com
   Import inventory file into ssh configuration file
   Please fill variables with ssh key location and usernames
"""
import sys
import yaml

bastion_username = "ubuntu"
server_username = "ubuntu"
bastion_key = "~/.ssh/id_rsa_bastion"
server_key = "~/.ssh/id_rsa_server"

if len(sys.argv) == 1:
    print("Please provide inventory file name...")
    sys.exit()

f = open(sys.argv[1])
yaml_inventory = yaml.safe_load(f)
for serverName in yaml_inventory:
    bastion_ip = yaml_inventory[serverName]['bastion']
    server_ip = yaml_inventory[serverName]['ip']
    section = f"""
Host {serverName}
  HostName {server_ip}
  User {server_username}
  IdentityFile {server_key}
  ProxyCommand ssh -W %h:%p -i {bastion_key} {bastion_username}@{bastion_ip}
    """
    print(section)