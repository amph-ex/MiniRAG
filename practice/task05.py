from llm.prompt_builder import build_prompt
query = "Сколько стоит доставка?"
chunks = [
    ("Доставка занимает 3-5 дней", 0.9)
]
prompt = build_prompt(query, chunks)
print(prompt)
