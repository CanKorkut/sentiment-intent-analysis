# 🧠 Sentiment & Intent Analysis

This repository contains the implementation of a **Sentiment and Intent Analysis** system, designed to analyze conversations in real-time. The system uses Natural Language Processing (NLP) techniques to detect the sentiment (positive, neutral, or negative) and intent (such as inquiry, purchase intent, complaint, etc.) behind user messages.

## 📌 Project Overview

This project includes several services:

- **API for Sentiment & Intent Prediction**: A FastAPI-based server that accepts text input and returns sentiment and intent predictions.
- **Streamlit UI**: A web-based user interface to upload conversation data (in JSON format) and visualize sentiment and intent analysis.
- **Logging Service**: A FastAPI service to log the results of the sentiment and intent analysis into a MongoDB database.
  
![demo](https://github.com/user-attachments/assets/02e3f74e-2658-43bd-b422-72fb9b6146fc)

## Features

- **Sentiment Analysis**: Classifies messages into three categories: positive, neutral, or negative.
- **Intent Classification**: Predicts the intent of the message (e.g., inquiry, greeting, purchase intent, etc.).
- **Real-Time Analysis**: Supports analyzing customer and sales representative conversations in real-time.
- **Visualization**: A user-friendly interface to upload and display analyzed results, including a summary table.

## Installation

To run this project locally, follow these steps:

### ⚙️ Prerequisites

Setting the [GROQ](https://groq.com/) API Key
This application requires a valid GROQ_API_KEY to be set as an environment variable. Here's how you can set it:

```bash
set GROQ_API_KEY=your_api_key_here

```
Make sure you have the following installed:

- Python 3.9+
- MongoDB
- Anaconda

### 🚀 Setup
0. Create Conda Env:
   
```bash
conda create -n myenv python=3.10
conda activate myenv
```
1. Clone the repository:

```bash
git clone https://github.com/CanKorkut/sentiment-intent-analysis.git
cd sentiment-intent-analysis
```
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up MongoDB:

```bash
docker pull mongo
docker run --name mongo-container -d -p 27017:27017 mongo
```

5. Start the Sentiment & Intent API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

5. Start the Logging Service:
```bash
cd log_service
uvicorn log_service:log_app --host 0.0.0.0 --port 8001 --reload
```

6. Start the Streamlit UI:
```bash
cd ui
streamlit run app.py
```
This will start the web interface at http://localhost:8501.

## ▶️ Usage
1. Upload a JSON file containing a list of sentences for analysis.
2. The application will predict the sentiment and intent of each sentence in real-time.
3. Results will be displayed with color-coded sentiment (positive, neutral, negative) and the predicted intent.

JSON file must be in this structure:

```bash
{
  "sentences": [
    "SENTENCE1",
    "SENTENCE2"
  ]
}
```

## 📁 Folder Structure
Here is an overview of the folder structure:

```bash
sentiment-intent-analysis/
│
├── main.py                # FastAPI server for sentiment and intent analysis
├── ui                     # Streamlit UI for uploading files and displaying results
    ├── ui.py
├── log_service
    ├── log_server.py      # FastAPI service for logging the analysis results
    ├── log_db.py          # MongoDB service to save logs
├── services/              # Sentiment and intent analysis services
│   ├── sentiment.py       # Sentiment analysis service
│   └── intent.py          # Intent classification service
├── requirements.txt       # Python dependencies
├── test.json              # test file example
└── README.md              # Project documentation
```

# DB LOG Example
![image](https://github.com/user-attachments/assets/0c200ff8-68ee-4a1d-8b15-dfdf9267a98a)
