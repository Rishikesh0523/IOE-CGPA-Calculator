import streamlit as st
import json

def load_semesters():
    try:
        with open('semesters.json', 'r') as file:
            semesters = json.load(file)
        return semesters
    except FileNotFoundError:
        st.error("Error: semesters.json file not found.")
        return {}
    except json.JSONDecodeError:
        st.error("Error: Invalid JSON in semesters.json file.")
        return {}

def calculate_grade_point(marks, full_marks):
    if marks/full_marks >= 0.8:
        return 4.0
    elif marks/full_marks >= 0.75:
        return 3.7
    elif marks/full_marks >= 0.70:
        return 3.3
    elif marks/full_marks >= 0.65:
        return 3.0
    elif marks/full_marks >= 0.60:
        return 2.7
    elif marks/full_marks >= 0.55:
        return 2.3
    elif marks/full_marks >= 0.50:
        return 2.0
    elif marks/full_marks >= 0.45:
        return 1.7
    else:
        return 1.0

def calculate_gpa(marks_list, credit_hours, full_marks_list):
    total_points = sum(calculate_grade_point(marks, full_marks) * credit for marks, credit, full_marks in zip(marks_list, credit_hours, full_marks_list))
    total_credits = sum(credit_hours)
    return total_points / total_credits if total_credits != 0 else 0

st.set_page_config(page_title="IOE BCT CGPA Calculator", page_icon=":chart_with_upwards_trend:", layout="wide")

# Custom CSS to reduce input field padding
st.markdown("""
<style>
    .stNumberInput>div>div>input {
        padding: 0.2rem 0.4rem;
    }
    .stNumberInput>div>div>div {
        padding: 0.1rem 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("IOE BCT CGPA Calculator")

semesters = load_semesters()

selected_semester = st.selectbox("Select the semester to calculate CGPA up to:", list(semesters.keys()))

all_marks = []
full_marks = []
all_credits = []

for sem, subjects in semesters.items():
    if sem > selected_semester:
        break
    
    st.header(f"Year: {sem.split('/')[0]}, Semester: {sem.split('/')[1]}")

    for subject in subjects:
        st.subheader(f"{subject['title']} ({subject['code']})")
        
        col1, col2, col3, col4, col5 = st.columns([2,2,2,2,1], gap="small")

        with col1:
            theory_ass = st.number_input(
                "Theory Ass", min_value=0, max_value=subject['theory_ass'] or 0, 
                key=f"{sem}_{subject['code']}_theory_ass") if subject['theory_ass'] is not None else None

        with col2:
            theory_final = st.number_input(
                "Theory Final", min_value=0, max_value=subject['theory_final'] or 0, 
                key=f"{sem}_{subject['code']}_theory_final") if subject['theory_final'] is not None else None

        with col3:
            practical_ass = st.number_input(
                "Practical Ass", min_value=0, max_value=subject['practical_ass'] or 0, 
                key=f"{sem}_{subject['code']}_practical_ass") if subject['practical_ass'] is not None else None

        with col4:
            practical_final = st.number_input(
                "Practical Final", min_value=0, max_value=subject['practical_final'] or 0, 
                key=f"{sem}_{subject['code']}_practical_final") if subject['practical_final'] is not None else None

        total_marks = sum(filter(None, [theory_ass, theory_final, practical_ass, practical_final]))
        full_marks.append(sum(filter(None, [subject['theory_ass'], subject['theory_final'], subject['practical_ass'], subject['practical_final']])))
        all_marks.append(total_marks)
        all_credits.append(subject['credits'])

        with col5:
            st.metric("Total", total_marks)

    st.divider()

cgpa = calculate_gpa(all_marks, all_credits, full_marks)
st.write(f"CGPA up to Semester {selected_semester}: {cgpa:.3f}")