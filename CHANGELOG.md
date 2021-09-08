# Changelog

1. file config.py

      New fields:

      rabbit_host -- host where rabbitMQ is installed

      ex: rabbit_host='localhost'

      list_from_prediction_size

        1=Yes --> show all results on Inference Stats (list can be very large)

        0=No --> displays only the results of the last NR_OF_WORKERS on Inference Stats

      ex: list_from_prediction_size = 1
  
2. Inference Stats 

      add column Nr. of row
4. Send Request continues 

        creating a defined number of threads (corresponding to NR_OF_WORKERS from config.py) 
        that send requests continuously at an interval of 1sec
    
4. Add "Stop Request" button
5. In LSTM_P.py

        +import os
        
        +os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        
        +os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        
        CUDA_VISIBLE_DEVICES
        
          for CPU vs GPU selection
          ex:
          CPU -> CUDA_VISIBLE_DEVICES = -1
          GPU -> CUDA_VISIBLE_DEVICES = 0 or 1 or n GPU per device

        TF_CPP_MIN_LOG_LEVEL level logs for GPU
          TF_CPP_MIN_LOG_LEVEL = 3 (no)
          
6. inference_service.py

        model initialization
        model = LSTM_P(tempfile.gettempdir() + '/binary_model.h5')

7. changed '/tmp' to tempfile.gettempdir () so you can test on windows machine
