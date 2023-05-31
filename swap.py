def swap(a, b):
    strings_values = ["zero", "one", "two", "three"]

    if 0 <= a <= 3 and 0 <= b <= 3:
        a_string = strings_values[a]
        b_string = strings_values[b]
        a, b = b_string, a_string
    return a, b