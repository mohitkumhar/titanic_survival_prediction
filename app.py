import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Pclass = int(request.form['Pclass'])
    Age = int(request.form['Age'])
    Fare = float(request.form['Fare'])
    familySize = int(request.form['familySize'])
    Sex = request.form['Sex']
    Embarked = request.form['Embarked']
    Title = request.form['Title']
    
    input_data = pd.DataFrame(
        {
            'Pclass': [Pclass],
            'Age' : [Age],
            'Fare': [Fare],
            'familySize' : [familySize],
            'Sex' : [Sex],
            'Embarked' : [Embarked],
            'Title' : [Title],
        }
    )
    
    
    prediction = model.predict(input_data)
    
    return render_template('index.html', prediction_text='Survive' if prediction[0] == 1 else 'Not - Survive')

if __name__ == '__main__':
    app.run(debug=True)

