import streamlit as st
import json
import pandas as pd
import altair as alt
import plotly.graph_objects as go
import plotly.io as pio
import io

# Configure plotly to use 'json' engine instead of 'orjson'
pio.json.config.default_engine = 'json'

# Load scoring scales
SCORING_SCALES = {
    "Use Case": {
        "Low": 1, "Moderate": 2, "High": 3, "Very High": 4
    },
    "Ease of Use": {
        "Basic": 1, "Moderate": 2, "High": 3, "Very High": 4
    },
    "Flexibility": {
        "Limited": 1, "Moderate": 2, "High": 3, "Very High": 4, "Excellent": 5
    },
    "Scalability": {
        "Limited": 1, "Moderate": 2, "High": 3, "Very High": 4
    },
    "Integration Capabilities": {
        "Basic": 1, "Good": 2, "Very Good": 3, "Excellent": 4
    },
    "Security": {
        "Basic": 1, "Moderate": 2, "High": 3, "Very High": 4
    },
    "Specialization": {
        "General": 1, "Moderate": 2, "High": 3, "Very High": 4
    },
    "Cost Efficiency": {
        "Low": 1, "Moderate": 2, "Good": 3, "High": 4
    },
    "Open Source vs. Proprietary": {
        "Proprietary": 1, "Hybrid": 2, "Mixed": 3, "Open Source": 4
    },
    "Support and Documentation": {
        "Basic": 1, "Good": 2, "High": 3, "Excellent": 4
    },
    "Performance": {
        "Moderate": 1, "High": 2, "Very High": 3, "Excellent": 4
    },
    "Popularity and Adoption": {
        "Low": 1, "Moderate": 2, "High": 3, "Very High": 4, "Excellent": 5
    },
    "GitHub Stars": {
        "Under 1K": 1, "1K-10K": 2, "10K-50K": 3, "50K-100K": 4, "100K+": 5, "N/A": 0
    },
    "Latest Update": {
        "Over 6 months": 1, "3-6 months": 2, "1-3 months": 3, "Within 1 month": 4
    },
    "Observability Features": {
        "Basic": 1, "Standard": 2, "Advanced": 3, "Enterprise": 4
    },
    "Debugging Capabilities": {
        "Basic": 1, "Standard": 2, "Advanced": 3, "Comprehensive": 4
    },
    "Integration Support": {
        "Few Integrations": 1, "Standard Integrations": 2, "Wide Range": 3, "Extensive Ecosystem": 4
    },
    "Collaboration Tools": {
        "Basic": 1, "Team Features": 2, "Advanced Collaboration": 3, "Enterprise Grade": 4
    },
    "Cost and Pricing": {
        "Free/Open Source": 4, "Affordable": 3, "Moderate": 2, "Enterprise": 1
    },
    "Deployment Options": {
        "Limited": 1, "Standard": 2, "Flexible": 3, "Highly Flexible": 4
    }
}

def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)

def get_numerical_score(criterion, rating):
    return SCORING_SCALES[criterion].get(rating, 0)

def calculate_scores(data):
    scores = {}
    for framework, details in data.items():
        total_score = 0
        for criterion, evaluation in details['evaluations'].items():
            score = get_numerical_score(criterion, evaluation['rating'])
            total_score += score
        scores[framework] = total_score
    return scores

def create_scoring_scales_df():
    # Convert SCORING_SCALES to a more readable DataFrame format
    scales_data = []
    for criterion, ratings in SCORING_SCALES.items():
        for rating, score in ratings.items():
            scales_data.append({
                'Criterion': criterion,
                'Rating': rating,
                'Score': score
            })
    return pd.DataFrame(scales_data)

