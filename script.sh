#!/bin/bash
/home/python3/.pyenv/shims/pypy3 /root/devzuul/zuulstatus/imgout.py
cat sourcedata > `date +%Y-%m-%d`
echo "{}" > sourcedata
rsync /root/zuulstatus/*.html /usr/share/nginx/html
