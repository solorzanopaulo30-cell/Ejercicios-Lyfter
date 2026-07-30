

notes = [80, 90, 40, 55, 96]

def sum_note(notes):
    total = 0
    for note in notes:
        total = total + note
    return total

result = sum_note(notes)
print(result)
