from flask import Flask, render_template, request

app = Flask(__name__)

# Threshold values for Good Response (GR)
gr_thresholds = {
    'bmi': 27.71,
    'afc': 8.76,
    'fsh': 6.45,
    'amh': 3.16,
    'lh': 851,
    'oestradiol': 44.60
}

# Threshold values for Bad Response (PR)
pr_thresholds = {
    'bmi': 26.54,
    'afc': 5.38,
    'fsh': 7.60,
    'amh': 1.67,
    'lh': 6.26,
    'oestradiol': 74.45
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from form
    bmi = float(request.form['bmi'])
    afc = float(request.form['afc'])
    fsh = float(request.form['fsh'])
    amh = float(request.form['amh'])
    lh = float(request.form['lh'])
    oestradiol = float(request.form['oestradiol'])
    
    # Prediction logic based on comparison
    response = "Bad Response (PR)"
    
    # Compare input values with GR thresholds
    if (bmi <= gr_thresholds['bmi'] and afc >= gr_thresholds['afc'] and 
        fsh <= gr_thresholds['fsh'] and amh >= gr_thresholds['amh'] and 
        lh <= gr_thresholds['lh'] and oestradiol <= gr_thresholds['oestradiol']):
        response = "Good Response (GR)"
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
