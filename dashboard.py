import streamlit as st
import pandas as pd

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Apollo Data Mining Dashboard",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# HEADER
# ============================================================

st.title("📊 Apollo Data Mining & Contact Quality Dashboard")

st.write(
    "Interactive analysis of business contact data using "
    "Python, Pandas and Streamlit."
)

st.divider()

# ============================================================
# FILE UPLOAD
# ============================================================

file = st.file_uploader(
    "Upload your Apollo CSV",
    type=["csv"]
)

# ============================================================
# MAIN APPLICATION
# ============================================================

if file:

    # ========================================================
    # LOAD DATA
    # ========================================================

    df = pd.read_csv(file)

    # Clean column names
    df.columns = [c.strip() for c in df.columns]

    # ========================================================
    # SIDEBAR FILTERS
    # ========================================================

    st.sidebar.header("🔎 Dashboard Filters")

    # ========================================================
    # FILTER OPTIONS
    # ========================================================

    status_options = sorted(
        df["Email Status"]
        .dropna()
        .unique()
        .tolist()
    )

    company_options = sorted(
        df["Company Name"]
        .dropna()
        .unique()
        .tolist()
    )

    if "Seniority" in df.columns:

        seniority_options = sorted(
            df["Seniority"]
            .dropna()
            .unique()
            .tolist()
        )

    else:

        seniority_options = []

    # ========================================================
    # INITIALIZE SESSION STATE
    # ========================================================

    if "status_filter" not in st.session_state:

        st.session_state["status_filter"] = (
            status_options.copy()
        )

    if "company_filter" not in st.session_state:

        st.session_state["company_filter"] = []

    if "seniority_filter" not in st.session_state:

        st.session_state["seniority_filter"] = []

    # ========================================================
    # RESET FILTERS
    # ========================================================

    if st.sidebar.button(
        "🔄 Reset Filters",
        use_container_width=True
    ):

        st.session_state["status_filter"] = (
            status_options.copy()
        )

        st.session_state["company_filter"] = []

        st.session_state["seniority_filter"] = []

        st.rerun()

    # ========================================================
    # EMAIL STATUS FILTER
    # ========================================================

    selected_status = st.sidebar.multiselect(
        "📧 Email Status",
        options=status_options,
        key="status_filter"
    )

    # ========================================================
    # COMPANY FILTER
    # ========================================================

    selected_companies = st.sidebar.multiselect(
        "🏢 Company",
        options=company_options,
        key="company_filter"
    )

    # ========================================================
    # SENIORITY FILTER
    # ========================================================

    if "Seniority" in df.columns:

        selected_seniority = st.sidebar.multiselect(
            "👥 Seniority",
            options=seniority_options,
            key="seniority_filter"
        )

    else:

        selected_seniority = []

    # ========================================================
    # APPLY FILTERS
    # ========================================================

    filtered_df = df.copy()

    if selected_status:

        filtered_df = filtered_df[
            filtered_df["Email Status"].isin(
                selected_status
            )
        ]

    if selected_companies:

        filtered_df = filtered_df[
            filtered_df["Company Name"].isin(
                selected_companies
            )
        ]

    if selected_seniority:

        filtered_df = filtered_df[
            filtered_df["Seniority"].isin(
                selected_seniority
            )
        ]

    # ========================================================
    # CALCULATE METRICS
    # ========================================================

    total = len(filtered_df)

    verified = int(
        (
            filtered_df["Email Status"]
            == "Verified"
        ).sum()
    )

    unavailable = int(
        (
            filtered_df["Email Status"]
            == "Unavailable"
        ).sum()
    )

    extrapolated = int(
        (
            filtered_df["Email Status"]
            == "Extrapolated"
        ).sum()
    )

    verified_rate = (
        verified / total * 100
        if total > 0
        else 0
    )

    unique_companies = (
        filtered_df["Company Name"]
        .nunique()
    )

    # ========================================================
    # KEY METRICS
    # ========================================================

    st.subheader("📌 Key Metrics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Contacts",
        total
    )

    c2.metric(
        "Verified Emails",
        verified
    )

    c3.metric(
        "Verified Rate",
        f"{verified_rate:.1f}%"
    )

    c4.metric(
        "Unique Companies",
        unique_companies
    )

    st.divider()

    # ========================================================
    # AUTOMATIC DATA INSIGHTS
    # ========================================================

    st.subheader("💡 Data Insights")

    i1, i2, i3 = st.columns(3)

    if not filtered_df.empty:

        # Top company
        company_counts = (
            filtered_df["Company Name"]
            .value_counts()
        )

        top_company = company_counts.index[0]

        top_company_count = company_counts.iloc[0]

        i1.info(
            f"🏢 **Top Company**\n\n"
            f"{top_company}\n\n"
            f"{top_company_count} contacts"
        )

        # Top job title
        title_counts = (
            filtered_df["Title"]
            .value_counts()
        )

        top_title = title_counts.index[0]

        top_title_count = title_counts.iloc[0]

        i2.info(
            f"💼 **Most Common Job Title**\n\n"
            f"{top_title}\n\n"
            f"{top_title_count} contacts"
        )

        # Main location
        if "City" in filtered_df.columns:

            city_counts = (
                filtered_df["City"]
                .value_counts()
            )

            if not city_counts.empty:

                top_city = city_counts.index[0]

                i3.info(
                    f"📍 **Main Location**\n\n"
                    f"{top_city}"
                )

    st.divider()

    # ========================================================
    # EMAIL QUALITY
    # ========================================================

    st.subheader("📧 Email Quality")

    col1, col2 = st.columns(2)

    with col1:

        email_counts = (
            filtered_df["Email Status"]
            .value_counts()
        )

        st.write("Email Status Distribution")

        st.bar_chart(
            email_counts,
            use_container_width=True
        )

    with col2:

        st.write("Email Quality Details")

        email_table = pd.DataFrame({
            "Status": email_counts.index,
            "Contacts": email_counts.values
        })

        st.dataframe(
            email_table,
            use_container_width=True,
            hide_index=True
        )

        st.metric(
            "Verified Email Rate",
            f"{verified_rate:.1f}%"
        )

    st.divider()

    # ========================================================
    # COMPANY ANALYSIS
    # ========================================================

    st.subheader("🏢 Company Analysis")

    col1, col2 = st.columns(2)

    with col1:

        company_counts = (
            filtered_df["Company Name"]
            .value_counts()
            .head(10)
        )

        st.write("Top Companies")

        st.bar_chart(
            company_counts,
            use_container_width=True
        )

    with col2:

        company_table = (
            filtered_df["Company Name"]
            .value_counts()
            .reset_index()
        )

        company_table.columns = [
            "Company",
            "Contacts"
        ]

        st.write("Company Contact Summary")

        st.dataframe(
            company_table,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ========================================================
    # SENIORITY ANALYSIS
    # ========================================================

    if "Seniority" in filtered_df.columns:

        st.subheader("👥 Seniority Distribution")

        seniority_counts = (
            filtered_df["Seniority"]
            .value_counts()
        )

        st.bar_chart(
            seniority_counts,
            use_container_width=True
        )

    st.divider()

    # ========================================================
    # JOB TITLE ANALYSIS
    # ========================================================

    st.subheader("💼 Top Job Titles")

    title_counts = (
        filtered_df["Title"]
        .value_counts()
        .head(10)
    )

    st.bar_chart(
        title_counts,
        use_container_width=True
    )

    st.divider()

    # ========================================================
    # LOCATION ANALYSIS
    # ========================================================

    st.subheader("📍 Location Analysis")

    col1, col2 = st.columns(2)

    with col1:

        if "City" in filtered_df.columns:

            st.write("Cities")

            city_counts = (
                filtered_df["City"]
                .value_counts()
            )

            st.bar_chart(
                city_counts,
                use_container_width=True
            )

    with col2:

        if "State" in filtered_df.columns:

            st.write("States")

            state_counts = (
                filtered_df["State"]
                .value_counts()
            )

            st.bar_chart(
                state_counts,
                use_container_width=True
            )

    st.divider()

    # ========================================================
    # INDUSTRY ANALYSIS
    # ========================================================

    if "Industry" in filtered_df.columns:

        st.subheader("🏭 Industry Distribution")

        industry_counts = (
            filtered_df["Industry"]
            .value_counts()
            .head(10)
        )

        st.bar_chart(
            industry_counts,
            use_container_width=True
        )

    st.divider()

    # ========================================================
    # DATA QUALITY ANALYSIS
    # ========================================================

    st.subheader("🔍 Data Quality Analysis")

    important_columns = [
        "Title",
        "Company Name",
        "Email",
        "Email Status",
        "City",
        "State",
        "Industry"
    ]

    quality_data = []

    for column in important_columns:

        if column in filtered_df.columns:

            missing = int(
                filtered_df[column].isna().sum()
            )

            missing_percentage = (
                missing / total * 100
                if total > 0
                else 0
            )

            quality_data.append({
                "Column": column,
                "Missing Values": missing,
                "Missing %": round(
                    missing_percentage,
                    1
                )
            })

    quality_df = pd.DataFrame(
        quality_data
    )

    st.dataframe(
        quality_df,
        use_container_width=True,
        hide_index=True
    )

    # ========================================================
    # DATA QUALITY METRICS
    # ========================================================

    q1, q2, q3 = st.columns(3)

    if "Email" in filtered_df.columns:

        missing_emails = int(
            filtered_df["Email"].isna().sum()
        )

    else:

        missing_emails = 0

    total_cells = (
        len(filtered_df)
        * len(filtered_df.columns)
    )

    missing_cells = (
        filtered_df.isna().sum().sum()
    )

    completeness = (
        100
        - (
            missing_cells
            / total_cells
            * 100
        )
        if total_cells > 0
        else 0
    )

    q1.metric(
        "Verified Emails",
        verified
    )

    q2.metric(
        "Missing Emails",
        missing_emails
    )

    q3.metric(
        "Data Completeness",
        f"{completeness:.1f}%"
    )

    st.divider()

    # ========================================================
    # CONTACT DATA
    # ========================================================

    st.subheader("📄 Contact Data")

    st.write(
        f"Showing **{len(filtered_df)}** contacts"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=400
    )

    # ========================================================
    # DOWNLOAD FILTERED DATA
    # ========================================================

    csv_data = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Filtered CSV",
        data=csv_data,
        file_name="filtered_apollo_contacts.csv",
        mime="text/csv"
    )

else:

    # ========================================================
    # INITIAL SCREEN
    # ========================================================

    st.info(
        "Upload an Apollo CSV to start the analysis."
    )

    st.markdown(
        """
        ### 📊 Dashboard Features

        - 📌 Key metrics
        - 💡 Automatic data insights
        - 📧 Email quality analysis
        - 🏢 Company analysis
        - 👥 Seniority analysis
        - 💼 Job title analysis
        - 📍 Location analysis
        - 🏭 Industry analysis
        - 🔍 Data quality analysis
        - 🔎 Interactive filters
        - 🔄 Reset filters
        - ⬇️ Filtered CSV download
        """
    )