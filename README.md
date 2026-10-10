AgentShield AI – Prompt Injection Firewall

ET AI Hackathon: Agentic Edition

Problem Statement 2 – Agentic Cybersecurity: Prompt Injection Firewall

Project Overview

AgentShield AI is a prototype security firewall designed to identify and prevent suspicious prompt-injection instructions from reaching an AI application.

It combines a rule-based detection engine, Gemini AI analysis, and a deterministic security policy engine.

Key Features

Rule-based suspicious instruction detection

Gemini-powered contextual security analysis

Model retry and fallback handling

ALLOW, BLOCK, and REVIEW policy decisions

Support for text prompts and UTF-8 TXT/Markdown uploads

Streamlit security dashboard

Session-level scan history

Automated backend tests

Technology Stack

Python 3.11

FastAPI

Streamlit

Google Gemini API

Pydantic

Pytest

Architecture

User Input → FastAPI → Rule-Based Detector → Gemini AI Analyzer → Policy Engine → Security Decision

The orchestrator coordinates the inspection stages. The current implementation is a hybrid AI security prototype, not a fully autonomous Google ADK agent.

Local Setup

Create a Python virtual environment.

Install dependencies using pip install -r requirements.txt.

Set GEMINI_API_KEY and GEMINI_MODEL in .env.

Start the backend using python -m uvicorn backend.main:app --reload.

Start the frontend using python -m streamlit run frontend/app.py.

Open http://localhost:8501.

Security Behavior

ALLOW: The analyzers found no identified threat, and the AI assessment is low-risk.

BLOCK: The policy engine identifies a prompt-injection threat.

REVIEW: Analysis is inconclusive or the AI service is unavailable.

Testing

Run python -m pytest -q.

The current automated suite contains six passing tests as of the latest local test run.

Limitations

This is a hackathon research prototype, not a production security solution. It may fail to detect previously unseen attacks, and model decisions can contain false positives or false negatives. Additional adversarial testing, source-aware validation, tool-call enforcement, and audit logging would be needed for production use.