# Python PDF Merger API

Flask API that merges a list of PDF files into one

### Setup

1. Clone the repository
2. Install dependencies with `pip install -r requirements.txt`
3. Run the server with `python main.py`

### Endpoints

- `GET /` - Shows the form to upload PDF files
- `POST /merge` - Merges a list of PDF files into one
- `GET /clear` - Clears the PDF files directory
