import streamlit as st
import requests
import urllib.parse

def main():
    st.title("Email Outreach Message Generator")
    st.write("Generate personalized outreach messages")
    
    # Create form for input parameters
    with st.form("outreach_form"):
        st.subheader("Required Parameters")
        
        # Required fields
        sender_email = st.text_input("Sender Email", placeholder="sender@example.com")
        recipient_email = st.text_input("Recipient Email", placeholder="recipient@example.com")
        candidate_name = st.text_input("Candidate Name", placeholder="John Doe")
        current_role = st.text_input("Current Role", placeholder="Software Engineer")
        current_company = st.text_input("Current Company", placeholder="Tech Corp")
        company_name = st.text_input("Target Company Name", placeholder="Target Corp")
        role = st.text_input("Target Role", placeholder="Senior Software Engineer")
        recruiter_name = st.text_input("Recruiter Name", placeholder="Jane Smith")
        organisation = st.text_input("Organisation", placeholder="HR Department")
        message_type = st.selectbox("Message Type", ["outreach", "follow_up", "thank_you"])
        
        st.subheader("Optional Parameters")
        
        # Optional fields
        job_evaluation = st.text_area("Job Evaluation (Optional)", placeholder="Enter job evaluation details...")
        reply_to_email = st.text_input("Reply To Email (Optional)", placeholder="reply@example.com")
        send_email = st.checkbox("Send Email (Optional)", value=False)
        past_conversation = st.text_area("Past Conversation (Optional)", placeholder="Enter past conversation details...")
        
        # Submit button
        submit_button = st.form_submit_button("Generate Message")
        
        if submit_button:
            # Validate required fields
            required_fields = {
                "sender_email": sender_email,
                "recipient_email": recipient_email,
                "candidate_name": candidate_name,
                "current_role": current_role,
                "current_company": current_company,
                "company_name": company_name,
                "role": role,
                "recruiter_name": recruiter_name,
                "organisation": organisation,
                "message_type": message_type
            }
            
            # Check if any required field is empty
            empty_fields = [field for field, value in required_fields.items() if not value.strip()]
            
            if empty_fields:
                st.error(f"Please fill in all required fields: {', '.join(empty_fields)}")
                return
            
            # Prepare API request
            api_url = "https://ak0601-outreach-api.hf.space/generate-message"
            
            # Build query parameters
            params = {
                "sender_email": sender_email,
                "recipient_email": recipient_email,
                "candidate_name": candidate_name,
                "current_role": current_role,
                "current_company": current_company,
                "company_name": company_name,
                "role": role,
                "recruiter_name": recruiter_name,
                "organisation": organisation,
                "message_type": message_type
            }
            
            # Add optional parameters if provided
            if job_evaluation.strip():
                params["job_evaluation"] = job_evaluation
            if reply_to_email.strip():
                params["reply_to_email"] = reply_to_email
            if send_email:
                params["send_email"] = str(send_email).lower()
            if past_conversation.strip():
                params["past_conversation"] = past_conversation
            
            # Headers
            headers = {
                "accept": "application/json",
                "X-API-Key": "Synapse@2025"
            }
            
            try:
                with st.spinner("Generating message..."):
                    response = requests.post(api_url, params=params, headers=headers)
                
                if response.status_code == 200:
                    st.success("Message generated successfully!")
                    
                    # Display the response
                    try:
                        result = response.json()
                        
                        # Display success status
                        if result.get("success"):
                            st.success("✅ Message generated successfully!")
                        else:
                            st.warning("⚠️ Message generated but with warnings")
                        
                        # Display email subject if available
                        if "email_subject" in result and result["email_subject"]:
                            st.subheader("📧 Email Subject")
                            st.info(result["email_subject"])
                        
                        # Display message content if available
                        if "message" in result and result["message"]:
                            st.subheader("💬 Message Content")
                            st.text_area("Generated Message", result["message"], height=200, disabled=True)
                        
                        # Display email sent status
                        if "email_sent" in result:
                            email_status = "✅ Email Sent" if result["email_sent"] else "📧 Email Not Sent (Preview Mode)"
                            st.info(email_status)
                        
                        # Display any errors
                        if "error" in result and result["error"]:
                            st.error(f"Error: {result['error']}")
                        
                        # Show full JSON response in expandable section
                        with st.expander("📋 Full API Response"):
                            st.json(result)
                        
                    except Exception as e:
                        st.error(f"Error parsing response: {str(e)}")
                        st.write("Raw response:")
                        st.text(response.text)
                        
                else:
                    st.error(f"API request failed with status code: {response.status_code}")
                    st.write("Response:")
                    st.text(response.text)
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Error making API request: {str(e)}")
    
    # Display API information
    with st.expander("API Information"):
        st.write("""
        **API Endpoint:** https://ak0601-outreach-api.hf.space/generate-message
        
        **Method:** POST
        
        **Required Parameters:**
        - sender_email
        - recipient_email
        - candidate_name
        - current_role
        - current_company
        - company_name
        - role
        - recruiter_name
        - organisation
        - message_type
        
        **Optional Parameters:**
        - job_evaluation
        - reply_to_email
        - send_email
        - past_conversation
        """)

if __name__ == "__main__":
    main() 