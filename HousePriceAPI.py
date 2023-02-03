from flask import *
import pandas as pd

app=Flask(__name__)

@app.route("/")
def housepriceform():
    return  render_template("index.html")
@app.route("/success",methods=['POST','GET'])
def housepricedata():
    if request.method == 'POST':
        print(request.form)
        result = request.form
        df=pd.DataFrame.from_dict(result,orient='index')
        df=df.T
        print(df)
        print(df.info())
        return render_template("result.html", result=result)
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)