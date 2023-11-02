import streamlit as st
import pandas as pd

st.set_page_config("Profile", "👤")

data = {
    'Liste': ['Reliable',
              'Tusted',
              'Steady',
              'Consistent',
              'Punctual',
              'Unflappable',
              'Efficent',
              'Productive',
              'Meticulous',
              'Attentive',
              'Persistent',
              'Enduring',
              'Indomitable',
              'Fortuitous',
              'Fatefel',
              'Serendipitous',
              'Adaptable',
              'Accommodating',
              'Resilient',
              'Genuine',
              'Others',
              ],

    'Koku': ['Alstroemeria',
             'Asparagus',
             'Aster',
             'Begonia',
             'Belladonna',
             'Calla Lily',
             'Camellia',
             'Carnation',
             'Dahlia',
             'Delphinium',
             'Fuchsia',
             'Gardenia',
             'Gladiolus',
             'Gypsophila',
             'Hydrangea',
             'Iris',
             'Jasmin',
             'Zinnia',
             'Anemone',
             'Chrysanthemum',
             'Purple',

             ]
}
df = pd.DataFrame(data)


st.dataframe(df, height=500, width=500)
