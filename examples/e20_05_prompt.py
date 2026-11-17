from llm.prompt_builder import build_prompt
chunks=[("Заказы отправляются по предоплате",0.81)]
query="Можно ли оплатить заказ после получения?"
prompt=build_prompt(query, chunks)
print(prompt)