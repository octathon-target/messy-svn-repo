"""Payment status transitions."""

STATES = ("pending", "authorized", "captured", "refunded")

def next_state(current):
    idx = STATES.index(current)
    return STATES[min(idx + 1, len(STATES) - 1)]
