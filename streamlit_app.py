import streamlit as st
import requests
from src.common.settings import config

EMAILER_URL = config.emailer_url

st.title("📧 Emailer Application")

st.write("Fill the form to send an email")

receiver = st.text_input("Receiver Email")
subject = st.text_input("Subject")
body = st.text_area("Message")
# file = st.file_uploader("Attachment (optional)", type=["pdf", "png", "jpg", "txt"])

if st.button("Send Email"):
    if not receiver or not subject or not body:
        st.error("All fields except attachment are required.")
    else:
        # files = {}
        # if file:
        #     files = {"file": (file.name, file, file.type)}

        response = requests.post(
            f"{EMAILER_URL}/v1/emailer/email",
            params={"email": receiver, "subject": subject, "body": body},
            # files=files
        )

        if response.status_code == 200:
            st.success("Email sent successfully!")
        else:
            st.error(f"Failed: {response.text}")
