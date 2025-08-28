import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import streamlit as st
import traceback

# Load environment variables from .env file
load_dotenv()

# Use the correct key name from your .env file
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Corrected variable assignment with '='
model = genai.GenerativeModel('gemini-2.0-flash') # Using gemini-pro-vision as it's standard for image inputs

# Creating the Header
st.header(":blue[Meeting Notes Analyzer and Summary] Generator 📜", divider="red")
st.markdown("Upload your handwritten Meeting Notes image. I’ll extract the to-dos and create a clean, structured table.")
uploaded_file = st.file_uploader('Upload Your Image', type=['jpg', 'jpeg', 'png'])

# Corrected variable name 'uploaded_file'
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded MoM Image", use_container_width=True) # Changed use_container_width to use_column_width for better compatibility
    
    prompt = '''You are an intelligent assistant tasked with generating structured Meeting notes and summary based on handwritten notes and to-dos provided as images. Your job is to extract text from the images and organize the information into a clean, professional table with the following columns:
| Particulars (To-Dos) | Deadline | Status (Completed / Pending / Not Started) | % Completion |
Requirements:
OCR: Accurately read and transcribe handwritten text from the uploaded images.
Task Identification: Identify individual to-do items, action points, or tasks from the transcribed text.
Deadline Detection: Detect any mentioned dates or inferred deadlines related to each task. If no deadline is present, leave the field blank or mark as “TBD.”
Status Assignment: Based on context (e.g., checkmarks, strikethroughs, annotations like "done", "in progress", "to-do", etc.), assign a task status:
✅ Completed
🕒 Pending
⏳ Not Started
Completion %: Estimate a percentage completion (e.g., 0%, 50%, 100%) based on the language or markings (e.g., “half done”, “in progress”, “✓✓✓”, etc.).

📋 Format the output into a markdown table with these columns:
| Particulars (To-Dos) | Deadline | Status | % Completion |

Be accurate, concise, and clean in formatting.
'''

    with st.spinner('Extracting and Analysing the Image...'):
        try:
            response = model.generate_content([prompt, img]) # Swapped order for convention, prompt first
            st.success("✅ Extraction Completed")
            st.markdown("### 🗂️ Extracted Minutes of Meeting")
            st.markdown(response.text)
        except Exception as e:
            print("‼️ An error occurred during the API call.")
            traceback.print_exc() # This prints the full error traceback to the terminal
            st.error(f"❌ An error occurred: {e}")

else:
    st.info("📥 Please upload a handwritten MoM image to proceed.")
