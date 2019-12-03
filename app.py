from flask import Flask, render_template, url_for, request
from consume import consume
import logging
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    app.logger.info("Hey")
    data = {
        "Inputs": {
                "input1":
                [
                    {
                        'TARGET': "",   
                        'GENDER': request.form.get('GENDER'),   
                        'OCCUPATION': request.form.get('OCCUPATION'),   
                        'AGE_BKT': request.form.get('AGE_BKT'),   
                        'ACC_TYPE': request.form.get('ACC_TYPE'), 
                        'FLG_HAS_CC': int(request.form.get('FLG_HAS_CC')),
                        'FLG_HAS_ANY_CHGS': int(request.form.get('FLG_HAS_ANY_CHGS')),   
                        'FLG_HAS_NOMINEE': int(request.form.get('FLG_HAS_NOMINEE')),   
                        'FLG_HAS_OLD_LOAN': int(request.form.get('FLG_HAS_OLD_LOAN')),   
                        'LEN_OF_RLTN_IN_YRS': int(request.form.get('LEN_OF_RLTN_IN_YRS')),   
                        'NO_OF_L_CR_TXNS': int(request.form.get('NO_OF_L_CR_TXNS')),
                        'AMT_ATM_DR': int(request.form.get('AMT_ATM_DR')),
                        'AVG_AMT_PER_ATM_TXN': int(request.form.get('AVG_AMT_PER_ATM_TXN')),
                        'BALANCE': int(request.form.get('BALANCE')),   
                        'HOLDING_PERIOD': int(request.form.get('HOLDING_PERIOD')),   
                    }
                ],
            },
        "GlobalParameters":  {
        }
    }
    res = consume(data)
    label = "Sí" if res["Results"]["output1"][0]["Scored Labels"] == "1" else "No"
    probability = float(res["Results"]["output1"][0]["Scored Probabilities"]) * 100
    app.logger.info(res)
    return render_template("predict.html", label=label, probability=probability)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)