import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"Give the answer as you are explaining it to a chlid."
        },
        {
            "role":"user",
            "content":"What is AI definition?"
        }
    ]
)
print(response["message"]["content"])