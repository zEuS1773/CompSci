def char_count(s, c):
    count = 0
    for char in s:
        if char == c:
            count += 1
        else:
            pass
    return count

def reverse(s):
    refined = ""
    for i in s:
        refined = i + refined
    return refined


