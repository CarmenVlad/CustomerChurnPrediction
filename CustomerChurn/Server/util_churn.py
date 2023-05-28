import json,pickle,numpy as np

__locations=None
__data_columns=None
__model=None

def get_estimated_churn(Tenure, CityTier, WarehouseToHome, HourSpendOnApp,
       NumberOfDeviceRegistered, SatisfactionScore, NumberOfAddress,Complain, OrderAmountHikeFromlastYear, CouponUsed, OrderCount,
       DaySinceLastOrder, CashbackAmount,PreferredLoginDevice,PreferredPaymentMode, Gender, PreferedOrderCat,MaritalStatus):

    x=np.array([])
    x=np.zeros(len(__data_columns))

    x[0]=Tenure
    x[1]=CityTier
    x[2]=WarehouseToHome
    x[3]=HourSpendOnApp
    x[4]=NumberOfDeviceRegistered
    x[5]=SatisfactionScore
    x[6]=NumberOfAddress
    x[7]=Complain
    x[8]=OrderAmountHikeFromlastYear
    x[9]=CouponUsed
    x[10]=OrderCount
    x[11]=DaySinceLastOrder
    x[12]=CashbackAmount
    x[13]=x[10]/x[12]
    
    if PreferredLoginDevice != 'Computer':
        index_PreferredLoginDevice=__data_columns.index('PreferredLoginDevice_' + PreferredLoginDevice)
        if index_PreferredLoginDevice>0: 
            x[index_PreferredLoginDevice]=1
     
    if PreferredPaymentMode!='CC':
        index_PreferredPaymentMode=__data_columns.index('PreferredPaymentMode_' + PreferredPaymentMode)
        if index_PreferredPaymentMode>0: 
            x[index_PreferredPaymentMode]=1
            
    if Gender != 'Female':  
        index_Gender=__data_columns.index('Gender_' + Gender)
        if index_Gender>0: 
            x[index_Gender]=1
            
    if PreferedOrderCat != 'Fashion':
        index_PreferedOrderCat=__data_columns.index('PreferedOrderCat_' + PreferedOrderCat)
        if index_PreferedOrderCat>0: 
            x[index_PreferedOrderCat]=1
    
    if MaritalStatus != 'Divorced':
        index_MaritalStatus=__data_columns.index('MaritalStatus_' + MaritalStatus)
        if index_MaritalStatus>0: 
            x[index_MaritalStatus]=1
 
    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print('loading saved artifacts..starting')
    
    global __data_columns
    global __locations
    global __model
    
    with open('./artifacts/customer_churn_json','r') as f:
       __data_columns= json.load(f)['data_columns']
       __locations= __data_columns[3:]
    with open('./artifacts/customer_churn_pickle','rb') as fp:
        __model=pickle.load(fp)
    
    print('loading saved artifacts...ending')
    
if __name__=='__main__':
    load_saved_artifacts()
    get_location_names()
   
    