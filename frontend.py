import streamlit as st
import requests

def generate_report_request(player_data):
    try:
        response = requests.post("http://127.0.0.1:5000/generate", json={"player_data": player_data})
        if response.status_code != 200:
            return {"error": f"Error: {response.status_code} - {response.text}"}
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

def main():
    st.title("NFL Scouting Report Generator")
    player_data = st.text_area("Enter player attributes:", "")
    if st.button("Generate Report"):
        response = generate_report_request(player_data)
        if "error" in response:
            st.error(response["error"])
        else:
            st.write(response.get("Generated NFL Scouting Report", "No report generated"))

if __name__ == "__main__":
    main()
