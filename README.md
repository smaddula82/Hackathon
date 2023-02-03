# Hackathon
Real Time prediction of house price using ML model through kafka streaming.
config.yml - This file contains the basic settings and model details.
Initializer.py - Settings and model details are created through Initialize class.
Trainer.py - This file contains the basic classes to read the train.csv and create a model with Gradient Boost algorithm and save the basic model.
Producer.py - This file contains the classes to connect to a kafka topic - "HousePrice", read the streaming data file and send the data to kafka producer.
Consmer.py - This file contains the classes to connec to a kafka topic - "HousePrice", read the data bytes from kafka consumer and massage the data into a numpy array and predict the house price by loading the model.
