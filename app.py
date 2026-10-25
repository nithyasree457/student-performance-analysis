# ============================================================
# STUDENT PERFORMANCE ANALYSIS
# Data Analysis and Interactive Dashboard
# ============================================================


# ------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 2. PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)


# ------------------------------------------------------------
# 3. DASHBOARD TITLE
# ------------------------------------------------------------

st.title("Student Performance Analytics")

st.write(
    "Analyze student academic performance "
    "and explore meaningful insights."
)


st.divider()


# ------------------------------------------------------------
# 4. LOAD DATASET
# ------------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/StudentsPerformance.csv"
    )

    return df


df = load_data()


# ------------------------------------------------------------
# 5. DATASET OVERVIEW
# ------------------------------------------------------------

total_dataset_students = df.shape[0]

total_columns = df.shape[1]


# ------------------------------------------------------------
# 6. GENDER FILTER
# ------------------------------------------------------------

st.sidebar.header("Dashboard Filters")


gender_option = st.sidebar.selectbox(
    "Select Gender",
    ["All", "Female", "Male"]
)


# ------------------------------------------------------------
# 7. TEST PREPARATION FILTER
# ------------------------------------------------------------

preparation_option = st.sidebar.selectbox(
    "Select Test Preparation",
    ["All", "Completed", "Not Completed"]
)


# ------------------------------------------------------------
# 8. APPLY GENDER FILTER
# ------------------------------------------------------------

if gender_option == "Female":

    filtered_df = df[
        df["gender"] == "female"
    ]


elif gender_option == "Male":

    filtered_df = df[
        df["gender"] == "male"
    ]


else:

    filtered_df = df.copy()


# ------------------------------------------------------------
# 9. APPLY TEST PREPARATION FILTER
# ------------------------------------------------------------

if preparation_option == "Completed":

    filtered_df = filtered_df[
        filtered_df["test preparation course"] == "completed"
    ]


elif preparation_option == "Not Completed":

    filtered_df = filtered_df[
        filtered_df["test preparation course"] == "none"
    ]


# ------------------------------------------------------------
# 10. CALCULATE FILTERED DATASET VALUES
# ------------------------------------------------------------

total_students = filtered_df.shape[0]


math_average = filtered_df["math score"].mean()


reading_average = filtered_df["reading score"].mean()


writing_average = filtered_df["writing score"].mean()


overall_average = filtered_df[
    ["math score", "reading score", "writing score"]
].mean().mean()


# ------------------------------------------------------------
# 11. STUDENT PERFORMANCE OVERVIEW
# ------------------------------------------------------------

st.header("Student Performance Overview")


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Students",
    total_students
)


col2.metric(
    "Math Average",
    f"{math_average:.2f}"
)


col3.metric(
    "Reading Average",
    f"{reading_average:.2f}"
)


col4.metric(
    "Writing Average",
    f"{writing_average:.2f}"
)


st.divider()


# ------------------------------------------------------------
# 12. OVERALL SUBJECT PERFORMANCE
# ------------------------------------------------------------

st.header("Overall Subject Performance")


subject_average = pd.DataFrame({

    "Subject": [
        "Mathematics",
        "Reading",
        "Writing"
    ],

    "Average Score": [
        math_average,
        reading_average,
        writing_average
    ]

})


fig1, ax1 = plt.subplots()


ax1.bar(
    subject_average["Subject"],
    subject_average["Average Score"]
)


ax1.set_title(
    "Average Student Performance by Subject"
)


ax1.set_xlabel(
    "Subject"
)


ax1.set_ylabel(
    "Average Score"
)


ax1.set_ylim(
    0,
    100
)


ax1.grid(
    axis="y",
    alpha=0.3
)


st.pyplot(
    fig1,
    use_container_width=True
)


st.divider()


# ------------------------------------------------------------
# 13. GENDER PERFORMANCE COMPARISON
# ------------------------------------------------------------

