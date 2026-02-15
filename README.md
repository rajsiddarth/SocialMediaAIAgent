[![Binder](https://mybinder.org/badge_logo.svg)](
https://mybinder.org/v2/gh/rajsiddarth/SocialMediaAIAgent/HEAD?filepath=Social%20media%20customer%20agent.ipynb
)


Social Media Customer Agent 🤖

An AI-powered customer support agent designed to simulate and respond to social media user posts.
This project demonstrates structured outputs, user simulation, and response parsing using the OpenAI Responses API.

📌 Overview

This notebook showcases how to:

Simulate a social media user

Generate AI-driven responses to user posts

Parse structured model outputs into typed Python objects

Work with the OpenAI Responses API using responses.parse()

The goal is to model a customer support or engagement agent that can be extended to real-world social media workflows.

## Run with a UI (Streamlit)

You can publish this project with a simple web UI using Streamlit.

### 1) Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Set your API key before starting:

```bash
export OPENAI_API_KEY="your_key_here"
```

### 2) Publish on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to https://share.streamlit.io and create a new app.
3. Select this repo and set the main file path to `app.py`.
4. In app settings, add `OPENAI_API_KEY` in **Secrets**.
5. Deploy.

### 3) Alternative hosting options

- **Render**: create a new Web Service, use `pip install -r requirements.txt` as build command and `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` as start command.
- **Hugging Face Spaces (Streamlit SDK)**: upload this repo and set the secret `OPENAI_API_KEY`.
