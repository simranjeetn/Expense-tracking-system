import streamlit as st
from datetime import datetime
import requests


API_URL = "http://localhost:8000"

def add_update_tab():
    selected_dt = st.date_input("Select Date", datetime(2024, 8, 1), label_visibility="collapsed")

    res = requests.get(f"{API_URL}/expenses/{selected_dt}")
    if res.status_code == 200:
        existing_expenses = res.json()
    # st.write(expenses)
    else:
        st.write("No expenses found")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Transport", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns([1, 1, 2])

            with col1:
                amount_input = st.number_input(label="Amount", min_value=0.0, value=amount, step=1.0, key=f"amount_{i}",
                                               label_visibility="collapsed")
            with col2:
                category_input = st.selectbox("Category", options=categories, index=categories.index(category),
                                              key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input("Notes", key=f"notes_{i}", value=notes, label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            response = requests.post(f"{API_URL}/expenses/{selected_dt}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error("Failed to update expenses.")