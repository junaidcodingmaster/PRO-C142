# PRO-C142: FLASK MOCKUP - 2

This is a simple Flask application that recommends articles using a CSV file containing article data. Users can retrieve articles, mark them as liked or not liked, and get the next recommended article.

_Note_ : It a new version.

## Prerequisites

- Python 3.8 or higher
- Flask
- Requests

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/junaidcodingmaster/PRO-C142
   cd PRO-142
   ```

2. Create and activate a new virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open another terminal and run the test script:

   ```bash
   python demo.py
   ```

   The test script will send requests to the Flask app to retrieve and interact with the articles.

## API Endpoints

### Get Article

- **Endpoint**: `/get_article`
- **Method**: GET
- **Description**: Retrieves the first article from the list of available articles.
- **Response**: JSON object representing the article or a message if no articles are remaining.

### Like Article

- **Endpoint**: `/like_article`
- **Method**: POST
- **Description**: Marks the current article as liked and moves to the next recommended article.
- **Response**: JSON object with a success message or a message if no articles are remaining.

### Not Like Article

- **Endpoint**: `/not_like_article`
- **Method**: POST
- **Description**: Marks the current article as not liked and moves to the next recommended article.
- **Response**: JSON object with a success message or a message if no articles are remaining.

## Example Usage

You can use tools like Postman to test the API endpoints. Alternatively, you can run the provided `demo.py` script, which sends requests to the Flask app.

```python
import requests

base_url = "http://127.0.0.1:5000"  # Replace with the appropriate base URL of your Flask app

# Test the GET request to get the first article
response = requests.get(f"{base_url}/get_article")
print(response.json())  # Print the response JSON

# Test the POST request to mark the article as liked
response = requests.post(f"{base_url}/like_article")
print(response.json())  # Print the response JSON

# Test the POST request to mark the article as not liked
response = requests.post(f"{base_url}/not_like_article")
print(response.json())  # Print the response JSON

# Test the GET request again to see the updated article
response = requests.get(f"{base_url}/get_article")
print(response.json())  # Print the response JSON
```

## Author

Created by [Junaid](https://abujuni.dev).
