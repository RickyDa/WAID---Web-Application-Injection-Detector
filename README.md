# WAID- Web Application Injection Detector

In this project, we developed a WAF - Web Application Firewall. Nowadays, where apps are commonly robust and often keep sensitive user information, we will be interested in preventing data theft. Therefore, the need for security for said app rises, and WAF is the solution.
Some protective mechanisms exist in the lower levels of OSI model-Open Systems Interconnection. However, in those information levels, the model is incomplete, and thus attacks can bypass said protection.

In the project, we narrow our scope to protect from two kinds of attacks: SQL Injection and XSS-Cross Site Scripting. These attacks can be recognized only in the application layer, the seventh layer in the OSI model.

We used machine learning algrithms to detect if an HTTP payload contains malicious. The Training and evaluation can be found on:

https://github.com/RickyDa/BigData-Http-injections

In Addition we implemented client side application for WAID configuration as seen on the WAID-client folder.
