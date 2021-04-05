#### This tool looks for valid subdomains for the given domain using the requests module in python, then it saves a .txt file with the list of subdomains found and starts scanning them to know their web technology using the tool Wappy, this scan will show you the version of the technology/framework used by the subdomain, category and confidence of it.

###### This is a project just to show a little bit of my knowledge to the SOIN team.

#### Requirements:

##### In order to run this program you should have the requests module installed in your computer.
##### In case you need to install it you can do it using the requirements.txt file that I am including here using the following commands:

##### For Windows, macOS and Linux.
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```

#### Usage:

##### You will need to provide 2 arguments when executing the program: a domain and a subdomains dictionary in .txt format.

#### Example:
```bash
python3 soin.py tesla.com subdomains_dictionary.txt
```