st.header("Gender Performance Comparison")


gender_average = df.groupby(
    "gender"
)[
    ["math score", "reading score", "writing score"]
].mean()


gender_average = gender_average.rename(
    columns={
        "math score": "Mathematics",
        "reading score": "Reading",
        "writing score": "Writing"
    }
)


fig2, ax2 = plt.subplots()


gender_average.plot(
    kind="bar",
    ax=ax2
)


ax2.set_title(
    "Average Performance by Gender"
)


ax2.set_xlabel(
    "Gender"
)


ax2.set_ylabel(
    "Average Score"
)


ax2.set_ylim(
    0,
    100
)


ax2.grid(
    axis="y",
    alpha=0.3
)


ax2.legend(
    title="Subjects"
)


st.pyplot(
    fig2,
    use_container_width=True
)


st.divider()


# ------------------------------------------------------------
# 14. TEST PREPARATION ANALYSIS
# ------------------------------------------------------------

st.header("Test Preparation Analysis")


preparation_average = df.groupby(
    "test preparation course"
)[
    ["math score", "reading score", "writing score"]
].mean()


preparation_average = preparation_average.rename(
    columns={
        "math score": "Mathematics",
        "reading score": "Reading",
        "writing score": "Writing"
    }
)


fig3, ax3 = plt.subplots()


preparation_average.plot(
    kind="bar",
    ax=ax3
)


ax3.set_title(
    "Performance Based on Test Preparation"
)


ax3.set_xlabel(
    "Test Preparation Course"
)


ax3.set_ylabel(
    "Average Score"
)


ax3.set_ylim(
    0,
    100
)


ax3.grid(
    axis="y",
    alpha=0.3
)


ax3.legend(
    title="Subjects"
)


st.pyplot(
    fig3,
    use_container_width=True
)


st.subheader(
    "Average Scores by Test Preparation"
)


st.dataframe(
    preparation_average.round(2),
    use_container_width=True
)


st.divider()


# ------------------------------------------------------------
# 15. STUDENT PERFORMANCE INSIGHTS
# ------------------------------------------------------------

st.header("Student Performance Insights")


if total_students > 0:

    highest_subject = subject_average.loc[
        subject_average["Average Score"].idxmax(),
        "Subject"
    ]


    lowest_subject = subject_average.loc[
        subject_average["Average Score"].idxmin(),
        "Subject"
    ]


    highest_average = subject_average[
        "Average Score"
    ].max()


    lowest_average = subject_average[
        "Average Score"
    ].min()


    st.info(
        f"Highest average performance is in "
        f"{highest_subject} with "
        f"{highest_average:.2f} marks."
    )


    st.info(
        f"Lowest average performance is in "
        f"{lowest_subject} with "
        f"{lowest_average:.2f} marks."
    )


    st.write(
        f"Overall average score across the three "
        f"subjects is {overall_average:.2f}."
    )


    math_below_50 = filtered_df[
        filtered_df["math score"] < 50
    ].shape[0]


    st.warning(
        f"{math_below_50} students in the selected "
        f"dataset scored below 50 in Mathematics."
    )


else:

    st.warning(
        "No students match the selected filters."
    )


st.divider()


# ------------------------------------------------------------
# 16. STUDENT DATASET
# ------------------------------------------------------------

st.header("Student Dataset")


st.write(
    f"Displaying {total_students} students "
    "based on the selected filters."
)


st.dataframe(
    filtered_df,
    use_container_width=True
)


# ------------------------------------------------------------
# 17. DOWNLOAD FILTERED DATASET
# ------------------------------------------------------------

csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(

    label="Download Filtered Dataset",

    data=csv_data,

    file_name="student_performance_filtered.csv",

    mime="text/csv"

)


st.divider()


# ------------------------------------------------------------
# 18. PROJECT FOOTER
# ------------------------------------------------------------

st.caption(
    "Student Performance Analysis | "
    "Data Analysis Project"
)