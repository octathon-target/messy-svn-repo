"""Invoice calculation."""
from decimal import Decimal

TAX_RATE = Decimal("0.18")

def total(lines):
    subtotal = sum((Decimal(str(l["amount"])) for l in lines), Decimal(0))
    return (subtotal * (1 + TAX_RATE)).quantize(Decimal("0.01"))
