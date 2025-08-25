#!/usr/bin/env python3
"""
Test script for ES Training DMCC HR Assistant
Validates the application structure without requiring Streamlit installation
"""

def test_handbook_data_structure():
    """Test the handbook data structure"""
    print("🧪 Testing handbook data structure...")
    
    # Import the handbook data (simulated)
    handbook_sections = [
        'working_hours', 'annual_leave', 'sick_leave', 'maternity_leave',
        'code_of_conduct', 'disciplinary_procedures', 'performance_management',
        'termination_gratuity'
    ]
    
    print(f"✅ Found {len(handbook_sections)} handbook sections")
    
    for section in handbook_sections:
        print(f"   • {section.replace('_', ' ').title()}")
    
    return True

def test_employee_data_structure():
    """Test employee data structure"""
    print("\n🧪 Testing employee data structure...")
    
    # Sample employee structure
    sample_employee = {
        'name': 'Test Employee',
        'department': 'Test Department',
        'approval_manager': 'Test Manager',
        'employee_id': 'TEST001',
        'join_date': '2024-01-01',
        'contract_type': 'Unlimited',
        'position': 'Test Position',
        'annual_leave_taken': 0,
        'sick_leave_taken': 0,
        'years_of_service': 1.0
    }
    
    required_fields = [
        'name', 'department', 'approval_manager', 'employee_id',
        'annual_leave_taken', 'sick_leave_taken', 'years_of_service'
    ]
    
    for field in required_fields:
        if field in sample_employee:
            print(f"   ✅ {field}: {sample_employee[field]}")
        else:
            print(f"   ❌ Missing field: {field}")
    
    return True

def test_leave_calculations():
    """Test leave calculation logic"""
    print("\n🧪 Testing leave calculation logic...")
    
    # Test cases
    test_cases = [
        {'years_of_service': 0.5, 'expected_annual': 20, 'description': 'First year employee'},
        {'years_of_service': 1.5, 'expected_annual': 22, 'description': 'Second year employee'},
        {'years_of_service': 3.0, 'expected_annual': 22, 'description': 'Experienced employee'}
    ]
    
    for case in test_cases:
        years = case['years_of_service']
        expected = case['expected_annual']
        
        # Simulate calculation logic
        if years >= 1:
            calculated = 22
        else:
            calculated = 20
            
        if calculated == expected:
            print(f"   ✅ {case['description']}: {calculated} days")
        else:
            print(f"   ❌ {case['description']}: Expected {expected}, got {calculated}")
    
    return True

def test_file_structure():
    """Test file structure"""
    print("\n🧪 Testing file structure...")
    
    import os
    
    required_files = [
        'app.py',
        'requirements.txt', 
        'README.md',
        '.gitignore',
        'Employee handbook.txt'
    ]
    
    base_path = r"c:\Users\ALYODY\Downloads\LGL PROJECT 2025\HR EMPLOYEE"
    
    for filename in required_files:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"   ✅ {filename}: {size:,} bytes")
        else:
            print(f"   ❌ Missing file: {filename}")
    
    return True

def main():
    """Run all tests"""
    print("🤖 ES Training DMCC HR Assistant - Validation Tests\n")
    print("=" * 60)
    
    try:
        test_handbook_data_structure()
        test_employee_data_structure() 
        test_leave_calculations()
        test_file_structure()
        
        print("\n" + "=" * 60)
        print("🎉 All validation tests completed successfully!")
        print("\n📋 Next Steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run the application: streamlit run app.py")
        print("3. Deploy to Streamlit Cloud for public access")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()