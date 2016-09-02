##Requirements
* Python 2.7
* bs4
* requests

##Description
* Scrapes "recent domains" from malwr.com's main page

##SSL Errors
If you receive "InsecurePlatformWarning" error install requests[security] package by running `pip install requests[security]`

This will install three additional packages:

* pyOpenSSL
* ndg-httpsclient
* pyasn1

