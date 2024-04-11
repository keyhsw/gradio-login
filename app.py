import gradio as gr
import random
import time

def authenticate(username, password):
    USERNAME='admin'
    PASSWORD=123
    
    if username == USERNAME and password == PASSWORD:
        return True
        
    else:
        return False

def logout(request: gr.Request):

    print("logged out")

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    logout_button = gr.Button(value = "Logout")
    logout_button.click(logout)
    # logout_button = gr.LogoutButton()
    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])


if __name__ == "__main__":
    demo.launch(auth=authenticate,share=True)
