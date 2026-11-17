import os
from llm.prompt_builder import build_prompt
def get_ai_response(query, chunks, mode="demo"):
    if not chunks:
        return "В базе нет ответа."
    if mode == "demo":
        return "[ДЕМО без генерации]\n" + chunks[0][0]
    if mode != "gemini":
        raise ValueError("Режим должен быть demo или gemini")
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key:
        raise ValueError("Не задан GEMINI_API_KEY")
    from google import genai
    name = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    prompt = build_prompt(query, chunks)
    with genai.Client(api_key=key) as client:
        response = client.models.generate_content(
            model=name,
            contents=prompt,
        )
    answer = response.text
    if not answer or not answer.strip():
        raise RuntimeError("Gemini не вернул текстовый ответ")
    return answer.strip()