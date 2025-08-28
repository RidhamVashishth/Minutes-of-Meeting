Meeting Notes Analyzer & Summary Generator
A web application that leverages the google-gemini-2.0 flash model to extract, analyze, and structure handwritten meeting notes from an uploaded image into a clean, organized markdown table.

Live Application
You can access the deployed application here: https://minutesofmeeting.streamlit.app/

Overview
This tool is designed to streamline the process of digitizing and organizing action items from meetings. Users can upload an image of their handwritten notes, and the application will use multimodal AI to perform Optical Character Recognition (OCR) and intelligently identify tasks, deadlines, and their current status. The final output is a professional and easy-to-read table summarizing all key to-dos.

Features
Image Upload: Supports common image formats (JPG, JPEG, PNG) for handwritten notes.

AI-Powered Text Extraction: Utilizes the google-gemini-2.0 flash model to accurately transcribe text from images.

Structured Data Output: Intelligently parses the transcribed text to identify action items, deadlines, and completion status.

Clean User Interface: Built with Streamlit for a simple and intuitive user experience.

Technology Stack
Language: Python

Framework: Streamlit

AI Model: google-gemini-2.0 flash

Libraries: google-generativeai, python-dotenv, Pillow

Local Setup and Installation
To run this project on your local machine, please follow these steps.

Prerequisites
Python 3.8 or higher

A Google API Key with the Generative Language API enabled. You can obtain one from Google AI Studio.
