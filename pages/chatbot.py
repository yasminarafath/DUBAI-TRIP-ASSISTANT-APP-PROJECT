from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()

initial_message = [
        {"role": "system", "content": "You are a trip planner to Dubai.You are expert in Dubai culture and tourism,locations,food,events,accomodations,etc. You are able to guide the users to plan their vacation to Dubai.You should respond them professionally.Your name is DubaiAI Guide,short name is DG.Response shouldn't exceed 200 words. Suggest the user most attractive and famous tourist places in Dubai.Always ask questions to user and help to plan the trip at it's best .Finally  give the user a day wise itinerary.respond to the user professionally."},
        {
            "role": "assistant",
            "content": "Hello Iam DubaiAI Guide, your expert trip planner.How can I help you?"
        }

]

#func to get response from OPENAI LLM
def get_response_from_llm(messages):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = messages
    )

    return completion.choices[0].message.content
#---------------------

#To initialize with initial_message
if "messages" not in st.session_state:
    st.session_state.messages = initial_message


st.title("DUBAI TRIP ASSISTANT APP")

#Display prev chat content i UI
for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


user_message = st.chat_input("Enter your message")
if user_message:
    new_message = {
              "role":"user",
              "content":user_message
        }
    st.session_state.messages.append(new_message)
    with st. chat_message(new_message["role"]):
          st.markdown(new_message["content"])

    response= get_response_from_llm(st.session_state.messages)
    if response:
        response_message={
            "role":"assistant",
            "content":response
        }
        st.session_state.messages.append(response_message)
        with st. chat_message(response_message["role"]):
          st.markdown(response_message["content"])

    
    

