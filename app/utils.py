def format_inr(amount):
    """
    Format a numeric amount into Indian Rupee style.
    Examples:
      2999     -> ₹2,999
      12999    -> ₹12,999
      149999   -> ₹1,49,999
      49       -> ₹49
      1299.5   -> ₹1,299.50
    """
    if amount is None:
        return "₹0"
    try:
        val = float(amount)
    except (ValueError, TypeError):
        return f"₹{amount}"

    is_integer = (abs(val - round(val)) < 0.001)

    if is_integer:
        int_part = str(int(round(val)))
        dec_part = ""
    else:
        parts = f"{val:.2f}".split(".")
        int_part = parts[0]
        dec_part = "." + parts[1]

    sign = ""
    if int_part.startswith("-"):
        sign = "-"
        int_part = int_part[1:]

    if len(int_part) <= 3:
        formatted = int_part
    else:
        last3 = int_part[-3:]
        remaining = int_part[:-3]
        groups = []
        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.insert(0, remaining)
        formatted = ",".join(groups) + "," + last3

    return f"₹{sign}{formatted}{dec_part}"
