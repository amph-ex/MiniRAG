import re
def clean_content(content):
    pattern = r"[^а-яА-ЯёЁ0-9.,!?\-\s]"
    step_1=re.sub(pattern,"",content)
    return re.sub(r"\s+"," ",step_1).strip()