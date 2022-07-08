
alpha_string = input()


def normalize(any_name):
    for _ in any_name:
        beta_1 = alpha_string.replace("é", "e")
        beta_2 = beta_1.replace("ë", "e")
        beta_3 = beta_2.replace("á", "a")
        beta_4 = beta_3.replace("å", "a")
        beta_5 = beta_4.replace("œ", "oe")
        beta_6 = beta_5.replace("æ", "ae")
    return beta_6


print(normalize(alpha_string))
