def is_isomorphic_brute(s, t):

    if len(s) != len(s):
        return False
    
    mapping = {}

    for cs, ct in zip(s, t):

        if cs in mapping:
            if mapping[cs] != ct:
                return False
        else:
            if ct in mapping.values():
                return False
            mapping[cs] = ct
    
    return True


def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for cs, ct in zip(s, t):
        if cs in s_to_t:
            if s_to_t[cs] != ct:
                return False
        else:
            s_to_t[cs] = ct
        
        if ct in t_to_s:
            if t_to_s[ct] != cs:
                return False
        else:
            t_to_s[ct] = cs
    
    return False


if __name__ == "__main__":
    print(is_isomorphic_brute("egg", "add"))  # True
    print(is_isomorphic_brute("foo", "bar"))  # False
    print(is_isomorphic_brute("paper", "title"))  # True
        