def create_sidebar():
    st.sidebar.title("Evaluation Criteria Guide")
    
    # Add Overview section at the top of the sidebar
    with st.sidebar.expander("📋 Evaluation Overview", expanded=False):
        st.markdown("""
        ### Framework Evaluation Methodology
        
        The evaluation of each framework is based on a comprehensive set of criteria to determine its suitability for AI Chatbot and AI Assistant use cases.
        
        **Evidence Collection:**
        - Official documentation
        - GitHub repositories
        - Community feedback
        - Credible third-party sources
        
        Each rating is supported by specific evidence to ensure objective evaluation.
        """)
        
        # Add a divider
        st.markdown("---")
        
        # Show all criteria in a clean list format
        st.markdown("### Complete Criteria List")
        criteria_descriptions = {
            "Use Case": "Verifying support for AI Chatbot and Assistant use cases through tutorials, examples, or documentation.",
            "Ease of Use": "Assessing simplicity in setup, learning curve, and user experience based on documentation and community feedback.",
            "Flexibility": "Evaluating adaptability to various use cases, customization options, and extensibility.",
            "Scalability": "Checking the framework's ability to handle large-scale deployments or high traffic.",
            "Integration Capabilities": "Reviewing the quality and quantity of integrations with tools, APIs, or platforms.",
            "Security": "Assessing features like data encryption, user authentication, and compliance with standards.",
            "Specialization": "Determining if the framework is tailored for specific use cases or industries.",
            "Cost Efficiency": "Evaluating affordability, whether free, open source, or enterprise-priced.",
            "Open Source vs. Proprietary": "Identifying the framework's licensing model.",
            "Support and Documentation": "Checking the quality of documentation, tutorials, and community or enterprise support.",
            "Performance": "Reviewing benchmarks, reviews, or performance metrics.",
            "Popularity and Adoption": "Measuring GitHub stars, community size, and industry adoption.",
            "GitHub Stars": "Checking the number of stars and forks on GitHub.",
            "Latest Update": "Reviewing the frequency of updates on GitHub or the official website.",
            "Observability Features": "Looking for monitoring, logging, and observability tools.",
            "Debugging Capabilities": "Assessing debugging tools and error-handling features.",
            "Integration Support": "Evaluating the range of supported integrations.",
            "Collaboration Tools": "Checking for team collaboration features.",
            "Cost and Pricing": "Reviewing pricing models and affordability.",
            "Deployment Options": "Assessing deployment flexibility (e.g., cloud, on-premises, hybrid)."
        }
        
        for criterion, description in criteria_descriptions.items():
            st.markdown(f"**{criterion}**")
            st.markdown(f"- {description}")
            st.markdown("")
    
    # Add a search box for criteria
    search = st.sidebar.text_input("Search criteria", "")
    
    # Create expandable sections for each group of criteria
    criteria_groups = {
        "Core Features": [
            ("Use Case", "Evaluates support for AI Chatbot and AI Assistant use cases, including available tutorials and examples."),
            ("Ease of Use", "Measures setup simplicity, learning curve, and overall user experience."),
            ("Flexibility", "Assesses adaptability to different use cases and customization options."),
            ("Scalability", "Evaluates capability to handle large-scale deployments and high traffic.")
        ],
        "Technical Aspects": [
            ("Integration Capabilities", "Number and quality of integrations with other tools and platforms."),
            ("Security", "Available security features including encryption and authentication."),
            ("Performance", "Framework performance based on benchmarks and metrics."),
            ("Debugging Capabilities", "Quality of debugging tools and error-handling features.")
        ],
        "Business Factors": [
            ("Cost Efficiency", "Overall cost considerations including free/paid options."),
            ("Open Source vs. Proprietary", "Framework licensing model and source code availability."),
            ("Support and Documentation", "Quality of documentation, tutorials, and support channels."),
            ("Specialization", "Focus on specific use cases or industries.")
        ],
        "Community & Updates": [
            ("Popularity and Adoption", "Community size and industry adoption metrics."),
            ("GitHub Stars", "Repository popularity on GitHub (stars and forks)."),
            ("Latest Update", "Frequency and recency of updates."),
            ("Collaboration Tools", "Available team collaboration features.")
        ],
        "Enterprise Features": [
            ("Observability Features", "Monitoring and logging capabilities."),
            ("Integration Support", "Range and depth of supported integrations."),
            ("Cost and Pricing", "Detailed pricing models and plans."),
            ("Deployment Options", "Available deployment methods (cloud/on-prem).")
        ]
    }
    
    # Display criteria based on search
    for group, criteria in criteria_groups.items():
        # Filter criteria based on search
        if search:
            filtered_criteria = [c for c in criteria if search.lower() in c[0].lower() or search.lower() in c[1].lower()]
            if not filtered_criteria:
                continue
        else:
            filtered_criteria = criteria
            
        if filtered_criteria:
            with st.sidebar.expander(f"📌 {group}"):
                for criterion, description in filtered_criteria:
                    st.markdown(f"**{criterion}**")
                    st.markdown(f"{description}")
                    # Show scoring scale for this criterion
                    if criterion in SCORING_SCALES:
                        scale_df = pd.DataFrame(
                            [(k, v) for k, v in SCORING_SCALES[criterion].items()],
                            columns=['Rating', 'Score']
                        )
                        st.dataframe(scale_df, hide_index=True, use_container_width=True)
                    st.markdown("---")

def create_radar_chart(data, selected_frameworks, criteria):
    fig = go.Figure()
    
    for framework in selected_frameworks:
        scores = []
        for criterion in criteria:
            rating = data[framework]['evaluations'][criterion]['rating']
            score = get_numerical_score(criterion, rating)
            scores.append(score)
        
        fig.add_trace(go.Scatterpolar(
            r=scores,
            theta=criteria,
            name=framework,
            fill='toself'
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )
        ),
        showlegend=True,
        title="Framework Comparison Radar Chart",
        height=600
    )
    
    # Convert to JSON using the default engine
    fig.update_layout(template='plotly')
    return fig

