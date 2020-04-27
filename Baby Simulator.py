from random import choice 

questions =["Why is the sky blue?:", "Why is there a face on the moon?:",
            "What happened to dinosaurs?:"]

question = choice(questions)
answer =input("Why is the sky blue?:").lower()

while answer != "just because":
    answer =input("why?:").strip().lower()

print("Oh...Okay")
