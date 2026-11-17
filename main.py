
import os
from rag.requests.controller import get


def main():
    mode = os.getenv("RAG_MODE", "demo").strip().lower()

    print("Режим:", mode)

    query = input("Вопрос: ")

    answer = get(query, top_k=2, mode=mode)

    print("Ответ:")

    print(answer)


if __name__ == "__main__":
    main()
