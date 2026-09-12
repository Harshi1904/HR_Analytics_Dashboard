import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PROFESSIONAL CSS
# ============================================================
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Hide Streamlit default menu */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Main container */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* Header */
    .main-header {
        background: linear-gradient(135deg, #172554, #1d4ed8);
        padding: 28px 35px;
        border-radius: 18px;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(30, 64, 175, 0.15);
    }

    .main-title {
        color: white;
        font-size: 34px;
        font-weight: 800;
        margin: 0;
    }

    .main-subtitle {
        color: #dbeafe;
        font-size: 15px;
        margin-top: 8px;
    }

    /* KPI Cards */
    .kpi-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
        min-height: 125px;
    }

    .kpi-icon {
        font-size: 25px;
    }

    .kpi-title {
        color: #64748b;
        font-size: 13px;
        font-weight: 600;
        margin-top: 5px;
    }

    .kpi-value {
        color: #0f172a;
        font-size: 28px;
        font-weight: 800;
        margin-top: 4px;
    }

    .kpi-description {
        color: #94a3b8;
        font-size: 11px;
        margin-top: 3px;
    }

    /* Section headings */
    .section-title {
        color: #0f172a;
        font-size: 21px;
        font-weight: 750;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 13px;
        margin-bottom: 15px;
    }

    /* Insight cards */
    .insight-card {
        background: white;
        padding: 18px;
        border-radius: 14px;
        border-left: 5px solid #2563eb;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.05);
        margin-bottom: 12px;
    }

    .insight-title {
        font-weight: 700;
        color: #0f172a;
        font-size: 15px;
    }

    .insight-text {
        color: #475569;
        font-size: 13px;
        margin-top: 5px;
        line-height: 1.5;
    }

    /* Risk indicator */
    .risk-card {
        padding: 20px;
        border-radius: 15px;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
        text-align: center;
    }

    .risk-label {
        color: #64748b;
        font-size: 13px;
        font-weight: 600;
    }

    .risk-value {
        font-size: 27px;
        font-weight: 800;
        margin-top: 5px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Footer */
    .custom-footer {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        padding: 25px 0 5px 0;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================
@st.cache_data
def load_data():
    df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.markdown("## 👥 HR Analytics")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Dashboard Navigation",
    [
        "📊 HR Overview",
        "📉 Attrition Analysis",
        "👤 Employee Insights"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔎 Filters")

departments = sorted(df["Department"].dropna().unique())
genders = sorted(df["Gender"].dropna().unique())
job_roles = sorted(df["JobRole"].dropna().unique())

selected_departments = st.sidebar.multiselect(
    "Department",
    departments,
    default=departments
)

selected_genders = st.sidebar.multiselect(
    "Gender",
    genders,
    default=genders
)

selected_roles = st.sidebar.multiselect(
    "Job Role",
    job_roles,
    default=job_roles
)


# ============================================================
# FILTER DATA
# ============================================================
filtered_df = df[
    (df["Department"].isin(selected_departments)) &
    (df["Gender"].isin(selected_genders)) &
    (df["JobRole"].isin(selected_roles))
].copy()


# ============================================================
# EMPTY DATA CHECK
# ============================================================
if filtered_df.empty:

    st.warning(
        "⚠️ No employees match the selected filters. "
        "Please change the filters from the sidebar."
    )

    st.stop()


# ============================================================
# COMMON CALCULATIONS
# ============================================================
total_employees = len(filtered_df)

employees_left = (
    filtered_df["Attrition"]
    .eq("Yes")
    .sum()
)

employees_stayed = (
    filtered_df["Attrition"]
    .eq("No")
    .sum()
)

attrition_rate = (
    employees_left / total_employees * 100
    if total_employees > 0
    else 0
)

avg_income = filtered_df["MonthlyIncome"].mean()

avg_age = filtered_df["Age"].mean()


# ============================================================
# HEADER
# ============================================================
st.markdown("""
<div class="main-header">
    <div class="main-title">👥 HR Analytics Dashboard</div>
    <div class="main-subtitle">
        Workforce intelligence • Employee insights • Attrition analysis
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR SUMMARY
# ============================================================
st.sidebar.markdown("### 📌 Current Selection")

st.sidebar.metric(
    "Employees",
    f"{total_employees:,}"
)

st.sidebar.metric(
    "Attrition Rate",
    f"{attrition_rate:.2f}%"
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Use the filters above to explore workforce patterns dynamically."
)


# ============================================================
# KPI FUNCTION
# ============================================================
def kpi_card(icon, title, value, description):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-icon">{icon}</div>
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CHART SETTINGS
# ============================================================
def apply_chart_style(fig, height=390):

    fig.update_layout(
        height=height,
        margin=dict(l=20, r=20, t=45, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(
            family="Arial",
            color="#334155"
        ),
        title_font=dict(
            size=17,
            color="#0f172a"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor="#e2e8f0"
    )

    fig.update_yaxes(
        gridcolor="#e2e8f0",
        zeroline=False
    )

    return fig


# ============================================================
# PAGE 1 — HR OVERVIEW
# ============================================================
if page == "📊 HR Overview":

    st.markdown(
        '<div class="section-title">Workforce Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A high-level view of the organization and employee workforce.'
        '</div>',
        unsafe_allow_html=True
    )

    # KPI ROW
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        kpi_card(
            "👥",
            "Total Employees",
            f"{total_employees:,}",
            "Employees in selection"
        )

    with c2:
        kpi_card(
            "🚪",
            "Employees Left",
            f"{employees_left:,}",
            "Recorded attrition"
        )

    with c3:
        kpi_card(
            "📉",
            "Attrition Rate",
            f"{attrition_rate:.2f}%",
            "Observed employee attrition"
        )

    with c4:
        kpi_card(
            "💰",
            "Avg Monthly Income",
            f"₹{avg_income:,.0f}",
            "Average monthly income"
        )

    with c5:
        kpi_card(
            "🎂",
            "Average Age",
            f"{avg_age:.1f}",
            "Average employee age"
        )


    # --------------------------------------------------------
    # RISK INDICATOR
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">HR Risk Indicator</div>',
        unsafe_allow_html=True
    )

    if attrition_rate >= 20:
        risk_text = "High"
        risk_message = "Attrition requires closer management attention."
    elif attrition_rate >= 15:
        risk_text = "Moderate"
        risk_message = "Attrition is at a level worth monitoring."
    else:
        risk_text = "Low"
        risk_message = "Attrition is comparatively lower in the selected workforce."

    r1, r2 = st.columns([1, 2])

    with r1:
        st.markdown(
            f"""
            <div class="risk-card">
                <div class="risk-label">CURRENT ATTRITION RISK</div>
                <div class="risk-value">{risk_text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with r2:
        st.info(f"💡 {risk_message}")


    # --------------------------------------------------------
    # DEPARTMENT + GENDER
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Workforce Distribution</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # Department
    with col1:

        dept_count = (
            filtered_df["Department"]
            .value_counts()
            .reset_index()
        )

        dept_count.columns = [
            "Department",
            "Employees"
        ]

        fig = px.bar(
            dept_count,
            x="Department",
            y="Employees",
            title="Employees by Department",
            text="Employees"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig = apply_chart_style(fig)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # Gender
    with col2:

        gender_count = (
            filtered_df["Gender"]
            .value_counts()
            .reset_index()
        )

        gender_count.columns = [
            "Gender",
            "Employees"
        ]

        fig = px.pie(
            gender_count,
            names="Gender",
            values="Employees",
            title="Gender Distribution",
            hole=0.55
        )

        fig.update_traces(
            textinfo="percent+label"
        )

        fig = apply_chart_style(fig)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # JOB ROLES
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Job Role Distribution</div>',
        unsafe_allow_html=True
    )

    role_count = (
        filtered_df["JobRole"]
        .value_counts()
        .sort_values()
        .reset_index()
    )

    role_count.columns = [
        "Job Role",
        "Employees"
    ]

    fig = px.bar(
        role_count,
        x="Employees",
        y="Job Role",
        orientation="h",
        title="Employees by Job Role",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig = apply_chart_style(fig, 470)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # ATTRITION BY DEPARTMENT
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Attrition by Department</div>',
        unsafe_allow_html=True
    )

    dept_attrition = (
        filtered_df
        .groupby("Department")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )

    dept_attrition.columns = [
        "Department",
        "Attrition Rate"
    ]

    dept_attrition = dept_attrition.sort_values(
        "Attrition Rate",
        ascending=False
    )

    fig = px.bar(
        dept_attrition,
        x="Department",
        y="Attrition Rate",
        title="Observed Attrition Rate by Department",
        text=dept_attrition["Attrition Rate"].round(2).astype(str) + "%"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    fig = apply_chart_style(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # DYNAMIC KEY FINDINGS
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">💡 Key HR Findings</div>',
        unsafe_allow_html=True
    )

    highest_dept = dept_attrition.iloc[0]

    highest_role_data = (
        filtered_df
        .groupby("JobRole")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .sort_values(ascending=False)
    )

    highest_role = highest_role_data.index[0]
    highest_role_rate = highest_role_data.iloc[0]

    findings = [
        (
            "Department with Highest Attrition",
            f"{highest_dept['Department']} shows the highest observed "
            f"attrition rate at {highest_dept['Attrition Rate']:.2f}%."
        ),
        (
            "Job Role Requiring Attention",
            f"{highest_role} has the highest observed attrition rate "
            f"among the selected job roles at {highest_role_rate:.2f}%."
        ),
        (
            "Overall Workforce",
            f"The selected workforce contains {total_employees:,} employees, "
            f"with {employees_left:,} recorded departures."
        )
    ]

    for title, text in findings:

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">{title}</div>
                <div class="insight-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# PAGE 2 — ATTRITION ANALYSIS
# ============================================================
elif page == "📉 Attrition Analysis":

    st.markdown(
        '<div class="section-title">Employee Attrition Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore factors associated with employee attrition.'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # ATTRITION DONUT
    # --------------------------------------------------------
    attrition_counts = (
        filtered_df["Attrition"]
        .value_counts()
        .reset_index()
    )

    attrition_counts.columns = [
        "Attrition",
        "Employees"
    ]

    col1, col2 = st.columns([1, 1])

    with col1:

        fig = px.pie(
            attrition_counts,
            names="Attrition",
            values="Employees",
            title="Employee Attrition Status",
            hole=0.55
        )

        fig.update_traces(
            textinfo="percent+label"
        )

        fig = apply_chart_style(fig)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:

        st.markdown(
            '<div class="section-title">Attrition Summary</div>',
            unsafe_allow_html=True
        )

        st.metric(
            "Employees Stayed",
            f"{employees_stayed:,}"
        )

        st.metric(
            "Employees Left",
            f"{employees_left:,}"
        )

        st.metric(
            "Observed Attrition Rate",
            f"{attrition_rate:.2f}%"
        )


    # --------------------------------------------------------
    # DEPARTMENT
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Attrition Rate by Department</div>',
        unsafe_allow_html=True
    )

    dept_attrition = (
        filtered_df
        .groupby("Department")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )

    dept_attrition.columns = [
        "Department",
        "Attrition Rate"
    ]

    fig = px.bar(
        dept_attrition.sort_values(
            "Attrition Rate",
            ascending=False
        ),
        x="Department",
        y="Attrition Rate",
        title="Observed Attrition Rate by Department",
        text=dept_attrition["Attrition Rate"].round(2).astype(str) + "%"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    fig = apply_chart_style(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # JOB ROLE
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Attrition Rate by Job Role</div>',
        unsafe_allow_html=True
    )

    role_attrition = (
        filtered_df
        .groupby("JobRole")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )

    role_attrition.columns = [
        "Job Role",
        "Attrition Rate"
    ]

    role_attrition = role_attrition.sort_values(
        "Attrition Rate",
        ascending=True
    )

    fig = px.bar(
        role_attrition,
        x="Attrition Rate",
        y="Job Role",
        orientation="h",
        title="Observed Attrition Rate by Job Role",
        text=role_attrition["Attrition Rate"].round(2).astype(str) + "%"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_xaxes(
        ticksuffix="%"
    )

    fig = apply_chart_style(fig, 470)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # OVERTIME
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Overtime and Attrition</div>',
        unsafe_allow_html=True
    )

    overtime_attrition = (
        filtered_df
        .groupby("OverTime")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )

    overtime_attrition.columns = [
        "OverTime",
        "Attrition Rate"
    ]

    fig = px.bar(
        overtime_attrition,
        x="OverTime",
        y="Attrition Rate",
        title="Observed Attrition Rate by Overtime",
        text=overtime_attrition["Attrition Rate"].round(2).astype(str) + "%"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    fig = apply_chart_style(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # JOB SATISFACTION
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Job Satisfaction and Attrition</div>',
        unsafe_allow_html=True
    )

    satisfaction_map = {
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Very High"
    }

    satisfaction_df = filtered_df.copy()

    satisfaction_df["Job Satisfaction Level"] = (
        satisfaction_df["JobSatisfaction"]
        .map(satisfaction_map)
    )

    satisfaction_attrition = (
        satisfaction_df
        .groupby("Job Satisfaction Level", observed=False)["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )

    satisfaction_attrition.columns = [
        "Job Satisfaction",
        "Attrition Rate"
    ]

    satisfaction_order = [
        "Low",
        "Medium",
        "High",
        "Very High"
    ]

    satisfaction_attrition["Job Satisfaction"] = pd.Categorical(
        satisfaction_attrition["Job Satisfaction"],
        categories=satisfaction_order,
        ordered=True
    )

    satisfaction_attrition = (
        satisfaction_attrition
        .sort_values("Job Satisfaction")
    )

    fig = px.bar(
        satisfaction_attrition,
        x="Job Satisfaction",
        y="Attrition Rate",
        title="Observed Attrition Rate by Job Satisfaction",
        text=satisfaction_attrition["Attrition Rate"].round(2).astype(str) + "%"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    fig = apply_chart_style(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # SALARY BAND
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Salary and Attrition</div>',
        unsafe_allow_html=True
    )

    salary_df = filtered_df.copy()

    salary_df["Salary Band"] = pd.cut(
        salary_df["MonthlyIncome"],
        bins=[0, 3000, 6000, 10000, np.inf],
        labels=[
            "₹0–3K",
            "₹3K–6K",
            "₹6K–10K",
            "₹10K+"
        ]
    )

    salary_attrition = (
        salary_df
        .groupby("Salary Band", observed=False)["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )

    salary_attrition.columns = [
        "Salary Band",
        "Attrition Rate"
    ]

    fig = px.bar(
        salary_attrition,
        x="Salary Band",
        y="Attrition Rate",
        title="Observed Attrition Rate by Salary Band",
        text=salary_attrition["Attrition Rate"].round(2).astype(str) + "%"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    fig = apply_chart_style(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # TENURE
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Tenure and Attrition</div>',
        unsafe_allow_html=True
    )

    tenure_df = filtered_df.copy()

    tenure_df["Tenure Band"] = pd.cut(
        tenure_df["YearsAtCompany"],
        bins=[-1, 2, 5, 10, np.inf],
        labels=[
            "0–2 Years",
            "3–5 Years",
            "6–10 Years",
            "10+ Years"
        ]
    )

    tenure_attrition = (
        tenure_df
        .groupby("Tenure Band", observed=False)["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )

    tenure_attrition.columns = [
        "Tenure Band",
        "Attrition Rate"
    ]

    fig = px.bar(
        tenure_attrition,
        x="Tenure Band",
        y="Attrition Rate",
        title="Observed Attrition Rate by Years at Company",
        text=tenure_attrition["Attrition Rate"].round(2).astype(str) + "%"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_yaxes(
        ticksuffix="%"
    )

    fig = apply_chart_style(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PAGE 3 — EMPLOYEE INSIGHTS
# ============================================================
elif page == "👤 Employee Insights":

    st.markdown(
        '<div class="section-title">Employee Insights</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore workforce demographics, experience and employee-related factors.'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # AGE DISTRIBUTION
    # --------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            filtered_df,
            x="Age",
            nbins=20,
            title="Employee Age Distribution"
        )

        fig = apply_chart_style(fig)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # TOTAL WORKING YEARS
    # --------------------------------------------------------
    with col2:

        fig = px.histogram(
            filtered_df,
            x="TotalWorkingYears",
            nbins=20,
            title="Total Working Experience"
        )

        fig = apply_chart_style(fig)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # PERFORMANCE RATING
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Performance Rating</div>',
        unsafe_allow_html=True
    )

    performance = (
        filtered_df["PerformanceRating"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    performance.columns = [
        "Performance Rating",
        "Employees"
    ]

    fig = px.bar(
        performance,
        x="Performance Rating",
        y="Employees",
        title="Employees by Performance Rating",
        text="Employees"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig = apply_chart_style(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # WORK LIFE BALANCE
    # --------------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:

        worklife = (
            filtered_df["WorkLifeBalance"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        worklife.columns = [
            "Work-Life Balance",
            "Employees"
        ]

        fig = px.bar(
            worklife,
            x="Work-Life Balance",
            y="Employees",
            title="Work-Life Balance Distribution",
            text="Employees"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig = apply_chart_style(fig)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # TRAINING
    # --------------------------------------------------------
    with col2:

        training = (
            filtered_df["TrainingTimesLastYear"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        training.columns = [
            "Training Sessions",
            "Employees"
        ]

        fig = px.bar(
            training,
            x="Training Sessions",
            y="Employees",
            title="Training Sessions Last Year",
            text="Employees"
        )

        fig.update_traces(
            textposition="outside"
        )

        fig = apply_chart_style(fig)

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # --------------------------------------------------------
    # INCOME VS EXPERIENCE
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">Income vs Experience</div>',
        unsafe_allow_html=True
    )

    fig = px.scatter(
        filtered_df,
        x="YearsAtCompany",
        y="MonthlyIncome",
        color="Attrition",
        hover_data=[
            "JobRole",
            "Department",
            "Age"
        ],
        title="Monthly Income vs Years at Company"
    )

    fig.update_xaxes(
        title="Years at Company"
    )

    fig.update_yaxes(
        title="Monthly Income"
    )

    fig = apply_chart_style(fig, 450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # BUSINESS INSIGHTS
    # --------------------------------------------------------
    st.markdown(
        '<div class="section-title">💡 Business Insights</div>',
        unsafe_allow_html=True
    )

    avg_tenure = filtered_df["YearsAtCompany"].mean()
    avg_experience = filtered_df["TotalWorkingYears"].mean()

    insights = [
        (
            "Workforce Age",
            f"The average age of employees in the selected workforce "
            f"is {avg_age:.1f} years."
        ),
        (
            "Company Tenure",
            f"Employees have an average tenure of "
            f"{avg_tenure:.1f} years at the company."
        ),
        (
            "Professional Experience",
            f"Average total working experience is "
            f"{avg_experience:.1f} years."
        ),
        (
            "Attrition",
            f"The selected workforce has an observed attrition rate "
            f"of {attrition_rate:.2f}%."
        )
    ]

    for title, text in insights:

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-title">{title}</div>
                <div class="insight-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <div class="custom-footer">
        HR Analytics Dashboard • Built with Python, Pandas, Plotly & Streamlit
        <br>
        Workforce insights for data-driven HR decision making
    </div>
    """,
    unsafe_allow_html=True
)