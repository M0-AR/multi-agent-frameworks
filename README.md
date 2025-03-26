# Multi-Agent Frameworks Analysis Tool 🤖

An interactive Streamlit application for analyzing and comparing various multi-agent frameworks based on comprehensive evaluation criteria. This tool helps developers and organizations make informed decisions when choosing a multi-agent framework for their AI chatbot and assistant projects.

> **Note**: This project is an enhanced version of the [multi-agent-framework-comparison](https://github.com/M0-AR/multi-agent-framework-comparison) repository, building upon its foundation with additional features and improvements.

## 🌟 Features

- **Interactive Data Table**
  - View and modify framework ratings
  - Detailed evaluation descriptions
  - Click-to-view detailed information
  - Excel export functionality

- **Visual Comparisons**
  - Radar charts for framework comparison
  - Bar charts for total scores
  - Interactive framework selection

- **Comprehensive Evaluation**
  - 20+ evaluation criteria
  - Detailed scoring scales
  - Evidence-based ratings

- **User-Friendly Interface**
  - Searchable criteria
  - Organized sidebar categories
  - Expandable sections
  - Responsive design

## 📊 Evaluation Criteria

The frameworks are evaluated across multiple categories:

### Core Features
- Use Case Support
- Ease of Use
- Flexibility
- Scalability

### Technical Aspects
- Integration Capabilities
- Security Features
- Performance Metrics
- Debugging Tools

### Business Factors
- Cost Efficiency
- Licensing Model
- Documentation Quality
- Specialization

### Community & Updates
- Popularity Metrics
- GitHub Activity
- Update Frequency
- Collaboration Features

### Enterprise Features
- Observability Tools
- Integration Support
- Pricing Models
- Deployment Options

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-agent-frameworks.git
cd multi-agent-frameworks
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to:
```
http://localhost:8501
```

## 📦 Dependencies

- streamlit==1.32.0
- pandas==2.2.1
- altair==5.2.0
- plotly==5.19.0
- openpyxl==3.1.2

## 💡 Usage

1. **View Framework Evaluations**
   - Browse the detailed scores table
   - Click cells to view detailed evaluations
   - Use the search function to find specific criteria

2. **Compare Frameworks**
   - Select multiple frameworks to compare
   - View side-by-side comparisons in the table
   - Analyze the radar chart visualization
   - Export data to Excel for further analysis

3. **Understand Criteria**
   - Explore the sidebar's organized categories
   - Read detailed descriptions of each criterion
   - View scoring scales and methodologies

## 📊 Data Structure

The framework evaluations are stored in `data.json` with the following structure:
```json
{
    "Framework_Name": {
        "evaluations": {
            "Criterion": {
                "rating": "Rating_Value",
                "details": "Detailed_Description"
            }
        }
    }
}
```

## 🔄 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all framework developers and maintainers
- Community contributors and reviewers
- Streamlit team for the amazing framework

## 📧 Contact

For questions or feedback, please open an issue in the GitHub repository.

---
Made with ❤️ for the AI community
