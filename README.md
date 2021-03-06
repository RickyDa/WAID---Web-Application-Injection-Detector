<img src="https://github.com/RickyDa/WAID---Web-Application-Injection-Detector/blob/master/assets/logo.png" height="250" width="300">

# WAID- Web Application Injection Detector

In this project, we developed a WAF - Web Application Firewall. Nowadays, where apps are commonly robust and often keep sensitive user information, we will be interested in preventing data theft. Therefore, the need for security for said app rises, and WAF is the solution.
Some protective mechanisms exist in the lower levels of OSI model-Open Systems Interconnection. However, in those information levels, the model is incomplete, and thus attacks can bypass said protection.

In the project, we narrow our scope to protect from two kinds of attacks: SQL Injection and XSS-Cross Site Scripting. These attacks can be recognized only in the application layer, the seventh layer in the OSI model.

We used machine learning algrithms to detect if an HTTP payload contains malicious. The Training and evaluation can be found on:

https://github.com/RickyDa/BigData-Http-injections

In Addition we implemented client side application for WAID configuration as seen on the WAID-client folder.

***NOTE: On real world WAFs are implemented as a reverse proxy, on our project we implemented it as a proxy to showcase our results.***

<img src="https://github.com/RickyDa/WAID---Web-Application-Injection-Detector/blob/master/assets/archi.png" height="450" width="300">


# Installation 
> Server Mode
```
ADDRESS="UR_SERVER_IP" docker-compose -f docker-compose-server.yml up --build 
```
> ADDRESS arg is optional, if not provided UR_SERVER_IP is localhost by default (So you can test it on ur local computer). Recommended to install on a remote server and use the client mode on local to exeperince the full project flow. In addition u can configure the site you would like to secure on the control panel.


> client Mode
```
docker-compose -f docker-compose-client.yml up --build 
```

> After intalling the client mode containers some configuration must be done, go to http://localhost:3000 and configure the remote server IP adress.

 # Requirments:
 
> Install docker and docker compose and you are ready to go. 

**OR**

> Run the setup.sh script
```
sudo bash setup.sh
```








