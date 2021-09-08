# Changelog

file config.py
  - New fields
  rabbit_host -- host where rabbitMQ is installed
  ex: rabbit_host='localhost'
  list_from_prediction_size
    # 1=Yes --> show all results (list can be very large)
    # 0=No --> displays only the results of the last NR_OF_WORKERS
  ex: list_from_prediction_size = 1

