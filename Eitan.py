def get_digit_at_position(position):
    current_position = 1
    current_number = 1
    print(current_position, current_number)

    while current_position < position:
        current_position += len(str(current_number))
        current_number += 1
        print(current_position,current_number)

    overshoot = current_position - position
    return int(str(current_number)[len(str(current_number)) - overshoot - 1])

result = get_digit_at_position(1224)
print(result)