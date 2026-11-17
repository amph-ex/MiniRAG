from llm.prompt_builder import build_prompt
query = "Где находится магазин?"
chunks = [
    ("Адрес нашего магазина - город Берлин.", 0.85)
]
prompt = build_prompt(query, chunks)
print(prompt)
print(query in prompt)
print("Берлин" in prompt)
