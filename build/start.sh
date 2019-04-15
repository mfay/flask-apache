#!/bin/bash

/usr/sbin/httpd -k start
echo 'Apache started'

tail -f /dev/null
