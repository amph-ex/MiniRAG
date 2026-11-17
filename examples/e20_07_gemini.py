from llm.llm import get_ai_response
chunks = [("Заказы отправляются по предоплате", 0.81)]
query = "Можно ли оплатить заказ после получения?"
answer = get_ai_response(query, chunks, mode="gemini")
print(answer)