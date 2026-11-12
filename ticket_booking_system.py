
"""Movie theater ticket booking and seating management module."""

import hashlib
import secrets

THEATER_SEATS = {
    "A1": {"tier": "Standard", "price": 12.0, "is_sold": False},
    "A2": {"tier": "Standard", "price": 12.0, "is_sold": True},
    "B1": {"tier": "Premium", "price": 20.0, "is_sold": False},
}


def reserve_seat(seat_id, customer, order_history=None):
    """Reserve an available seat and record the booking."""
    if seat_id not in THEATER_SEATS:
        return False

    if THEATER_SEATS[seat_id]["is_sold"]:
        return False

    THEATER_SEATS[seat_id]["is_sold"] = True

    if order_history is None:
        order_history = []

    order_history.append(
        f"Reserved seat {seat_id} for customer {customer}"
    )
    return True


def cancel_seat(seat_id):
    """Cancel a reservation if the seat exists."""
    if seat_id not in THEATER_SEATS:
        return False

    THEATER_SEATS[seat_id]["is_sold"] = False
    return True


def check_seat_status(seat_id):
    """Return True if the requested seat is available."""
    seat = THEATER_SEATS.get(seat_id)

    if seat is None:
        return False

    return not seat["is_sold"]


def compute_discounted_price(seat_id, discount_rate=0.20):
    """Calculate a ticket price after applying a discount rate."""
    if seat_id not in THEATER_SEATS:
        raise ValueError("Invalid seat ID")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be a number")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")

    base_price = THEATER_SEATS[seat_id]["price"]
    return base_price * (1 - discount_rate)


def generate_ticket_hash(ticket_code):
    """Generate a SHA-256 hash for a ticket code."""
    return hashlib.sha256(ticket_code.encode("utf-8")).hexdigest()


def generate_booking_pin():
    """Generate a cryptographically secure four-digit booking PIN."""
    return secrets.randbelow(9000) + 1000


def export_seating_chart(filename="seating_chart.txt"):
    """Export the current seating information to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(THEATER_SEATS))

    print(f"Seating chart exported to: {filename}")


def get_theater_summary(seats):
    """Return the number of seats that have been sold."""
    return sum(
        1 for details in seats.values() if details["is_sold"]
    )


def main():
    """Run a demonstration of the ticket booking system."""
    reserve_seat("A1", "Sarah Connor")
    cancel_seat("A2")

    print("Is B1 available:", check_seat_status("B1"))
    print("Promo price:", compute_discounted_price("B1", 0.20))
    print("Ticket Hash:", generate_ticket_hash("TKT_882"))
    print("Booking PIN:", generate_booking_pin())

    export_seating_chart()
    print("Sold count:", get_theater_summary(THEATER_SEATS))


if __name__ == "__main__":
    main()
