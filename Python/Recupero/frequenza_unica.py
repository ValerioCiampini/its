from string import punctuation

def count_unique_words(s:str) -> dict[str, int]:
    s.split(" ")
    d:dict[str, int] = {}
    
    for token in s:
        token_lower:str = token.lower()
        clean_token:str = token_lower.strip(punctuation)

        if not clean_token:
            continue
        
        if clean_token in d:
            d[clean_token] += 1
        else:
            d[clean_token] = 1

    return d