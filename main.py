
import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List


models.OpenAI.api_key = "OPENAI_API_KEY"



SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
"""


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):

    user_message = message_history[-1].content.lower()
    if "mental health" in user_message:
        bot_response = "Mental health is an important topic. It refers to the emotional, psychological, and social well-being of an individual. Taking care of your mental health is essential for overall well-being and quality of life. If you have specific questions or concerns about mental health, feel free to share, and I'll do my best to provide helpful information."
    if "down" in user_message:
        bot_response = "I'm really sorry to hear that you're feeling this way. It's important to talk about these feelings. Can you tell me more about what's been bothering you lately?"
        
    if "stress" in user_message:
        bot_response  = "Stress and anxiety can be challenging to cope with. Remember to take breaks, practice deep breathing, and consider talking to someone you trust or a mental health professional for support."
            
    if "anxiety" in user_message:
        bot_response = "Stress and anxiety can be challenging to cope with. Remember to take breaks, practice deep breathing, and consider talking to someone you trust or a mental health professional for support."

    if "difficult decision " in user_message:
      bot_response = "Making decisions can be tough. Take some time to weigh the pros and cons, and consider talking it through with someone you trust to gain perspective."

    if "confidence" in user_message:
        bot_response = "Building self-esteem takes time and self-compassion. Focus on your strengths, set achievable goals, and celebrate your accomplishments, no matter how small."


    else:

        bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
       
    )

    return bot_response, state