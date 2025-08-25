# 🤖 ES Training DMCC HR Assistant

An intelligent AI-powered HR assistant that provides comprehensive support for ES Training DMCC employee handbook queries and HR operations.

## 🌟 Features

### 🎯 **Intelligent HR Support**
- Natural language processing for employee handbook queries
- Smart keyword detection and policy mapping
- Context-aware responses with relevant information
- Comprehensive coverage of all HR policies and procedures

### 💬 **Interactive Interface**
- Modern, responsive design with professional styling
- Real-time chat interface with ES Training branding
- Quick action buttons for common HR topics
- Beautiful gradient backgrounds and smooth animations

### 📚 **Complete Handbook Coverage**
- **Working Hours** (Administrative & Academic staff schedules)
- **Employee Benefits** (Health insurance, Visa sponsorship)
- **Leave Policies** (Annual, Sick, Maternity, Parental, Bereavement)
- **Code of Conduct** (Professional standards, Dress code, Safeguarding)
- **Performance Management** (Appraisals, Probation procedures)
- **Disciplinary Procedures** (Misconduct, Warnings, Appeals)
- **COVID-19 Policy** (Health protocols, Quarantine rules)
- **Termination & Gratuity** (Notice periods, End of service benefits)

### 👥 **Employee Management**
- **Employee Login System** with personalized profiles
- **Leave Balance Tracking** with real-time calculations
- **Personalized Greetings** and employee details display
- **Department-based Access** to relevant policies

## 🚀 Quick Start

### Local Development
```bash
# Clone or download the files to your local machine
cd "HR EMPLOYEE"

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
HR EMPLOYEE/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── .gitignore            # Git ignore file
└── Employee handbook.txt  # Source handbook document
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
- Fallback responses for unmatched queries

## 📋 Sample Queries

### **Leave & Time Off**
- "How many annual leave days do I have left?"
- "What is the sick leave policy?"
- "How do I apply for maternity leave?"
- "When are the working hours?"

### **Policies & Procedures**
- "What is the dress code policy?"
- "Tell me about the disciplinary procedure"
- "How does the performance appraisal work?"
- "What are the COVID-19 protocols?"

### **Benefits & Employment**
- "What health insurance benefits do I get?"
- "How does visa sponsorship work?"
- "What is the probation period?"
- "Tell me about gratuity payments"

## 🎨 Customization

### Company Branding
- Update company name and logo in the header section
- Modify color scheme in the CSS styling
- Add custom company information and contact details

### Employee Data
- Update the `EMPLOYEE_DATA` dictionary with real employee information
- Modify leave calculations based on your specific policies
- Add new employee fields as needed

### Handbook Content
- Edit the `HANDBOOK_DATA` dictionary to reflect your policies
- Add new policy sections and topics
- Update keywords for better query matching

## 🔧 Technical Details

### Built With
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **Python** - Core programming language

### Key Features
- Responsive design with mobile compatibility
- Session state management for user interactions
- Real-time leave balance calculations
- Professional UI with ES Training branding

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

## 📞 Support & Contact

For questions, issues, or feature requests:
- **Company**: ES Training DMCC
- **Location**: 15th Floor, Mazaya Business Avenue, BB1, JLT, Dubai, UAE
- **Purpose**: Internal HR operations and employee support

## 📄 License

This HR assistant is designed specifically for ES Training DMCC internal use and employee support operations.

## 🏢 About ES Training DMCC

ES Training is an international English language training centre based in Dubai, UAE. We provide high-quality English language education to students from around the world, with state-of-the-art facilities and experienced native English-speaking teachers.

**Mission**: To deliver English Language and Business programmes of the highest quality to international students, providing them with the necessary skills for employment and further education.

**Values**: Education with ethics and integrity, innovation through technology, personalized care, employee engagement, and creating a culture of warmth and belonging.

---

**Built with ❤️ for ES Training DMCC employees**