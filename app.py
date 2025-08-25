import streamlit as st
import re
import time
import random
import pandas as pd
from datetime import datetime, date, timedelta
import urllib.parse
import json

# Configure the page
st.set_page_config(
    page_title="LGL HR Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS styling with improved formatting
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, rgb(52, 152, 219) 0%, rgb(41, 128, 185) 100%) !important;
        padding: 2rem;
        border-radius: 15px;
        color: white !important;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
    }
    
    .main-header h1 {
        color: white !important;
        font-size: 2.5rem !important;
        margin: 0 !important;
    }
    
    .main-header p {
        color: white !important;
        opacity: 0.9 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, rgb(52, 152, 219) 0%, rgb(41, 128, 185) 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        height: 70px !important;
        box-shadow: 0 3px 10px rgba(52, 152, 219, 0.3) !important;
        transition: all 0.3s ease !important;
        text-align: center !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, rgb(41, 128, 185) 0%, rgb(31, 78, 121) 100%) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4) !important;
    }
    
    .bot-message {
        background: rgb(248, 249, 250) !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        border-left: 4px solid rgb(52, 152, 219) !important;
        margin: 1rem 0 !important;
        color: rgb(44, 62, 80) !important;
        box-shadow: 0 2px 8px rgba(52, 152, 219, 0.1) !important;
        line-height: 1.6 !important;
    }
    
    .bot-message h2, .bot-message h3 {
        color: rgb(52, 152, 219) !important;
        margin-top: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    .bot-message ul {
        margin: 0.5rem 0 !important;
        padding-left: 1.5rem !important;
    }
    
    .bot-message li {
        margin-bottom: 0.3rem !important;
    }
    
    .user-message {
        background: linear-gradient(135deg, rgb(52, 152, 219), rgb(41, 128, 185)) !important;
        color: white !important;
        padding: 1.5rem !important;
        border-radius: 12px !important;
        margin: 1rem 0 !important;
        text-align: right !important;
    }
    
    .footer {
        background-color: rgb(248, 249, 250);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 3rem;
        text-align: center;
        border: 1px solid rgb(226, 232, 240);
    }
</style>
""", unsafe_allow_html=True)

# Employee Database - Sample Data for Leave Tracking
EMPLOYEE_DATA = {
    'john_doe': {
        'name': 'John Doe',
        'department': 'Academic Staff',
        'approval_manager': 'HR Manager',
        'employee_id': 'EMP001',
        'join_date': '2023-01-15',
        'contract_type': 'Unlimited',
        'position': 'English Teacher',
        'annual_leave_taken': 8,
        'sick_leave_taken': 2,
        'maternity_leave_taken': 0,
        'parental_leave_taken': 0,
        'bereavement_leave_taken': 0,
        'probation_completed': True,
        'years_of_service': 1.8
    },
    'sarah_smith': {
        'name': 'Sarah Smith',
        'department': 'Administration',
        'approval_manager': 'HR Manager',
        'employee_id': 'EMP002',
        'join_date': '2022-08-10',
        'contract_type': 'Unlimited',
        'position': 'Administrative Assistant',
        'annual_leave_taken': 12,
        'sick_leave_taken': 3,
        'maternity_leave_taken': 0,
        'parental_leave_taken': 0,
        'bereavement_leave_taken': 0,
        'probation_completed': True,
        'years_of_service': 2.3
    },
    'ahmed_hassan': {
        'name': 'Ahmed Hassan',
        'department': 'Academic Staff',
        'approval_manager': 'Academic Director',
        'employee_id': 'EMP003',
        'join_date': '2024-01-20',
        'contract_type': 'Limited',
        'position': 'Academic Coordinator',
        'annual_leave_taken': 5,
        'sick_leave_taken': 1,
        'maternity_leave_taken': 0,
        'parental_leave_taken': 0,
        'bereavement_leave_taken': 0,
        'probation_completed': True,
        'years_of_service': 0.7
    }
}

# Comprehensive LGL Handbook Data
HANDBOOK_DATA = {
    'working_hours': {
        'title': 'Working Hours',
        'content': """
**Administrative Staff:**
• Working Days: Monday – Friday
• Working Hours: 9:00am – 6:00pm

**Academic Staff:**
• Minimum 2 teaching sessions per day
• Sessions: 9:00am-12:00pm, 12:00pm-3:00pm, 3:00pm-6:00pm
• Working days: Monday to Friday

**Overtime:**
• Paid according to confirmed attendance
• At management's discretion

**Ramadan Hours:**
• Reduced by 2 hours per day for administrative staff
• One week notice for revised working times
        """,
        'keywords': ['working hours', 'schedule', 'time', 'overtime', 'ramadan', 'shift', 'administrative', 'academic']
    },
    'annual_leave': {
        'title': 'Annual Leave Policy',
        'content': """
**Annual Leave Entitlement:**
• First Year: 20 working days (after probation)
• Subsequent Years: 22 working days
• Notice Required: Minimum twice the duration requested

**Application Process:**
• Submit Annual Leave Form to line manager
• First-come, first-served basis
• Subject to operational requirements

**Carrying Over Leave:**
• Maximum 7 days for administrative staff
• Teaching staff cannot carry over leave

**Peak Periods:**
• Limited leave during July and August
• 4 weeks notice for restricted periods
        """,
        'keywords': ['annual leave', 'vacation', 'holiday', 'time off', 'leave policy', 'probation']
    },
    'sick_leave': {
        'title': 'Sick Leave Policy',
        'content': """
**Sick Leave Entitlement:**
• Total: 90 calendar days per year (after 3 months post-probation)
• Full Pay: First 15 days
• Half Pay: Next 30 days
• No Pay: Final 45 days

**Application Process:**
• Notify line manager and HR within 1.5 hours (academic) / 1 hour (admin)
• Medical certificate required after 2 days
• Complete Sick Leave Form upon return

**Coverage Includes:**
• Illness recovery
• Medical procedures/surgery
• Severe injury recovery
• COVID-19 quarantine/isolation
        """,
        'keywords': ['sick leave', 'illness', 'medical', 'health', 'doctor', 'certificate', 'absence']
    },
    'maternity_leave': {
        'title': 'Maternity & Parental Leave',
        'content': """
**Maternity Leave Entitlement:**
• Total: 60 days maternity leave
• Full Pay: First 45 consecutive calendar days
• Half Pay: Following 15 days
• Written notice: 15 weeks before due date

**Extended Maternity Leave:**
• Additional 100 days without pay (consecutive or non-consecutive)
• Medical certificate required for illness-related extensions

**Parental Leave:**
• Female employees: Additional 5 days within 6 months of birth
• Male employees: 5 days within 6 months of birth

**Feeding Breaks:**
• Two 30-minute breaks daily for 18 months post-delivery
• Considered part of working hours
        """,
        'keywords': ['maternity leave', 'parental leave', 'pregnancy', 'birth', 'feeding breaks', 'family']
    },
    'bereavement_leave': {
        'title': 'Bereavement / Compassionate Leave',
        'content': """
**Bereavement Leave Entitlement:**
• Five (5) paid days for the death of a spouse
• Three (3) paid days for the death of a parent, child, sibling, grandchild, or grandparent

**Application Process:**
• Notify reporting line manager as soon as possible
• Latest notification: first day of absence
• Exceptional circumstances: applications considered after first day at management discretion

**Support Available:**
• Regular progress discussions with line manager during leave and upon return
• Confidential discussions with HR Manager about grieving process impact on work performance
• Time off for dependents available for emergencies involving family members

**Coverage:**
• Spouse death: 5 paid days
• Immediate family death: 3 paid days
• Emergency dependent care: Reasonable unpaid leave
        """,
        'keywords': ['bereavement', 'compassionate', 'death', 'family', 'grief', 'emergency', 'dependent']
    },
    'code_of_conduct': {
        'title': 'Code of Conduct',
        'content': """
**Employee Duties:**
• Exercise reasonable skill and care
• Obey rules, policies, and work directions
• Care for company property and facilities
• Maintain confidentiality of trade secrets
• Act in good faith and maintain trust

**Dress Code:**
• Smart, professional attire required
• No torn, dirty, or inappropriate clothing
• No transparent clothing or low necklines
• No shorts or flip-flops
• Tattoos and piercings should be covered where possible

**Safeguarding Standards:**
• No physical contact with students
• Avoid being alone with students
• Maintain professional boundaries
• No personal relationships with students
• Report safeguarding concerns immediately
        """,
        'keywords': ['conduct', 'dress code', 'safeguarding', 'professional', 'behavior', 'standards']
    },
    'disciplinary_procedures': {
        'title': 'Disciplinary Procedures',
        'content': """
**Minor Misconduct Examples:**
• Persistent lateness and poor timekeeping
• Unauthorized absence without valid reason
• Failure to follow prescribed procedures
• Incompetence or failure to meet standards

**Gross Misconduct Examples:**
• Theft or unauthorized possession of company property
• Being unfit for duty due to alcohol/drug use
• Physical assault or verbal abuse
• Breach of confidentiality procedures
• Unlawful discrimination or harassment

**Warning Validity Periods:**
• Verbal Warnings: 6 months
• First Written Warnings: 12 months
• Final Written Warnings: 12 months

**Appeal Rights:**
• 5 days to submit written appeal
• Appeal meeting within 20 working days
        """,
        'keywords': ['disciplinary', 'misconduct', 'warnings', 'dismissal', 'appeals', 'procedures']
    },
    'performance_management': {
        'title': 'Performance Management',
        'content': """
**Performance Appraisal Process:**
• First appraisal after 6-month probation
• Annual formal reviews thereafter
• Optional 6-month mid-year reviews

**Appraisal Components:**
• Review of previous year's achievements
• Personal Development Plan for coming year
• Training needs identification
• Career planning discussions

**Probationary Period:**
• Duration: 6 months for all new staff
• Performance monitoring throughout
• Review meeting at completion
• Possible 3-month extension if needed

**Key Principles:**
• Fair and equitable process
• Confidential discussions
• Two-way communication
• Focus on development and improvement
        """,
        'keywords': ['performance', 'appraisal', 'review', 'probation', 'development', 'evaluation']
    },
    'termination_gratuity': {
        'title': 'Termination & Gratuity',
        'content': """
**Notice Periods:**
• Unlimited contracts: 30 calendar days minimum
• Limited contracts: No notice required at natural expiry

**Gratuity Calculations:**
**Years 1-5:** 21 calendar days' basic pay per year
**Year 6+:** 30 calendar days' basic pay per year
• Maximum total: 2 years' pay equivalent

**Limited Contract Resignation:**
• Under 5 years: No gratuity entitlement
• Over 5 years: Same as unlimited contract

**Early Termination Compensation:**
• Employer termination: 3 months' remuneration minimum
• Employee termination: Half of 3 months' remuneration

**Exit Process:**
• Exit interviews conducted
• Return of company property
• Final settlement processing
        """,
        'keywords': ['termination', 'resignation', 'gratuity', 'notice period', 'compensation', 'exit']
    }
}

def calculate_leave_entitlements(employee_data):
    """Calculate leave entitlements based on employee data and handbook policies"""
    years_of_service = employee_data['years_of_service']
    probation_completed = employee_data['probation_completed']
    
    # Annual Leave Calculation
    if years_of_service >= 1:
        annual_leave_entitlement = 22
    else:
        annual_leave_entitlement = 20
    
    # Sick Leave Calculation
    if probation_completed:
        sick_leave_entitlement = 90
    else:
        sick_leave_entitlement = 0
    
    return {
        'annual_leave': {
            'entitlement': annual_leave_entitlement,
            'taken': employee_data['annual_leave_taken'],
            'remaining': annual_leave_entitlement - employee_data['annual_leave_taken']
        },
        'sick_leave': {
            'entitlement': sick_leave_entitlement,
            'taken': employee_data['sick_leave_taken'],
            'remaining': sick_leave_entitlement - employee_data['sick_leave_taken']
        }
    }

def process_user_query(query):
    """Process user query and return appropriate response with smart leave detection"""
    query_lower = query.lower()
    
    # Smart leave type detection - show options when user types general terms
    leave_triggers = ['leave', 'time off', 'absence', 'vacation', 'holiday']
    if any(trigger in query_lower for trigger in leave_triggers) and not any(specific in query_lower for specific in ['annual', 'sick', 'maternity', 'parental', 'bereavement']):
        return {
            'type': 'leave_options',
            'content': "🏖️ **Which type of leave are you asking about?**\n\nPlease select from the options below:"
        }
    
    # Leave balance queries
    if any(word in query_lower for word in ['balance', 'remaining', 'left', 'how many']):
        if st.session_state.get('current_employee'):
            emp_data = st.session_state.employee_data
            leave_data = calculate_leave_entitlements(emp_data)
            return {
                'type': 'text',
                'content': f"""
📊 **Your Current Leave Balances:**

**Annual Leave:** {leave_data['annual_leave']['remaining']} days remaining
• Entitlement: {leave_data['annual_leave']['entitlement']} days
• Used: {leave_data['annual_leave']['taken']} days

**Sick Leave:** {leave_data['sick_leave']['remaining']} days remaining  
• Entitlement: {leave_data['sick_leave']['entitlement']} days
• Used: {leave_data['sick_leave']['taken']} days

💡 **Need to apply for leave?** Ask me "How do I apply for annual leave?" for the application process.
"""
            }
        else:
            return {
                'type': 'text',
                'content': "Please select your employee profile from the sidebar to view your leave balances."
            }
    
    # Specific policy queries
    if any(word in query_lower for word in ['apply', 'application', 'request', 'form']):
        if any(word in query_lower for word in ['leave', 'vacation', 'holiday']):
            return {
                'type': 'text',
                'content': """
📋 **How to Apply for Leave:**

**Step 1:** Submit Annual Leave Form to your line manager
**Step 2:** Provide minimum notice (twice the duration requested)
**Step 3:** Wait for approval based on operational requirements

**Example:** For 1 week leave, submit request 2 weeks in advance

**Peak Restrictions:** Limited availability during July-August (4 weeks notice given)
**Processing:** First-come, first-served basis

📞 **Need the form?** Contact HR Department or your line manager
"""
            }
    
    # Find best matching topic
    best_match = None
    best_score = 0
    
    for topic_key, topic_data in HANDBOOK_DATA.items():
        score = 0
        for keyword in topic_data['keywords']:
            if keyword in query_lower:
                score += 1
        
        if score > best_score:
            best_score = score
            best_match = topic_data
    
    if best_match:
        return {
            'type': 'text',
            'content': f"## {best_match['title']}\n{best_match['content']}"
        }
    
    return {
        'type': 'text',
        'content': """
I'm here to help with LGL HR policies! You can ask me about:

🕒 **Working Hours** - Schedule, overtime, Ramadan hours
🏖️ **Annual Leave** - Entitlements, application process  
🏥 **Sick Leave** - Medical leave policies
👶 **Maternity/Parental Leave** - Family leave policies
📋 **Code of Conduct** - Professional standards, dress code
🎯 **Performance Management** - Appraisals and reviews
⚖️ **Disciplinary Procedures** - Warnings, misconduct, appeals
🏁 **Termination & Gratuity** - Notice periods, end-of-service benefits

**Quick Commands:**
• "My leave balance" - Check your remaining days
• "How do I apply for leave?" - Application process
• "What is the dress code?" - Professional standards
• "Disciplinary procedure" - Misconduct and warnings

**Try typing:** "leave" to see all leave options!
"""
    }

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'show_leave_options' not in st.session_state:
    st.session_state.show_leave_options = False

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 LGL HR Assistant</h1>
    <p>Your intelligent guide to company policies and procedures</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for employee selection
st.sidebar.title("👤 Employee Login")
employee_options = ['Select Employee'] + [emp_data['name'] for emp_data in EMPLOYEE_DATA.values()]
selected_employee = st.sidebar.selectbox("Choose your profile:", employee_options)

if selected_employee != 'Select Employee':
    # Find employee data
    employee_key = None
    for key, data in EMPLOYEE_DATA.items():
        if data['name'] == selected_employee:
            employee_key = key
            break
    
    if employee_key:
        st.session_state.current_employee = selected_employee
        st.session_state.employee_data = EMPLOYEE_DATA[employee_key]
        
        # Show employee info in sidebar
        emp_data = st.session_state.employee_data
        st.sidebar.markdown("---")
        st.sidebar.markdown(f"**👋 Welcome, {emp_data['name']}!**")
        st.sidebar.markdown(f"""
        **📋 Your Details:**
        • Department: {emp_data['department']}
        • Position: {emp_data['position']}
        • Employee ID: {emp_data['employee_id']}
        • Years of Service: {emp_data['years_of_service']} years
        """)
        
        # Quick leave balance
        leave_data = calculate_leave_entitlements(emp_data)
        st.sidebar.markdown(f"""
        **📅 Quick Leave Balance:**
        • Annual: {leave_data['annual_leave']['remaining']} days
        • Sick: {leave_data['sick_leave']['remaining']} days
        """)

# Main content area
st.markdown("### 🚀 Quick Topics:")

topic_cols = st.columns(3)
with topic_cols[0]:
    if st.button("🕒 Working Hours"):
        response = process_user_query("working hours")
        st.session_state.messages.append({"role": "user", "content": "Working Hours"})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

with topic_cols[1]:
    if st.button("🏖️ Annual Leave"):
        response = process_user_query("annual leave")
        st.session_state.messages.append({"role": "user", "content": "Annual Leave"})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

with topic_cols[2]:
    if st.button("🏥 Sick Leave"):
        response = process_user_query("sick leave")
        st.session_state.messages.append({"role": "user", "content": "Sick Leave"})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# Chat Interface
st.markdown("---")
st.markdown("### 💬 Ask me anything about HR policies:")

# Display chat messages
for i, message in enumerate(st.session_state.messages):
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        # Handle different response types
        if isinstance(message["content"], dict):
            if message["content"]["type"] == "leave_options":
                st.markdown(f'<div class="bot-message">{message["content"]["content"]}</div>', unsafe_allow_html=True)
                
                # Display leave type buttons
                leave_cols = st.columns(2)
                with leave_cols[0]:
                    if st.button("🏖️ Annual Leave", key=f"annual_{i}"):
                        response = process_user_query("annual leave")
                        st.session_state.messages.append({"role": "user", "content": "Annual Leave"})
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.rerun()
                    
                    if st.button("👶 Maternity Leave", key=f"maternity_{i}"):
                        response = process_user_query("maternity leave")
                        st.session_state.messages.append({"role": "user", "content": "Maternity Leave"})
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.rerun()
                
                with leave_cols[1]:
                    if st.button("🏥 Sick Leave", key=f"sick_{i}"):
                        response = process_user_query("sick leave")
                        st.session_state.messages.append({"role": "user", "content": "Sick Leave"})
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.rerun()
                    
                    if st.button("🍼 Bereavement Leave", key=f"bereavement_{i}"):
                        response = process_user_query("bereavement leave")
                        st.session_state.messages.append({"role": "user", "content": "Bereavement Leave"})
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.rerun()
            else:
                st.markdown(f'<div class="bot-message">{message["content"]["content"]}</div>', unsafe_allow_html=True)
        else:
            # Handle string responses (backward compatibility)
            st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)

# Chat input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question here:", placeholder="e.g., leave, annual leave balance, or dress code")
    submitted = st.form_submit_button("Send")
    
    if submitted and user_input:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Generate response
        response = process_user_query(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        st.rerun()

# Footer
st.markdown("""
<div class="footer">
    <strong>LGL HR Assistant</strong><br>
    Helping employees navigate company policies with ease<br>
    <small>Your intelligent guide to HR policies and procedures</small>
</div>
""", unsafe_allow_html=True)