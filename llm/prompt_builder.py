def build_context(chunks):
    lines=[]
    for number,item in enumerate(chunks,start=1):
        text,score=item
        lines.append(f'[{number}] {text}')
    return "\n".join(lines)