from flask import Flask, request, render_template
import joblib 

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
# Make sure 'emailSpamDet.pkl' is in the same directory as this script
try:
    model = joblib.load('emailSpamDet.pkl')
except FileNotFoundError:
    print("Error: 'emailSpamDet.pkl' not found. Ensure the file is in the same directory as this script.")
    exit()

# Route for the home page
@app.route('/')
def home():
    # Ensure 'index.html' is located in the 'templates' folder
    return render_template('index.html')

# Route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get email text from the form input named 'email_text'
        email_text = request.form.get('email_text', '')
        
        if not email_text.strip():
            # Handle empty input
            return render_template('index.html', prediction="Please provide email content to analyze.")
        
        # Use the model to make a prediction
        prediction = model.predict([email_text])[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        
        # Pass the result back to the frontend
        return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True) //
