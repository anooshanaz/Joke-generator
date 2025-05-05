import streamlit as st
import requests

# Fetch joke from the API
def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get('https://official-joke-api.appspot.com/jokes/random')
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch the joke, try again later!"
    except Exception:
        return "Why did the programmer quit his job? \n\n Because he did not get arrays!"

# UI part
def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to get a random joke")

    if st.button("Get a joke"):
        joke = get_random_joke()
        st.success(joke)  # Moved inside the if block

    # Add a horizontal line
    st.markdown("---")

    # Footer using HTML
    st.markdown(
        """
        <div style="text-align:center;">
            <p>Joke from official API</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Ensure script runs properly
if __name__ == "__main__":
    main()
