from llm.prompt_builder import build_context
chunks=[("Заказы отправляются по предоплате",0.81)]
chunks.append(("Доставка занимает 3-5 дней", 0.62))
print(build_context(chunks))