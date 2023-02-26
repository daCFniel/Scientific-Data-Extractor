"""
Process data according to specific set of rules.
"""
import math

homo = 0
lumo = 0
homo_lumo_is_saved = False


def process_data(data):
    """
    Processes data
    """
    processed_data = []

    # Iterate over key/value pairs
    for key in data:
        current_state = []

        # Transition
        current_state.append(p_transition(key))
        # Energy
        current_state.append(p_energy(data[key][0]))
        # Length (λ)
        current_state.append(p_length(data[key][1]))
        # f (intensity)
        current_state.append(p_f(data[key][2]))
        # Contributions
        current_state.append(p_contributions(data[key]))

        processed_data.append(current_state)

    return processed_data


def p_transition(t):
    """
    Transition
    """
    transition = "S0 → S{}".format(t)

    return subscript_digits(transition)


def p_energy(e):
    """
    Energy
    """
    return round_with_trailing_zero(float(e), 2)


def p_length(le):
    """
    Length (λ)
    """
    return round_with_trailing_zero(float(le), 0)


def p_f(f):
    """
    F
    """
    return round_with_trailing_zero(float(f), 3)


def p_contributions(data):
    """
    Contributions
    """
    global homo, lumo, homo_lumo_is_saved
    contribution = ""
    coma = False
    for i in range(3, len(data), 3):

        h = int(data[i])
        l = int(data[i+1])
        c_value = float(data[i+2])

        if not homo_lumo_is_saved:
            homo = h
            lumo = l
            homo_lumo_is_saved = True

        if h < homo:
            h = "H-{}".format(homo - h)
        else:
            h = "H"

        if l > lumo:
            l = "L+{}".format(l - lumo)
        else:
            l = "L"

        percentage = round_with_trailing_zero(pow(c_value, 2) * 200, 2)

        if not coma:
            contribution += "{} → {} ({}%)".format(h, l, percentage)
            coma = True
        else:
            contribution += ", {} → {} ({}%)".format(h, l, percentage)

    return contribution


def round_with_trailing_zero(value, round_digits):
    """
    Round a number leaving the trailing zeros
    """
    return format(round(value, round_digits), "." + str(round_digits) + "f")


def subscript_digits(string):
    """
    Changes digits in a string to subscript
    """
    subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    return string.translate(subscript)
