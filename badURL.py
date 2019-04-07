"""
Your module description
"""
import certifi
import urllib3 as url
import sys

http = url.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
request = 'GET'
url= 'https://expired.badssl.com'
r = http.request(request, url)
r.status

