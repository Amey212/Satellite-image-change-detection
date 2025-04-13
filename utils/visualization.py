import matplotlib.pyplot as plt
import plotly.express as px

def plot_ndvi(image):
    """Plot NDVI analysis"""
    ndvi = calculate_ndvi(image)
    fig = px.imshow(ndvi, color_continuous_scale='YlGn', 
                   title="Vegetation Analysis (NDVI)")
    st.plotly_chart(fig)

def plot_false_color(image, bands):
    """Create false color composite"""
    false_color = image[:, :, bands]
    fig = px.imshow(false_color, title="False Color Composite")
    st.plotly_chart(fig)

def plot_change_map(change_map):
    """Visualize change detection results"""
    fig = px.imshow(change_map, binary_string=True,
                   title="Change Detection Map")
    st.plotly_chart(fig)