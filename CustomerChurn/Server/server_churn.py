from flask import Flask,render_template,jsonify,request
import util_churn
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict_churn():
    Tenure=float(request.form['Tenure'])
    CityTier=float(request.form['CityTier'])
    WarehouseToHome=float(request.form['WarehouseToHome'])
    HourSpendOnApp=float(request.form['HourSpendOnApp'])
    NumberOfDeviceRegistered=float(request.form['NumberOfDeviceRegistered'])
    SatisfactionScore=float(request.form['SatisfactionScore'])
    NumberOfAddress=float(request.form['NumberOfAddress'])
    Complain=float(request.form['Complain'])
    OrderAmountHikeFromlastYear=float(request.form['OrderAmountHikeFromlastYear'])
    CouponUsed=float(request.form['CouponUsed'])
    OrderCount=float(request.form['OrderCount']) 
    DaySinceLastOrder=float(request.form['DaySinceLastOrder'])
    CashbackAmount=float(request.form['CashbackAmount'])
    PreferredLoginDevice=request.form['PreferredLoginDevice']
    PreferredPaymentMode=request.form['PreferredPaymentMode']
    Gender=request.form['Gender']
    PreferedOrderCat=request.form['PreferedOrderCat']
    MaritalStatus=request.form['MaritalStatus']
    
    
    #response=jsonify({'estimated_churn_prediction' : int(util_churn.get_estimated_churn(Tenure, CityTier, WarehouseToHome, HourSpendOnApp,
     #  NumberOfDeviceRegistered, SatisfactionScore, NumberOfAddress,Complain, OrderAmountHikeFromlastYear, CouponUsed, OrderCount,
     #  DaySinceLastOrder, CashbackAmount,PreferredLoginDevice,PreferredPaymentMode, Gender, PreferedOrderCat,MaritalStatus))})

    res=int(util_churn.get_estimated_churn(Tenure, CityTier, WarehouseToHome,HourSpendOnApp,NumberOfDeviceRegistered, SatisfactionScore, NumberOfAddress,Complain, OrderAmountHikeFromlastYear, CouponUsed, OrderCount,
    DaySinceLastOrder, CashbackAmount,PreferredLoginDevice,PreferredPaymentMode, Gender,PreferedOrderCat,MaritalStatus))
    if res==0:
        return render_template('index.html',prediction_text='Estimted prediction : not very likely to churn')
    else:
        return render_template('index.html',prediction_text=f'Estimted prediction : veri likely to churn')

if __name__ == "__main__":
    util_churn.load_saved_artifacts()
    app.run(debug=True)

