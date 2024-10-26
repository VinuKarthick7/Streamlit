import streamlit as st
st.title("GRADE CALCULATOR")
marks = []
for i in range(1, 4):
    mark = st.number_input(f"Enter mark for subject {i}:", min_value=0, max_value=100)
    marks.append(mark)
if st.button("Calculate Grade"):
    if all(mark >= 0 for mark in marks):
        
        # Calculate average
        average = sum(marks) / len(marks)

        
        # Determine grade based on average
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"
        st.write(f"### Average: {average:.2f}")
        st.write(f"### Grade: {grade}")
    else:
        st.write("Please enter valid marks for all subjects.")