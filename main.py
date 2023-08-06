import streamlit as st
from PIL import Image
#from fpdf import FPDF
import base64

st.set_page_config(
    page_title="Digital Resume 👈",
    #page_icon="wave",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a portfolio webite!"
    }
)

st.image("Profile.png")
    
st.text("")

st.title("Hi, I'm Vighnesh Pawar :wave:")
st.text("")
st.text("")
st.text("")
st.text("")


tab1, tab2, tab3 = st.tabs(["Education", "About", "Resume"])
    
with tab1:
    st.header("Education")
    st.markdown(
"""
    - 2021-2023   |   Master’s Information Technology    |   Pillai College Of Arts, Commerce & Science, New Panvel   |    
    8.67 CGPA
    - 2018-2021   |   Bachelor’s Information Technology  |   Western College Of Commerce & Business Management   |   
    7.38 CGPA
    - 2016-2018   |   Tilak Education Society Vashi   |   HIGHER SECONDARY EDUCATION board   |   
    57.54%

    - JULY 2023 - Present   |   Coursera - Software Testing 
"""  
    )

with tab2:
    st.header("About")
    st.write("I've earned a master's degree in information technology, and I'm now searching for some valuable work experience to advance my software testing abilities. Like you, I enjoy working with others and giving back to the community.I'm entering the realm of software testing for the first time.The initial encounter is invaluable and unforgettable. I'll do every effort to succeed in my goals. The development of new talents, especially those related to problem solving, most interests me.") 
    st.markdown(
"""
    - Email ID : vighneshpawar@gmail.com
    - LinkedIn Profile : https://www.linkedin.com/in/vighnesh-pawar-31a4a5220
    - Location : Juinagar   |  Navi Mumbai
"""  
    )

with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.header("Resume Download")
            st.image("VIGHNESH PAWAR.jpg")
            def generate_pdf_content():
    # Replace this function with your code that generates the PDF content.
    # You can use any library (e.g., ReportLab, FPDF) to generate the PDF.
    # For the sake of this example, we'll just create a simple PDF content.
                content = "Download My Resume."
                return content

            def main():
            #st.title("Download Resume")

    # Create a download button
            #if st.button("Download Resume"):
                    pdf_content = generate_pdf_content()
        # Set the filename and content type for the download
                #filename = "DAMINI SHARMA.pdf"
                #mime_type = "application/pdf"
        # Use the st.download_button function to display the download button
                #st.download_button(label="Download Resume", data=pdf_content, file_name=filename, mime=mime_type)

        #if __name__ == "__main__":
            #main()
        
        

        # Assuming you have a PDF file named "example.pdf"
            file_path = "VIGHNESH PAWAR.pdf"

# Read the PDF file and get its content as bytes
            with open(file_path, "rb") as file:
                pdf_content = file.read()

# Provide the file name and content to st.file_download()
                st.download_button("Download Resume", pdf_content, mime="application/pdf")

