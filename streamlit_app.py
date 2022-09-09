from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.set_page_config(
     page_title="This is Lit!",
     page_icon=":whale:",
     layout="centered",
     initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "# This is lit!"
     }
 )

"""
# Welcome to This Is Lit!
"""

with st.sidebar:
     st.radio('Select one:', ["default", "strange"])

total_points = st.slider("Number of points in spiral", 1, 2000, 10)
num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

Point = namedtuple('Point', 'x y')
data = []

points_per_turn = total_points / num_turns


for curr_point_num in range(total_points):
    curr_turn, i = divmod(curr_point_num, points_per_turn)
    angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    radius = curr_point_num / total_points
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    data.append(Point(x, y))

st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
