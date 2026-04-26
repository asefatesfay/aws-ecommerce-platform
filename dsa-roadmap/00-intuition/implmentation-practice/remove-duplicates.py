# Given a string, repeatedly remove pairs of adjacent equal characters until no more can be removed.

# Input: "abbaca"
# Output: "ca"

def remove_duplicates_brute(s):
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(s) -1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                changed = True
            else:
                i += 1
    return s

def remove_duplicates(s):
    stack = []

    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)



if __name__ == "__main__":
    s = "abbaca"
    print(remove_duplicates_brute(s))

    s = "azxxzy"
    print(remove_duplicates(s))