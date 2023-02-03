from kafka import KafkaConsumer, KafkaProducer
from Initializer import Initialize
import json
import pickle
import numpy as np


init_object = Initialize()



class Prediction_Consumer():

    def predict_prize(self, house_data):

        loaded_model = pickle.load(open(init_object.model_path + init_object.model_file, 'rb'))

        predicted_startup_cost = loaded_model.predict(house_data)
        #print(predicted_startup_cost[0][0])
        return predicted_startup_cost

    def gather_data(self):
        consumer = KafkaConsumer(auto_offset_reset='latest',
                                 bootstrap_servers=[init_object.kafka_host], api_version=(0, 10),
                                 consumer_timeout_ms=1000)

        consumer.subscribe(topics=['HousePrice'])  # Subscribe to a pattern

        while True:
            for message in consumer:
                if message.topic == "HousePrice":
                    house_data = (message.value.decode())
                    print(house_data)
                    house_data_list=[]
                    house_data_converted=[]
                    house_data_list=house_data.split(" ")
                    for row in house_data_list:
                        house_data_converted.append(float(row))
                    reshaped_house_data = np.array(house_data_converted).reshape(-1,75)
                    predicted_house_price = self.predict_prize(reshaped_house_data)
                    print ("Predicted Sale Price ", predicted_house_price)




if __name__ == '__main__':
    pred_consumer = Prediction_Consumer()
    pred_consumer.gather_data()
