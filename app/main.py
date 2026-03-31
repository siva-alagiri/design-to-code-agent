import streamlit as st
from PIL import Image
import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.tools.vision_tool import analyze_image
from app.tools.codegen_tool import generate_code

# Page config
st.set_page_config(
    page_title="Design to Code Agent",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 Design to Code Agent")
st.markdown("Upload a UI design image and get production-ready HTML/CSS code instantly.")
st.divider()

# Layout — two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Design")
    uploaded_file = st.file_uploader(
        "Upload a UI screenshot or design image",
        type=["png", "jpg", "jpeg", "webp"]
    )
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Design", use_column_width=True)

with col2:
    st.subheader("🔍 UI Analysis")
    
    if uploaded_file:
        if st.button("🚀 Generate Code", type="primary", use_container_width=True):
            
            # Step 1 - Analyze image
            with st.spinner("Analyzing your design..."):
                ui_description = analyze_image(image)
            
            st.success("✅ Design analyzed!")
            
            with st.expander("📋 View UI Description"):
                st.write(ui_description)
            
            # Step 2 - Generate code
            with st.spinner("Generating HTML/CSS ..."):
                html_code = generate_code(ui_description)
            
            st.success("✅ Code generated!")
            
            # Show code
            st.subheader("💻 Generated Code")
            st.code(html_code, language="html")
            
            # Download button
            st.download_button(
                label="⬇️ Download HTML File",
                data=html_code,
                file_name="generated_ui.html",
                mime="text/html"
            )
            
            # Live preview
            st.subheader("👁️ Live Preview")
            st.components.v1.html(html_code, height=500, scrolling=True)
    
    else:
        st.info("👈 Upload a design image to get started")