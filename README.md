# Phone tree demo

Based on Twilio's example provided here: https://github.com/TwilioDevEd/ivr-phone-tree-python

The example has been cleaned up, with all 10-year-old dependencies upgraded, and all the necessary changes made for running with Python 3. A Dockerfile and a docker compose file are also made to facilitate easy testing. You will need to modify the `Caddyfile` with your own domain and generate a new password for HTTP Basic auth.

For using HTTP Basic auth with Twilio webhooks, read the tutorial here: https://www.twilio.com/docs/usage/webhooks/webhooks-security#http-authentication
