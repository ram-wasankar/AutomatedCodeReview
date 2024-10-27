Code Review Application

This Flask application enables a backend server that provides a REST API to review code snippets. It interfaces with the Google Generative Language API to process the submitted code, analyze it, and return feedback or insights. The app is configured to serve a frontend HTML/CSS interface alongside the backend API.
Features

    Accepts code snippets via a POST request to the /review endpoint.
    Analyzes code using the Google Generative Language API (Gemini model).
    Serves a simple frontend with index.html and styles.css.
    Supports CORS to enable frontend-backend communication.

Requirements

    Python 3.6+
    Flask
    requests
    flask_cors

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Install dependencies:

bash

    pip install -r requirements.txt

    Setup Google API Key: Replace the api_key in app.py with your actual Google Generative Language API key.

    Project Structure:
        Backend/: Contains app.py (Flask server code).
        Frontend/: Holds static files (index.html and styles.css).

Usage

    Run the Flask Server:

    bash

    python app.py

    Access the Application:
        Open a browser and navigate to http://localhost:5000 to load the frontend.
        To review code, use the /review endpoint by sending a POST request with JSON data that includes a code field.

API Endpoints

    GET /: Serves index.html.
    GET /styles.css: Serves styles.css for basic styling.
    POST /review: Accepts code for review and returns the API response.

Example Request

To test the /review endpoint, you can use curl or Postman:

bash

curl -X POST http://localhost:5000/review -H "Content-Type: application/json" -d '{"code": "print(\"Hello, world!\")"}'

Error Handling

The app returns a JSON object with an error message and a 500 status code in case of any request failure to the Google API.
