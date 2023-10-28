import pandas as pd
import streamlit as st

data = st.sidebar.file_uploader("Upload your file", type=["xlsx"])
if data is not None:
    df = pd.read_excel(data, engine="openpyxl", index_col=None)
    df1 = pd.DataFrame(df)
    pd.DataFrame.reset_index(df1, drop=True, inplace=True)

    options = st.multiselect(
        "Which fields do you want to display?",
        [
            "RowID",
            "Email Address",
            "Date",
        ],
    )
    if options == []:
        st.write("No fields selected")
        df2 = df1
    else:
        st.write("You selected:", options)
        df2 = df1[options]

    df2 = df2.style.format(precision=0)
    edited_df = st.experimental_data_editor(df2)

    if st.button("Update"):
        edited_df.to_excel("testfile.xlsx")
        st.write("Update the new file")

    st.write(pd.read_excel("testfile.xlsx", engine="openpyxl", index_col=None))
