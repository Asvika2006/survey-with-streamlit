import streamlit as st
import pandas as pd

# Title and instructions
st.title("Real-Time Polling App")
st.write("Vote for your favorite language and see real-time results!")

# Initialize poll options and votes
poll_options = ["C", "C++", "Python", "HTML"]
if "votes" not in st.session_state:
    st.session_state.votes = {option: 0 for option in poll_options}

# Display poll question
st.subheader("Which option do you prefer?")

# Create radio buttons for user to select an option
selected_option = st.radio("Choose an option:", poll_options)

# Button to submit vote
if st.button("Vote"):
    st.session_state.votes[selected_option] += 1
    st.success(f"Thank you for voting for {selected_option}!")

# Display poll results in real-time
st.subheader("Live Poll Results")
votes_data = pd.DataFrame.from_dict(st.session_state.votes, orient='index', columns=['Votes'])

# Display results as a bar chart
st.bar_chart(votes_data)

# Display raw vote counts
st.write("Current Vote Counts:")
st.write(votes_data)
