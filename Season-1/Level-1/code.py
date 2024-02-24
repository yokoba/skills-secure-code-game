"""
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
"""

from collections import namedtuple
from typing import Any
from decimal import Decimal as decimal
from rich import print

Order = namedtuple("Order", "id, items")
Item = namedtuple("Item", "type, description, amount, quantity")

MAX_NET = decimal("100000.0")
MAX_AMOUNT = decimal("100000.0")


def validorder(order: Order):
    payment = decimal("0.0")
    product = decimal("0.0")

    for item in order.items:
        amount = decimal(str(item.amount))
        quantity = decimal(str(item.quantity))

        if not (-MAX_AMOUNT < amount < MAX_AMOUNT):
            amount = decimal("0.0")

        if amount < decimal("0.0"):
            amount = decimal(amount) * -1

        if item.type == "payment":
            payment += amount
        elif item.type == "product":
            product = amount * quantity
        else:
            return "Invalid item type: %s" % item.type

        if amount > MAX_NET or product > MAX_AMOUNT:
            return "Total amount payable for an order exceeded"

    if product < payment:
        net = (payment - product) * -1
    else:
        net = payment - product

    if net != decimal("0.0"):
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
