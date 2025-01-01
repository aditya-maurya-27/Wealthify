from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recipient_name = "Aditya Maurya"
    correct_password = "wealthify"  # The password you want to set for validation
    status = None
    received_amount = None  # Variable to store the amount

    if request.method == 'POST':
        entered_password = request.form.get('password')
        amount = request.form.get('amount')  # Get the amount entered by the user
        
        if entered_password == correct_password:
            status = "success"
            received_amount = amount  # Store the received amount here
            print(f"Received Amount: {received_amount}")  # You can replace this with actual saving logic
        else:
            status = "failure"
            print("Incorrect password")
    
    return render_template('index.html', recipient_name=recipient_name, status=status, correct_password=correct_password, received_amount=received_amount)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
