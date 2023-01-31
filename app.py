from flask import Flask
from flask import request
from flask import jsonify
import pickle
import numpy as np


model=pickle.load(open('int_model.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def home():
    return "chalja"

@app.route('/predict',methods=['POST'])

def predict():
    texture=request.form.get('texture')
    colour=request.form.get('colour')
    size=request.form.get('size')

    # result={'texture':texture,
    #         'colour':colour,
    #         'size':size
    #         }

    input_q=np.array([[texture,colour,size]])

    result=model.predict(input_q)[0]

    return jsonify({'position':str(result)})

if __name__=='__main__':
    app.run(debug=True)