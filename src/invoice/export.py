"""Invoice export to CSV."""

def export(lines, path):
    with open(path, "w") as fh:
        fh.write("amount\n")
        for l in lines:
            fh.write(f"{l['amount']}\n")
