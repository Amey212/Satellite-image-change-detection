import streamlit as st
from utils.data_processor import load_and_process_image
from utils.change_detection import detect_changes
from utils.visualization import plot_ndvi, plot_false_color, plot_change_map
from utils.classification_model import classify_changes

st.set_page_config(page_title="Satellite Change Detection", layout="wide")

def main():
    st.title("Satellite Imagery Change Detection and Analysis")
    
    # File upload
    col1, col2 = st.columns(2)
    with col1:
        img1 = st.file_uploader("Upload earlier satellite image", type=["tif", "png", "jpg"])
    with col2:
        img2 = st.file_uploader("Upload recent satellite image", type=["tif", "png", "jpg"])
    
    if img1 and img2:
        # Process images
        with st.spinner('Processing images...'):
            img1_processed = load_and_process_image(img1)
            img2_processed = load_and_process_image(img2)
            
            # Change detection
            change_map = detect_changes(img1_processed, img2_processed)
            
            # Classification
            classified_changes = classify_changes(change_map)
            
            # Visualization
            st.subheader("Change Detection Results")
            tab1, tab2, tab3 = st.tabs(["Change Map", "Classification Results", "Spectral Analysis"])
            
            with tab1:
                plot_change_map(change_map)
            
            with tab2:
                st.image(classified_changes, caption="Classified Changes")
            
            with tab3:
                band_combo = st.selectbox("Select band combination", 
                                        ["Natural Color", "False Color", "Vegetation Analysis"])
                if band_combo == "Natural Color":
                    plot_false_color(img2_processed, [3,2,1])
                elif band_combo == "False Color":
                    plot_false_color(img2_processed, [4,3,2])
                else:
                    plot_ndvi(img2_processed)

if __name__ == "__main__":
    main()