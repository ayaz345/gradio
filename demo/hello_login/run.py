import gradio as gr

user_db = {"admin": "admin", "foo": "bar"}


def greet(name):
    return f"Hello {name}!!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")
if __name__ == "__main__":
    demo.launch(enable_queue=False,
        auth=lambda u, p: user_db.get(u) == p,
        auth_message="This is a welcome message")
