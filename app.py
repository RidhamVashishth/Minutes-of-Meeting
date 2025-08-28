import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PIL import Image

# --------------------🔐 Load and Configure API --------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# --------------------🎨 App Title --------------------
st.header(":blue[Minutes of Meeting] Generator 📜", divider="red")
st.markdown("Upload your handwritten MoMs (Minutes of Meeting) image. I’ll extract the to-dos and create a clean, structured table.")

# --------------------📤 Image Upload --------------------
uploaded_file = st.file_uploader("📎 Upload Handwritten MoM Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="📸 Uploaded Image Preview", use_container_width=True)

    # --------------------📝 Prompt for Gemini --------------------
    prompt = """
You are a highly intelligent assistant tasked with generating structured **Minutes of Meeting (MoM)** based on handwritten notes and to-do items extracted from an image.

Please perform the following tasks:
1. **OCR**: Read and transcribe the handwritten text.
2. **Task Extraction**: Identify individual tasks, to-dos, or action points.
3. **Deadline Detection**: Detect or infer any mentioned deadlines. If not mentioned, use “TBD”.
4. **Status Assignment**: Use context clues like “done”, checkmarks, etc. to mark status as:
   - ✅ Completed
   - 🕒 Pending
   - ⏳ Not Started
5. **% Completion**: Estimate the percentage completed (e.g., “in progress” → 50%).

📋 Format the output into a markdown table with these columns:
| Particulars (To-Dos) | Deadline | Status | % Completion |

Be accurate, concise, and clean in formatting.
"""

    # --------------------🧠 Generate Output --------------------
    with st.spinner("🔍 Extracting and analyzing the image..."):
        try:
            response = model.generate_content([img, prompt])
            st.success("✅ Extraction Completed")
            st.markdown("### 🗂️ Extracted Minutes of Meeting")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

else:
    st.info("📥 Please upload a handwritten MoM image to proceed.")
