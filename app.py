from flask import Flask,request,jsonify
import numpy as np
import pandas as pd 
import pickle
import sklearn
app=Flask(__name__)


@app.route('/')
def index():
    return "Hello world"

model=pickle.load(open('RFC.pkl','rb'))

@app.route('/predict',methods=['POST'])
def predict():
    age=request.form.get('age')
    bp=request.form.get('bp')
    su=request.form.get('su')
    al=request.form.get('al')
    sg=request.form.get('sg')
    rbc=request.form.get('rbc')
    pcc=request.form.get('pcc')
    pc=request.form.get('pc')
    ba=request.form.get('ba')
    bgr=request.form.get('bgr')
    bu=request.form.get('bu')
    sc=request.form.get('sc')
    sd=request.form.get('sd')
    pot=request.form.get('pot')
    hemo=request.form.get('hemo')
    pcv=request.form.get('pcv')
    wc=request.form.get('wc')
    rc=request.form.get('rc')
    htn=request.form.get('htn')
    dm=request.form.get('dm')
    cad=request.form.get('cad')
    appet=request.form.get('appet')
    pe=request.form.get('pe')
    ane=request.form.get('ane')

    prediction=model.predict(pd.DataFrame(columns=[
      'age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','htn','dm','cad','appet','pe','ane'],
        data=np.array([
        age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sd,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]).reshape(1,24)))
    print(prediction)

    return jsonify({'placement': str(prediction)})



if __name__=='__main__':
    app.debug = True

    app.run()
