# 📧 Recruiter Outreach Generator

> A Streamlit web app that generates AI-powered, personalized recruiter emails — supporting initial outreach, follow-ups, and thank-you messages with optional live email dispatch.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Repo](https://img.shields.io/badge/GitHub-recruiter--outreach--generator-181717?logo=github)](https://github.com/jyotidabass/recruiter-outreach-generator)

---

## 📌 Overview

**Recruiter Outreach Generator** is a lightweight Streamlit frontend that connects to an AI-powered backend API (hosted on Hugging Face Spaces) to generate personalized recruiter emails. Recruiters fill in candidate and role details, choose a message type, and instantly get a ready-to-send email — complete with subject line and body.

Key highlights:
- Zero ML setup — the AI runs on a hosted backend
- Three message modes: cold outreach, follow-up, and thank-you
- Preview mode by default; optionally dispatch the email live
- Context-aware follow-ups using past conversation history
- Full JSON API response visible in-app for debugging

---

## ✨ Features

| Feature | Details |
|---|---|
| 🤖 AI-generated emails | Powered by `ak0601-outreach-api` on Hugging Face Spaces |
| 📨 3 message types | `outreach`, `follow_up`, `thank_you` |
| 📬 Optional email sending | Check a box to dispatch email immediately |
| 🧵 Conversation context | Include prior messages for smarter follow-ups |
| 📝 Job evaluation input | Add role notes to improve message relevance |
| 🔍 Full API response view | Expandable JSON panel for transparency |
| ✅ Client-side validation | Highlights missing required fields before submission |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/jyotidabass/recruiter-outreach-generator.git
cd recruiter-outreach-generator

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run streamlit_app.py
```

The app opens at **http://localhost:8501** in your browser.

---

## 🖥️ Usage

Fill in the form and click **Generate Message**. The app validates inputs, calls the API, and displays the generated subject line and email body.

### Required Fields

| Field | Description |
|---|---|
| `sender_email` | Recruiter's email address |
| `recipient_email` | Candidate's email address |
| `candidate_name` | Full name of the candidate |
| `current_role` | Candidate's current job title |
| `current_company` | Candidate's current employer |
| `company_name` | Company the recruiter is hiring for |
| `role` | Target role being offered |
| `recruiter_name` | Name of the recruiter |
| `organisation` | Recruiter's organisation or department |
| `message_type` | One of: `outreach` · `follow_up` · `thank_you` |

### Optional Fields

| Field | Description |
|---|---|
| `job_evaluation` | Additional context about the role or candidate fit |
| `reply_to_email` | Alternative reply-to address |
| `send_email` | If checked, dispatches the email immediately |
| `past_conversation` | Prior message history for context-aware follow-ups |

### Output

After a successful API call, the app displays:
- ✅ **Success status**
- 📧 **Email subject line**
- 💬 **Generated message body** (editable text area)
- 📬 **Email sent status** — Preview Mode or Sent confirmation
- 📋 **Full JSON response** in a collapsible panel

---

## 🔌 API Reference

The app calls a hosted REST API on Hugging Face Spaces:

```
POST https://ak0601-outreach-api.hf.space/generate-message
```

**Authentication:** `X-API-Key` header  
**Content-Type:** Parameters sent as query string

### Example Request

```python
import requests

response = requests.post(
    "https://ak0601-outreach-api.hf.space/generate-message",
    params={
        "sender_email": "jane@company.com",
        "recipient_email": "john@example.com",
        "candidate_name": "John Doe",
        "current_role": "Software Engineer",
        "current_company": "Tech Corp",
        "company_name": "Target Corp",
        "role": "Senior Software Engineer",
        "recruiter_name": "Jane Smith",
        "organisation": "HR Department",
        "message_type": "outreach"
    },
    headers={
        "accept": "application/json",
        "X-API-Key": "YOUR_API_KEY"
    }
)

print(response.json())
```

### Response Schema

```json
{
  "success": true,
  "email_subject": "Exciting Opportunity at Target Corp",
  "message": "Hi John, ...",
  "email_sent": false,
  "error": null
}
```

---

## 📁 Project Structure

```
recruiter-outreach-generator/
├── streamlit_app.py      # Main Streamlit application
├── requirements.txt      # Python dependencies
└── README.md
```

---

## 📦 Dependencies

```
streamlit    # Web UI framework
requests     # HTTP client for API communication
```

Install with:
```bash
pip install -r requirements.txt
```

---

## ⚙️ How It Works

```
User fills form
      │
      ▼
Client-side validation (required fields check)
      │
      ▼
POST request → https://ak0601-outreach-api.hf.space/generate-message
      │         (with candidate + role + message_type params)
      ▼
AI backend generates personalized email
      │
      ▼
App displays subject, body, send status + full JSON
      │
      ▼ (if send_email = true)
Email dispatched to recipient_email
```

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch — `git checkout -b feature/your-feature`
3. Commit your changes — `git commit -m "Add your feature"`
4. Push to the branch — `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🔗 Links

- 🐙 **GitHub:** [jyotidabass/recruiter-outreach-generator](https://github.com/jyotidabass/recruiter-outreach-generator)
- 🤗 **API Backend:** [ak0601-outreach-api on Hugging Face Spaces](https://ak0601-outreach-api.hf.space)
