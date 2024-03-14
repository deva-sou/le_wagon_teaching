import streamlit as st
import pandas as pd
import geopandas
from shapely.geometry import Polygon


def main():
    st.title("My Streamlit App")

    # Add your content here
    st.write("Welcome to my Streamlit app!")

    """
    # My first app
    Here's our first attempt at using data to create a table:
    """
    df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

    df
    p1 = Polygon([(0, 0), (1, 0), (1, 1)])
    p2 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
    p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
    g = geopandas.GeoSeries([p1, p2, p3])
    g.plot()


if __name__ == "__main__":
    main()
