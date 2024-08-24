import streamlit as st
import json

def load_semesters():
    try:
        with open('semesters.json', 'r') as file:
            semesters = json.load(file)
        return semesters
    except FileNotFoundError:
        print("Error: semesters.json file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON in semesters.json file.")
        return {}

# Function to calculate grade points based on marks
def calculate_grade_point(marks):
    if marks >= 80:
        return 4.0
    elif marks >= 75:
        return 3.7
    elif marks >= 70:
        return 3.3
    elif marks >= 65:
        return 3.0
    elif marks >= 60:
        return 2.7
    elif marks >= 55:
        return 2.3
    elif marks >= 50:
        return 2.0
    elif marks >= 45:
        return 1.7
    else:
        return 1.0

# Function to calculate GPA for a semester
def calculate_gpa(marks_list, credit_hours):
    total_points = sum(calculate_grade_point(marks) * credit for marks, credit in zip(marks_list, credit_hours))
    total_credits = sum(credit_hours)
    return total_points / total_credits if total_credits != 0 else 0

# Streamlit interface
st.title("CGPA Calculator")

# Define the subjects structure for each semester
semesters = load_semesters()

# Select the semester to calculate up to
selected_semester = st.selectbox("Select the semester to calculate CGPA up to:", list(semesters.keys()))

# Initialize marks and credit lists
all_marks = []
all_credits = []

# Loop through the selected semesters
for sem, subjects in semesters.items():
    if sem > selected_semester:
        break
    
    st.header(f"Year: {sem.split('/')[0]}, Semester: {sem.split('/')[1]}")

    for subject in subjects:
        st.subheader(f"{subject['title']} ({subject['code']})")
        
        # Create a table-like structure for input
        columns = st.columns(5)
        with columns[0]:
            st.write("Theory Ass")
        with columns[1]:
            st.write("Theory Final")
        with columns[2]:
            st.write("Practical Ass")
        with columns[3]:
            st.write("Practical Final")
        with columns[4]:
            st.write("Total")
        
        # Row for input
        with columns[0]:
            theory_ass = st.number_input(
                "", min_value=0, max_value=subject['theory_ass'], 
                key=f"{sem}_{subject['code']}_theory_ass") if subject['theory_ass'] is not None else st.write(" ")
        with columns[1]:
            theory_final = st.number_input(
                "", min_value=0, max_value=subject['theory_final'], 
                key=f"{sem}_{subject['code']}_theory_final") if subject['theory_final'] is not None else st.write(" ")
        with columns[2]:
            practical_ass = st.number_input(
                "", min_value=0, max_value=subject['practical_ass'], 
                key=f"{sem}_{subject['code']}_practical_ass") if subject['practical_ass'] is not None else st.write("")
        with columns[3]:
            practical_final = st.number_input(
                "", min_value=0, max_value=subject['practical_final'], 
                key=f"{sem}_{subject['code']}_practical_final") if subject['practical_final'] is not None else st.write(" ")
        
        # Calculate and display the total marks for this subject
        total_marks = sum(filter(None, [theory_ass, theory_final, practical_ass, practical_final]))
        all_marks.append(total_marks)
        all_credits.append(subject['credits'])
        with columns[4]:
            st.write(total_marks)
    st.divider()

# Calculate CGPA up to the selected semester
cgpa = calculate_gpa(all_marks, all_credits)
st.write(f"CGPA up to Semester {selected_semester}: {cgpa:.2f}")
