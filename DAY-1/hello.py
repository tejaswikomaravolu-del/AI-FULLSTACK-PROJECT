import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"What is AI definition and  what are main types of AI ?"
        }
    ]
)
print(response["message"]["content"])