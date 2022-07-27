import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# markdown = """
# Web App URL: <https://template.streamlitapp.com>
# GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
# """
# st.sidebar.title("About")
# st.sidebar.info(markdown)
# logo = "https://i.imgur.com/UbOXYAU.png"
# st.sidebar.image(logo)

# Customize page title
st.title("Vegetation Changes in Kalimantan Island with MODIS Satellite Imagery")

st.markdown(
    """
    Kalimantan Island is one of Indonesia's islands famous for its forest's vast and abundant natural resources. Many of the produce of the land are exported abroad, especially from the mining and forestry sectors. The existence of mining activities and forest use causes changes in the types of land cover and forest degradation. Therefore, vegetation data is needed to monitor forest degradation.

The existence of vegetation is vital and has many benefits, such as producing air, controlling climate, animal habitat, and so on. The presence of vegetation provides a sizeable positive impact on an area. Balance
the ecosystem will be maintained, such as carbon dioxide and oxygen balance, regulation of groundwater management, improvement of soil physical, chemical, and biological properties, and so on.

Therefore, this website application was made to monitor vegetation changes from year to year on the island of Kalimantan using satellite image data. Based on [W.J.D. van Leeuwen, 1996](https://www.sciencedirect.com/science/article/abs/pii/0034425795001980)
    """
)

# st.header("Instructions")

# markdown = """
# 1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
# 2. Customize the sidebar by changing the sidebar text and logo in each Python files.
# 3. Find your favorite emoji from https://emojipedia.org.
# 4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

# """

# st.markdown(markdown)

#m = leafmap.Map(minimap_control=True)
#m.add_basemap("OpenTopoMap")
#m.to_streamlit(height=500)
