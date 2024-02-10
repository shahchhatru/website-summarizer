import gradio as gr
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Google API key and model
GOOGLE_API_KEY = "AIzaSyDupxjjNLXwy9bHrzhzGN28ujpWAQ1Z76k"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-pro')

def summarize_webpage(message, history):
    url = message  # Assuming the user enters a URL directly
    # Initialize the Chrome webdriver
    driver = webdriver.Chrome()
    # Open the URL in the webdriver
    driver.get(url)
    # Wait for the page to load completely
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # Extract all the information from the website
    all_text = driver.find_element(By.TAG_NAME, "body").text
    # Close the webdriver
    driver.quit()
    # Summarize the text
    prompt = f"Summarize Given text: {all_text} in about 200 words"
    response = model.generate_content(prompt)
    summarized_text = response.candidates[0].content.parts[0].text
    return summarized_text

# Custom theme with monospace font
custom_theme = gr.themes.Default(font=["Courier New", "Arial", "sans-serif"])

# Create a Gradio interface with a chat-like appearance and custom theme
chat_interface = gr.ChatInterface(
    summarize_webpage,
    chatbot=gr.Chatbot(height=400),
    textbox=gr.Textbox(placeholder="Enter the URL of the webpage", container=False, scale=5),
    title="Webpage Summarizer",
    theme=custom_theme,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
)

# Launch the Gradio interface
chat_interface.launch()
