from llm.llm import get_ai_response
chunks = [
    ("Заказы отправляются по предоплате", 0.81)
]
print(get_ai_response("Как оплатить заказ?", chunks, mode="demo"))
print(get_ai_response("Как оплатить заказ?", [], mode="demo"))
