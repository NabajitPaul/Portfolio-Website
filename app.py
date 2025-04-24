from flask import Flask, request, jsonify, render_template
import os
import logging
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a directory for storing contact form submissions
SUBMISSIONS_DIR = 'submissions'
if not os.path.exists(SUBMISSIONS_DIR):
    os.makedirs(SUBMISSIONS_DIR)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Validate form data
        if not name or not email or not message:
            return jsonify({
                'success': False,
                'message': 'Please fill out all fields.'
            }), 400
            
        # Log the submission
        logger.info(f"Form submission received from {name} ({email})")
        
        # Save the submission to a file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SUBMISSIONS_DIR}/contact_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Message: {message}\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # In a real application, you might send an email here
        # or store the submission in a database
        
        return jsonify({
            'success': True,
            'message': 'Thanks for your message! I\'ll get back to you soon.'
        })
        
    except Exception as e:
        logger.error(f"Error processing form submission: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Something went wrong. Please try again.'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
