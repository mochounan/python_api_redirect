#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  :  nan
# @File     : redirect.py
import requests
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def check_for_redirects(url):
    try:
        r = requests.get(url, allow_redirects=False, timeout=0.5)
        if 300 <= r.status_code < 400:
            return r.headers['location']
        else:
            return '[no redirect]'
    except requests.exceptions.Timeout:
        return '[timeout]'
    except requests.exceptions.ConnectionError:
        return '[connection error]'


def check_domains(urls):
    for url in urls:
        url_to_check = url if url.startswith('http') else "http://%s" % url
        redirect_url = check_for_redirects(url_to_check)
        print("%s => %s" % (url_to_check, redirect_url))


if __name__ == '__main__':
    domains = [
        'http://127.0.0.1:5050/search_api_info/trustgroup1/'
    ]
    try:
        fname = sys.argv[1]
    except IndexError:
        for url in domains:
            check_domains(url)
