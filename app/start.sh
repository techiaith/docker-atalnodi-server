#!/bin/bash
#echo "Starting CherryPy..."
supervisord -c /app/cherrypy.conf
sleep infinity