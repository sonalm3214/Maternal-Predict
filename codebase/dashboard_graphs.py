import streamlit as st
import pandas as pd
import plotly.express as px
from io import StringIO
import requests

BUBBLE_CHART_INFO = """
The Bubble Chart provides a visual representation of how well different regions have performed in achieving institutional deliveries compared to their assessed needs. It visualizes maternal health data, particularly focusing on the achievement of institutional deliveries in different states or union territories during the period of April to June for the year 2019-20.

### Chart Breakdown:

1.  **X-axis (Need Assessed):**
    This axis represents the assessed needs for maternal health in different regions.

2.  **Y-axis (Achievement):**
    This axis represents the actual number of institutional deliveries during the specified period.

3.  **Bubble Size (% Achievement):**
    The size of each bubble is determined by the percentage achievement of the assessed needs (`% Achvt = (Achievement / Need) * 100`). Larger bubbles indicate better performance.

4.  **Color (State/UT):**
    Each bubble is color-coded by the state or union territory it represents.

5.  **Hover Name (State/UT):**
    Hovering over a bubble reveals the name of the state or union territory.
"""

PIE_CHART_INFO = """
This chart visualizes the proportion of institutional deliveries across different states/union territories (UTs) during the specified period (April to June 2019-20).

### Key Components:

*   **Slices of the Pie:**
    Each slice of the pie represents a specific state or UT.

*   **Size of Slices:**
    The size of each slice corresponds to the proportion of institutional deliveries achieved by that state or UT.

*   **Hover Information:**
    Hovering over a slice provides the name of the state/UT and the exact number of institutional deliveries.
"""

def _clean_column_names(df):
    """Cleans up long column names for easier use."""
    df.columns = [col.strip() for col in df.columns]
    df = df.rename(columns={
        "Need Assessed (2019-20) - (A)": "Need Assessed",
        "Achievement during April to June - Total Institutional Deliveries - (2019-20) - (B)": "Achievement",
        "% Achvt of need assessed (2019-20) - (E=(B/A)*100)": "% Achievement"
    })
    return df

@st.cache_data(ttl=3600) # Cache data for 1 hour
def fetch_data_from_api(api_endpoint):
    """Fetches and cleans data from the API, with caching."""
    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = pd.read_csv(StringIO(response.text))
        data = _clean_column_names(data)
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error during API request: {e}")
        return None
    except Exception as e:
        st.error(f"An error occurred while processing the data: {e}")
        return None

class MaternalHealthDashboard:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint
        self.maternal_health_data = fetch_data_from_api(api_endpoint)

    def drop_all_india(self, df):
        return df[df["State/UT"] != "All India"]

    def create_bubble_chart(self):
        if self.maternal_health_data is None:
            return
        st.subheader("Bubble Chart: Need Assessed vs Achievement")
        df = self.drop_all_india(self.maternal_health_data)

        fig = px.scatter(
            df,
            x="Need Assessed",
            y="Achievement",
            size="% Achievement",
            color="State/UT",
            hover_name="State/UT",
            title="Bubble Chart: Need Assessed vs Achievement"
        )
        st.plotly_chart(fig)

    def create_pie_chart(self):
        if self.maternal_health_data is None:
            return
        st.subheader("Proportion of Institutional Deliveries by State/UT")
        df = self.drop_all_india(self.maternal_health_data)

        fig = px.pie(
            df,
            names="State/UT",
            values="Achievement",
            title="Proportion of Institutional Deliveries by State/UT"
        )
        st.plotly_chart(fig)

    def get_bubble_chart_data(self):
        return BUBBLE_CHART_INFO
    def get_pie_graph_data(self):
        return PIE_CHART_INFO


if __name__ == "__main__":
    api_key = "579b464db66ec23bdd00000139b0d95a6ee4441c5f37eeae13f3a0b2"
    api_endpoint = f"https://api.data.gov.in/resource/6d6a373a-4529-43e0-9cff-f39aa8aa5957?api-key={api_key}&format=csv"
    dashboard = MaternalHealthDashboard(api_endpoint)

    if dashboard.maternal_health_data is not None:
        dashboard.create_bubble_chart()
        dashboard.create_pie_chart()