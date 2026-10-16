"""Hand-written lexer — kept for reference only."""
TOKENS = ("NUMBER", "STRING", "OP", "EOF")

def tokenize(line):
    return [(TOKENS[0], line.strip())] if line.strip() else []
