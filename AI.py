import google.generativeai as genai
genai.configure(api_key='AIzaSyBU8RdqlMWvVAXTuBE4vFOeZ4FpsvlmWIo')
model = genai.GenerativeModel('gemini-1.5-flash')
conversation_history = []
def generate_response(prompt):
    conversation_history.append(f"User: {prompt}")
    context = "\n".join(conversation_history)
    response = model.generate_content(context, generation_config=genai.types.GenerationConfig(temperature=0.2))
    ai_response = response.text
    conversation_history.append(f"You: {ai_response}")
    return ai_response
print("Wealthify AI: Hi! I'm Wealthify AI. You can start chatting with me.")
while True:
    user_input = input("You: ").strip()
    ai_response = generate_response(user_input)
    print(f"Wealthify AI: {ai_response}")
    print(conversation_history)
