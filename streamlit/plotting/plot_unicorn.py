import streamlit as st
import pandas as pd
import plotly.express as px
# import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Unicorn Plotter',
    page_icon=':unicorn_face:',
    layout='wide'
)

@st.cache
def xls_to_df(xls_file):
    df = pd.read_excel(
        io=xls_file, 
        # engine='openpyxl',
        header=[2]
    )

    # drop extra l columns
    df.drop(list(df.filter(regex = 'l\.')), axis = 1, inplace = True)
    return df

st.title(':unicorn_face: :chart_with_upwards_trend:  Unicorn Plotter')

uploaded_xls = st.file_uploader(
    'Upload your xls file here:',
    type='xls',
    accept_multiple_files=False
)

if uploaded_xls is not None:
    # df = xls_to_df('input/PP-PGM2-22-164-Chromatogram.xls')
    df = xls_to_df(uploaded_xls)

    st.sidebar.header('Please filter here:')
    unicorn_out = st.sidebar.multiselect(
        'Select the data to plot:',
        options = df.columns,
        default = df.columns[1]
    )

    line_chart = px.line(
        df,
        x='l',
        y=unicorn_out
    )

    st.plotly_chart(line_chart)

# st.dataframe(df)

# print(df.info())




# print(df.columns)
# df.plot.line(x='l', y=' mS/cm')
# plt.show()


