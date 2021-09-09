#!/bin/bash
gunicorn -w 100 gunicorn_server:app
