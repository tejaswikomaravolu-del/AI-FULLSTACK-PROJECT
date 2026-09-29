import ollama
msg=[{
    "role":"system",
    "content":"Answer me using cartoon characters in 2 lines."
}]
while True:
    question=input("Ask me a question:")
    if question.lower()=="exit":
        break
    msg.append(
        {"role": "user",
        "content":question}
    )
    response=ollama.chat(
        model="llama3.2:3b",
        messages=msg
    )
    msg.append(
        {"role":"assistant",
        "content":response["message"]["content"]}
    )
    print("AI:",response["message"]["content"])
print("----CHAT HISTORY----\n")
for m in msg:
    if m["role"]=="system":
        continue
    print(m["role"],":",m["content"])