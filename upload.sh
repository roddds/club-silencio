#! /usr/bin/env bash
lftp -c "open -u $CS_USERNAME,$CS_PASSWORD ftp.club-silencio.com; set ssl:verify-certificate no; mirror -R ${PWD}/build/ /public_html"
