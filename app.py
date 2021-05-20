from flask import Flask, request, render_template
from spacy import load

app = Flask(__name__)
model = load('model_spacy')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text = str(request.form['text'])
    doc = model(text)
    
    l=[(X.text, X.label_) for X in doc.ents]
    
    if len(l)>0:
        label = l[0][1]
    else:
        label = 'None'

    output = label

    return render_template('index.html', prediction_text='{}'.format(text), prediction_entity = '{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)