# Domain-Specific-Transformer-FineTuning

# NFL Scouting Report Generator

## Overview

This project is a web-based application that allows users to generate NFL scouting reports based on player attributes using a GPT-2 model. It consists of a frontend built with Streamlit and a backend implemented with Flask and Hugging Face's Transformers library.

## Features

- User-friendly interface to input player attributes
- Backend API to process the request and generate a scouting report
- GPT-2 model for text generation
- Error handling for API requests

## Technologies Used

- **Python**
- **Streamlit** (Frontend UI)
- **Flask** (Backend API)
- **Requests** (API calls)
- **Transformers (Hugging Face)** (Text generation with GPT-2)

## Installation & Setup

### Prerequisites

Make sure you have Python installed (>=3.8 recommended). You will also need to install the required dependencies.

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/nfl-scouting-report.git
   cd nfl-scouting-report
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask backend:

   ```bash
   python backend.py
   ```

4. Run the Streamlit frontend:

   ```bash
   streamlit run frontend.py
   ```

## Usage

- Enter player attributes in the provided text box.
- Click the "Generate Report" button.
- View the generated scouting report.

## API Endpoint

**POST /generate**

- Request: `{ "player_data": "string" }`
- Response: `{ "Generated NFL Scouting Report": "string" }`

- <img width="1728" alt="Image" src="https://github.com/user-attachments/assets/a13b8ab9-31f1-4875-8424-c8b6c168a578" />

