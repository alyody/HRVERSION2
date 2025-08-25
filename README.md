# 🤖 LGL HR Assistant

An intelligent AI-powered HR assistant that provides comprehensive support for LGL employee handbook queries and HR operations.

## 🌟 Features

### 🎯 **Intelligent HR Support**
- Natural language processing for employee handbook queries
- Smart keyword detection and policy mapping
- Context-aware responses with relevant information
- Comprehensive coverage of all HR policies and procedures

### 💬 **Interactive Interface**
- Modern, responsive design with professional styling
- Real-time chat interface with LGL branding
- Quick action buttons for common HR topics
- Beautiful gradient backgrounds and smooth animations

### 📚 **Complete Handbook Coverage**
- **Working Hours** (Administrative & Academic staff schedules)
- **Employee Benefits** (Health insurance, Visa sponsorship)
- **Leave Policies** (Annual, Sick, Maternity, Parental, Bereavement)
- **Code of Conduct** (Professional standards, Dress code, Safeguarding)
- **Performance Management** (Appraisals, Probation procedures)
- **Disciplinary Procedures** (Misconduct, Warnings, Appeals)
- **Termination & Gratuity** (Notice periods, End of service benefits)

### 👥 **Employee Management**
- **Employee Login System** with personalized profiles
- **Leave Balance Tracking** with real-time calculations
- **Personalized Greetings** and employee details display
- **Department-based Access** to relevant policies

### 🔘 **Smart Leave Detection**
- When users type "leave" or similar general terms, the system automatically displays clickable buttons for:
  - 🏖️ Annual Leave
  - 🏥 Sick Leave  
  - 👶 Maternity Leave
  - 🍼 Bereavement Leave

## 🚀 Quick Start

### Local Development
```bash
# Clone or download the files to your local machine
cd "HRVERSION2"

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

### Streamlit Cloud Deployment
1. **Upload to GitHub**: Create a public repository with these files
2. **Connect to Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io/)
3. **Deploy**: Select your repository and set main file to `app.py`
4. **Auto-deploy**: Changes pushed to GitHub will automatically redeploy

## 📁 File Structure

```
HRVERSION2/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
└── .gitignore            # Git ignore file
```

## 💻 Application Components

### Employee Database
The system includes sample employee data with comprehensive tracking:
- Personal information and department details
- Leave balances and usage tracking
- Contract types and service years
- Manager assignments and approval workflows

### Handbook Data Structure
All HR policies are structured and organized for quick retrieval:
- **Working Hours**: Administrative and academic staff schedules
- **Leave Policies**: Detailed entitlements and application procedures
- **Benefits**: Health insurance, visa sponsorship, and other perks
- **Conduct Standards**: Professional behavior and safeguarding policies

### Smart Query Processing
- Keyword-based topic detection and matching
- Leave balance calculations based on service years
- Personalized responses for logged-in employees
- Smart leave type detection with clickable buttons
- Fallback responses for unmatched queries

## 📋 Sample Queries

### **Leave & Time Off**
- "How many annual leave days do I have left?"
- "What is the sick leave policy?"
- "How do I apply for maternity leave?"
- "leave" (triggers smart leave type selection)

### **Policies & Procedures**
- "What is the dress code policy?"
- "Tell me about the disciplinary procedure"
- "How does the performance appraisal work?"
- "What are the working hours?"

### **Benefits & Employment**
- "What health insurance benefits do I get?"
- "How does visa sponsorship work?"
- "What is the probation period?"
- "Tell me about gratuity payments"

## 🎨 Key Improvements

### **Enhanced User Experience**
- ✅ Fixed HTML formatting issues with proper CSS styling
- ✅ Smart leave detection with clickable buttons
- ✅ Updated branding from "ES Training DMCC" to "LGL HR Assistant"
- ✅ Removed quick reference contact information
- ✅ Improved text formatting and readability

### **Interactive Features**
- 🔘 Clickable leave type buttons for better navigation
- 📊 Real-time leave balance calculations
- 👤 Employee login with personalized responses
- 🎯 Smart keyword matching across 50+ policy terms

## 🔧 Technical Details

### Built With
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Python** - Core programming language

### Key Features
- Responsive design with mobile compatibility
- Session state management for user interactions
- Real-time leave balance calculations
- Professional UI with LGL branding
- Structured response format to prevent HTML display issues

## 📱 Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 🤝 Contributing

To enhance the HR assistant:

1. **Add New Policies**: Update `HANDBOOK_DATA` with new sections
2. **Improve Responses**: Enhance the `process_user_query` function
3. **Add Features**: Implement new employee management capabilities
4. **Update Styling**: Modify CSS for better user experience

## 📄 License

This HR assistant is designed specifically for LGL internal use and employee support operations.

## 🏢 About LGL

LGL is committed to providing excellent HR support and employee services. This intelligent assistant helps employees quickly access company policies and procedures.

**Mission**: To deliver comprehensive HR support through innovative technology solutions.

**Values**: Employee engagement, transparency, efficiency, and continuous improvement.

---

**Built with ❤️ for LGL employees**