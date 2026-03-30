# 🌍 EU PR Intelligence System

A comprehensive web application for searching, filtering, and comparing Permanent Residence (PR) requirements across European countries.

## ✨ Features

- **🔍 Advanced Search & Filtering**
  - Filter countries by continent
  - Search by country name
  - Filter by immigration route (Student, Work, Family)

- **📊 Country Comparison Tool**
  - Side-by-side comparison of multiple countries
  - View all PR requirements at a glance
  - Compare language requirements, citizenship timelines, and more

- **📋 Comprehensive Database**
  - 30+ European countries (EU and non-EU)
  - Detailed PR information for each country
  - Language requirements, income thresholds, residency rules
  - Family sponsorship and spousal work permissions

- **📥 Export Functionality**
  - Export all country data to Excel spreadsheet
  - Perfect for research and analysis

- **➕ Add New Records**
  - Easily add new country PR information
  - Structured form for consistent data entry

- **🎨 Modern, Responsive UI**
  - Beautiful gradient design
  - Mobile-friendly interface
  - Intuitive navigation

## 📋 Project Structure

```
EU_PR_System/
├── main.py                 # FastAPI application & routes
├── models.py              # SQLAlchemy ORM models
├── database.py            # Database configuration
├── scraper.py             # Sample data seeding
├── export_excel.py        # Excel export functionality
├── schemas.py             # Pydantic schemas (if applicable)
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css          # Application styling
├── templates/
│   ├── index.html         # Dashboard & country listing
│   ├── country.html       # Country detail page
│   └── compare.html       # Country comparison page
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohammadabdullah2724/EU_PR_System.git
   cd EU_PR_System
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application:**
   - Open your browser and navigate to `http://localhost:8000`

## 📊 Database Setup

The application uses SQLite for data storage. When you first run the application, the database will be created automatically.

### Seed Sample Data

To populate the database with sample PR data for 30+ European countries:
1. Click the **"📊 Seed Sample Data"** button on the dashboard
2. This will insert comprehensive PR information for all countries

## 🔧 API Routes

### GET Routes

| Route | Description |
|-------|-------------|
| `/` | Home page with country listing and filters |
| `/country/{id}` | View detailed PR information for a specific country |
| `/compare` | Country comparison tool |
| `/seed` | Seed the database with sample data |
| `/export` | Export all countries to Excel file |
| `/api/countries` | JSON API endpoint for countries |

### POST Routes

| Route | Description |
|-------|-------------|
| `/add` | Add a new country PR record |

## 📝 Data Fields

Each country record contains:

- **Basic Info**: Country name, continent, PR name, PR validity years
- **Immigration Routes**: Student, Work, Family route availability
- **Requirements**: Language proficiency, income requirements, continuous residence rules
- **Family**: Spousal permissions and work authorization for spouses
- **Citizenship**: Years required before citizenship eligibility
- **Official Source**: Link to official government immigration resource
- **Last Updated**: Date of last information update

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Data Export**: Pandas & openpyxl (Excel)
- **Server**: Uvicorn

## 📦 Dependencies

See `requirements.txt` for complete list:
- fastapi
- uvicorn
- sqlalchemy
- pandas
- openpyxl
- jinja2

## 🎯 Usage Examples

### Filter by Continent
1. Go to the dashboard
2. Select a continent from the dropdown (Europe)
3. Click "Filter" to view countries in that continent

### Search for a Country
1. Use the country search box
2. Type the country name
3. Click "Filter" to see results

### Compare Countries
1. Click the **"⚖️ Compare Countries"** button
2. View the list of available countries with their IDs
3. Enter comma-separated IDs (e.g., "1,2,3")
4. Click "📊 Compare" to view side-by-side comparison

### Export Data
1. Click the **"📥 Export to Excel"** button
2. The Excel file will automatically download
3. File includes all countries and their complete information

## 🔄 Recent Updates

### Latest Features (v1.1)
- ✅ Added continent field to country model
- ✅ Continent filtering capability
- ✅ Expanded sample data to 30+ countries
- ✅ Modern gradient UI design
- ✅ Improved table styling and responsiveness
- ✅ Enhanced country detail pages
- ✅ Better visual hierarchy with emojis

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Mohammad Abdullah**
- GitHub: [@mohammadabdullah2724](https://github.com/mohammadabdullah2724)

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please [open an issue](https://github.com/mohammadabdullah2724/EU_PR_System/issues) on GitHub.

## 📚 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 💡 Future Enhancements

- [ ] User authentication and accounts
- [ ] Bookmark favorite countries
- [ ] Email notifications for PR updates
- [ ] Mobile app
- [ ] Multiple language support
- [ ] Integration with official government APIs
- [ ] PR timeline calculator
- [ ] Document checklist generator

---

**Last Updated**: March 30, 2026

For questions or support, please contact the repository owner.
