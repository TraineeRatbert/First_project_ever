msgs = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):", " ... lazy", " ... very lazy", " ... very, very lazy",
        "You are", "Are you sure? It is only one digit! (y / n)",
        " Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]
memory = 0
alef = 0
bet = 0
vet = 0
a = 0
b = 0
result = 0
input_a_correct = 0  # flag to check that input a is float numbers
input_b_correct = 0  # flag to check that input b is float numbers
answer_1 = 0  # flag to store results start position is 0, yes is 1 no is 2
answer_2 = 0  # flag to continue calculations start position is 0, yes is 1 no is 2


def get_input():
    global alef
    global bet
    global vet
    global answer_1
    global answer_2
    print(msgs[0])
    calc = input()
    alef, bet, vet = calc.split()
    answer_1 = 0  # reset answer_1 to allow recheck at next iteration
    answer_2 = 0  # reset answer_2 to allow recheck at next iteration


def memory_and_inputs_check():
    global alef
    global a
    global input_a_correct
    global vet
    global b
    global input_b_correct
    if alef != "M":
        try:
            alef = float(alef)
        except ValueError:
            print(msgs[1])
            get_input()
        else:
            a = float(alef)
            input_a_correct = 1
    elif alef == "M":
        a = float(memory)  # a equals memory
        input_a_correct = 1
    if vet != "M":
        try:
            vet = float(vet)
        except ValueError:
            print(msgs[1])
            get_input()
        else:
            b = float(vet)
            input_b_correct = 1
    elif vet == "M":
        b = float(memory)
        input_b_correct = 1


def complexity_check_and_calculate():
    global result
    single_digit_a = 0  # flag to check for single digit a
    single_digit_b = 0  # flag to check for single digit b
    msg_lazy = ""
    if -10 < a < 10 and a.is_integer():
        single_digit_a = 1
    if -10 < b < 10 and b.is_integer():
        single_digit_b = 1
    if single_digit_a == 1 and single_digit_b == 1:
        msg_lazy = msg_lazy + msgs[6]
    if (a == 1 or b == 1) and bet == "*":
        msg_lazy = msg_lazy + msgs[7]
    if (a == 0 or b == 0) and (bet == "*" or bet == "+" or bet == "-"):
        msg_lazy = msg_lazy + msgs[8]
    if msg_lazy != "":
        msg_lazy = msgs[9] + msg_lazy
        print(msg_lazy)
    if bet == "+":
        result = a + b
    elif bet == "-":
        result = a - b
    elif bet == "*":
        result = a * b
    elif bet == "/":
        if b != 0:
            result = a / b
        else:
            print(msgs[3])
            run_calculator()
    print(result)


def get_answer_1():
    global answer_1
    while answer_2 == 0:
        print(msgs[4])
        storage = input()
        if storage == "y":
            answer_1 = 1  # answer_1 = 1 affirmative answer
            break
        elif storage == "n":
            break
        else:
            continue


def confirm_record():
    msg_index = 10
    global memory
    while msg_index < 13:
        if -10 < result < 10 and result.is_integer():
            print(msgs[msg_index])
            save_reply = input()
            if save_reply == "y":
                msg_index += 1
            elif save_reply == "n":
                get_answer_2()
                break
            else:
                continue
        else:
            memory = result
            get_answer_2()
            break
    else:
        memory = result
        get_answer_2()


def get_answer_2():
    global answer_2
    while answer_2 == 0:
        print(msgs[5])
        more_counting = input()
        if more_counting == "y":
            answer_2 = 1  # answer_1 = 1 affirmative answer
            run_calculator()
            break
        elif more_counting == "n":
            answer_2 = 2  # answer_1 = 2 negative answer
            break
        else:
            continue


def run_calculator():
    get_input()
    memory_and_inputs_check()
    operand_set = 0
    if input_a_correct == 1 and input_b_correct == 1:
        while True:
            if bet not in ("+", "-", "*", "/"):
                print(msgs[2])
                get_input()
            else:
                operand_set = 1
                break
    if operand_set == 1:
        complexity_check_and_calculate()
        get_answer_1()
        if answer_1 == 1:
            confirm_record()
        else:
            get_answer_2()


while True:
    if answer_2 != 2:
        run_calculator()
    else:
        break
