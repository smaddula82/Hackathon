from flask import *
import pandas as pd
from HousePricePredict.DataProducer import Data_Streamer


app=Flask(__name__)

@app.route("/")
def housepriceform():
    return  render_template("index.html")
@app.route("/success",methods=['POST','GET'])
def housepricedata():
    if request.method == 'POST':
        print(request.form)
        result = request.form
        df = pd.DataFrame.from_dict(result, orient='index')
        df = df.T
        stream_obj=Data_Streamer(df.to_string(index=False,header=False))
        stream_obj.stream_data()
        return render_template("result.html", result=result)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)