def convert_df_to_data(edited_df):
    """Convert the edited DataFrame back to the original data structure"""
    data = {}
    for _, row in edited_df.iterrows():
        framework = row['Framework']
        data[framework] = {'evaluations': {}}
        for criterion in SCORING_SCALES.keys():
            data[framework]['evaluations'][criterion] = {
                'rating': row[f"{criterion} Rating"],
                'details': row[f"{criterion} Details"]
            }
    return data

def main():
    st.set_page_config(layout="wide")
    
    # Add sidebar
    create_sidebar()
    
    # Main content
    st.title("Multi-Agent Frameworks Analysis")
    
    # Load data
    data = load_data()
    
    # Create detailed scores table with clickable cells
    st.header("Detailed Scores")
    
    # Prepare data for the table
    frameworks = list(data.keys())
    criteria = list(SCORING_SCALES.keys())
    
    # Create a DataFrame for the scores and details
    scores_data = []
    for framework in frameworks:
        row = {'Framework': framework}
        for criterion in criteria:
            eval_data = data[framework]['evaluations'][criterion]
            row[f"{criterion} Rating"] = eval_data['rating']
            row[f"{criterion} Details"] = eval_data['details']
        scores_data.append(row)
    
    df = pd.DataFrame(scores_data)
    
    # Create column configuration for the table
    column_config = {
        "Framework": st.column_config.TextColumn(
            "Framework",
            width="medium",
            required=True,
        )
    }
    
    # Add column configs for each criterion
    for criterion in criteria:
        column_config[f"{criterion} Rating"] = st.column_config.SelectboxColumn(
            f"{criterion} Rating",
            width="medium",
            options=list(SCORING_SCALES[criterion].keys()),
            required=True,
        )
        column_config[f"{criterion} Details"] = st.column_config.TextColumn(
            f"{criterion} Details",
            width="large",
        )
    
    # Display the table
    st.write("Click on a cell to view or modify ratings and details")
    edited_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        column_config=column_config,
        key="framework_table"
    )
    
    # Convert edited DataFrame back to data structure
    updated_data = convert_df_to_data(edited_df)
    
    # Add download button for Excel file with both sheets
    if st.download_button(
        label="Download Excel file",
        data=create_excel_file(edited_df),
        file_name="framework_analysis.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        st.success("File downloaded successfully!")
    
    # Calculate total scores using updated data
    st.header("Total Scores Comparison")
    scores = calculate_scores(updated_data)
    df_scores = pd.DataFrame(list(scores.items()), columns=['Framework', 'Total Score'])
    df_scores = df_scores.sort_values('Total Score', ascending=False)
    
    # Create bar chart using Altair with updated data
    chart = alt.Chart(df_scores).mark_bar().encode(
        x='Framework',
        y='Total Score',
        tooltip=['Framework', 'Total Score']
    ).properties(
        title='Framework Total Scores'
    )
    st.altair_chart(chart, use_container_width=True)
    
    # Framework comparison with updated data
    st.header("Framework Comparison")
    selected_frameworks = st.multiselect(
        "Select frameworks to compare",
        options=list(updated_data.keys()),
        default=list(updated_data.keys())[:3]
    )
    
    if selected_frameworks:
        # Create comparison table with updated data
        comparison_data = []
        for framework in selected_frameworks:
            row = {'Framework': framework}
            for criterion in criteria:
                rating = updated_data[framework]['evaluations'][criterion]['rating']
                score = get_numerical_score(criterion, rating)
                row[criterion] = f"{rating} ({score})"
            comparison_data.append(row)
        
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True)
        
        # Add radar chart with updated data
        radar_fig = create_radar_chart(updated_data, selected_frameworks, criteria)
        st.plotly_chart(radar_fig, use_container_width=True)

def create_excel_file(data_df):
    # Create an Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Write the main data to the first sheet
        data_df.to_excel(writer, sheet_name='Framework Analysis', index=False)
        
        # Write the scoring scales to the second sheet
        scoring_scales_df = create_scoring_scales_df()
        scoring_scales_df.to_excel(writer, sheet_name='Scoring Scales', index=False)
        
        # Auto-adjust column widths
        for sheet in writer.sheets.values():
            for column in sheet.columns:
                max_length = 0
                column = [cell for cell in column]
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass
                adjusted_width = (max_length + 2)
                sheet.column_dimensions[column[0].column_letter].width = adjusted_width
    
    output.seek(0)
    return output

if __name__ == "__main__":
    main()
