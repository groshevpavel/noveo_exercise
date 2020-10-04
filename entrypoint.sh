#!/bin/bash

exec gunicorn wsgi:app --name noveo_exercise --workers ${CONCURRENCY:-8} -b 0.0.0.0:5000 --timeout=600
