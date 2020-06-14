#!/bin/bash
#
# LICENSE: MIT
# AUTHOR: notaperson@example.com
# USE: As a temporary cron job for testing website availability
# STEPS:
#   1. Try to retrieve the first line of Example’s home page:
#        `curl -Ls $myWebsite | head -1`
#   2. If no line is returned, email system administrator (with null message
#      body):
#        mail -s "$myEmailSubject" $myEmailAddress < /dev/null
# NOTES:
#   - Don’t use "curl -Is $myWebsite | grep 200" or similar filters; servers may
#     return HTTP 200 responses for nonexistent URLs (for example, URLs
#     containing typos).
#   - The curl -L (--location) option accommodates 30x redirects.
#   - Double quotes ("$myEmailSubject") accommodate spaces.
# RESOURCES:
#   https://unix.stackexchange.com/questions/84814/health-check-of-web-page-using-curl
#   https://unix.stackexchange.com/questions/223636/sendmail-attachment/223650#223650

myWebsite='www.example.com';
myEmailAddress='sysadmin@example.com';
myEmailSubject='Example website is down!';

if [[ ! `curl -Ls $myWebsite | head -1` ]]; then
  mail -s "$myEmailSubject" $myEmailAddress < /dev/null;
fi
