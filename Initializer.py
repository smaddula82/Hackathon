import traceback
import yaml

class Initialize:
    def __init__(self):
        print("object created")
        try:
            with open('config.yml','r') as f:
                config=yaml.load(f,Loader=yaml.FullLoader)
                print(config)
                self.data_path=config['settings']['data_path']
                self.data_file=config['settings']['data_file']
                self.streaming_file=config['settings']['streaming_file']
                self.kafka_host=config['settings']['kafka_host']
                self.model_path=config['model']['model_path']
                self.model_file=config['model']['model_file']
                self.test_file=config['settings']['test_file']
        except Exception as e:
            traceback.print_exc()


#new_obj=Initialize()
#print(new_obj.data_path,new_obj.data_file,new_obj.streaming_file,new_obj.kafka_host,new_obj.model_path,new_obj.model_file)