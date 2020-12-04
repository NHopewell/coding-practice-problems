def check_last_index(s: str) -> bool:
    try:
        last = int(s[len(s)-1])
        return last
    except:
        return None

def increment_string(s: str) -> str:

    
    s = list(s)
    last = check_last_index(s)
    
    if last:
        last += 1
        s.pop()
        s.append(str(last))
        return "".join(s)
    else:
        s.append("1")
        return "".join(s)
