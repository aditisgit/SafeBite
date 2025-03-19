import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="SafeBite", layout="centered")
    
    # Title
    st.title("SafeBite: Detection of Food Contamination and Adulteration in Perishables")
    
    # Description
    st.write("""
    Welcome to SafeBite, a tool designed to help detect food contamination and adulteration in perishables. 
    Ensure food safety by checking contamination levels and predicting adulteration severity.
    """)
    
    # Display images of perishables
    col1, col2, col3 = st.columns(3)
    
    with col1:
        image1 = Image.open(r"SafeBite\UI\tomato.jpg")  # Add relevant image
        st.image(image1, caption="Fresh Fruits", use_container_width=True)
    with col2:
        image2 = Image.open(r"SafeBite\UI\burger.jpg")  # Add relevant image
        st.image(image2, caption="Vegetables", use_container_width=True)
    with col3:
        image3 = Image.open(r"SafeBite\UI\scientist.png")  # Add relevant image
        st.image(image3, caption="Dairy Products", use_container_width=True)
    
    # Main Buttons
    st.header("Food Safety Detection")
    tab1, tab2 = st.tabs(["Food Contamination", "Food Adulteration"])
    
    with tab1:
        st.subheader("Food Contamination")
        st.write("Analyze the degree of contamination in various food items.")
        
        if st.button("Predict Contaminant Level "):
            st.subheader("Enter Details")
            food_group = st.text_input("Food Group Name")
            country = st.text_input("Country Name")
            contaminant = st.text_input("Contaminant")
            year = st.text_input("Year")
            if st.button("Check Here"):
                st.write("Processing request...")  # Placeholder for backend integration
        
        
    
    with tab2:
        st.subheader("Food Adulteration")
        st.write("Detect potential adulterants in food products.")
        
        brand_name = st.text_input("Brand Name")
        product_name = st.text_input("Product Name")
        adulterant = st.selectbox("Select Adulterant", ["Chemical Additive", "Coloring Agent", "Preservative", "Other"])
        
        if st.button("Predict Severity"):
            st.write("Processing request...")  # Placeholder for backend integration

if __name__ == "__main__":
    main()
