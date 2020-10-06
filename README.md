<h1 align="center">Welcome to Devops challenge 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000" />
</p>

<h2 align="center">Challenge</h2>
Consider having an inventory in the following format (yaml):<br />
server1:<br />
ip: 192.168.0.1<br />
bastion: 212.186.105.45<br />
server2:<br />
ip: 192.168.0.2<br />
bastion: 212.186.105.45<br />
server3:<br />
ip: 192.168.0.3<br />
bastion: 212.186.105.48<br />
server4:<br />
ip: 192.168.0.4<br />
bastion: 212.186.105.49<br />
serverN:<br />
.....<br />
To remotely login (ssh) to any of the servers with the given ip you have to jump over a bastion
host defined for the given server.<br />
Question 1<br />
Assuming the login username to all servers is ubuntu and we have public key authentication
(your public key is already on all of those hosts), how would you log in to a server?<br />
Question 2<br />
There can be thousands of servers in the inventory. You might need to log in remotely multiple
times per hour to arbitrary servers from the list. How would you ease this process?<br />

<h2 align="center">Anwsers</h2>

I would use ProxyCommand with ssh. To use it once I would do:<br />
```
ssh -o ProxyCommand="ssh -W %h:%p bastion-host" remote-host

ssh -o ProxyCommand="ssh -W %h:%p ubuntu@212.186.105.45" ubuntu@192.168.0.1
```
Another option is to use -J flag in ssh (available from version 7.3 of ssh)<br />
```
ssh -J <bastion-host> <remote-host>

ssh -J ubuntu@212.186.105.45 ubuntu@192.168.0.1
```
To simplify login process I wrote simple script to create Host entries in .ssh/config. With many entries in .ssh/config file it's a good idea to give them a good name to make use of autocomplete feature.
```
python3 import-inventory.py inventory.yml >> ~/.ssh/config
```
This allow login to server with simple ssh command like
```
ssh server4
```

## Author

👤 **Mariusz Walczyk**

* Website: https://mwalczyk.pl
* Github: [@mwalczykpl](https://github.com/mwalczykpl)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/mwalczyk-it\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/mwalczyk-it\/)
