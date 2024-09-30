class Guest:
    """Class to represent a Guest in the hotel reservation system."""

    def __init__(self, name, email, phone_number, address, guest_id):
        self.name = name  # Constructor to initialize the Guest object with attributes
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.guest_id = guest_id

    # Getter and Setter methods
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_guest_id(self):
        return self.guest_id

    def set_guest_id(self, guest_id):
        self.guest_id = guest_id

    # Placeholder methods with pass statement
    def make_reservation(self):
        """Initiate the reservation process."""
        pass

    def modify_reservation(self):
        """Modify an existing reservation."""
        pass

    def cancel_reservation(self):
        """Cancel the reservation."""
        pass


# Create a Guest object and use its methods
guest = Guest("Shatha Khaled", "Shathooy979@icloud.com", "0502010086", "Dubai", 202280069)
print(f"Guest Name: {guest.get_name()}")
print(f"Guest Email: {guest.get_email()}")
print(f"Guest Phone Number: {guest.get_phone_number()}")
print(f"Guest Address: {guest.get_address()}")
print(f"Guest ID: {guest.get_guest_id()}")


class Reservation:
    """Class to represent a Reservation in the hotel reservation system."""

    def __init__(self, reservation_id, check_in_date, check_out_date, room_type, total_cost): #Constructor to initialize the Guest object with attributes
        self.reservation_id = reservation_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room_type = room_type
        self.total_cost = total_cost
        self.status = "Pending"

    # Getter and Setter methods
    def get_reservation_id(self):
        return self.reservation_id

    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def get_check_in_date(self):
        return self.check_in_date

    def set_check_in_date(self, check_in_date):
        self.check_in_date = check_in_date

    def get_check_out_date(self):
        return self.check_out_date

    def set_check_out_date(self, check_out_date):
        self.check_out_date = check_out_date

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_total_cost(self):
        return self.total_cost

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    # Placeholder methods with pass statement
    def confirm_reservation(self):
        """Confirm the reservation."""
        pass

    def update_reservation(self):
        """Update the details of an existing reservation."""
        pass

    def cancel_reservation(self):
        """Cancel the reservation."""
        pass

# Create a Reservation object and use its methods
reservation = Reservation(979, "2024-7-25", "2024-7-30", "King", 3000.0)
print(f"Reservation ID: {reservation.get_reservation_id()}")
print(f"Check-in Date: {reservation.get_check_in_date()}")
print(f"Check-out Date: {reservation.get_check_out_date()}")
print(f"Room Type: {reservation.get_room_type()}")
print(f"Total Cost: {reservation.get_total_cost()}")

class Room:
    """Class to represent a Room in the hotel reservation system."""

    def __init__(self, room_number, room_type, availability_status, floor_number, view_type): #Constructor to initialize the Guest object with attributes
        self.room_number = room_number
        self.room_type = room_type
        self.availability_status = availability_status
        self.floor_number = floor_number
        self.view_type = view_type

    # Getter and Setter methods
    def get_room_number(self):
        return self.room_number

    def set_room_number(self, room_number):
        self.room_number = room_number

    def get_room_type(self):
        return self.room_type

    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_availability_status(self):
        return self.availability_status

    def set_availability_status(self, availability_status):
        self.availability_status = availability_status

    def get_floor_number(self):
        return self.floor_number

    def set_floor_number(self, floor_number):
        self.floor_number = floor_number

    def get_view_type(self):
        return self.view_type

    def set_view_type(self, view_type):
        self.view_type = view_type

    # Placeholder methods with pass statement
    def check_availability(self):
        """Check if the room is available."""
        pass

    def assign_room(self):
        """Assign the room to a reservation."""
        pass

# Create a Room object and use its methods
room = Room(465, "King", True, 7, "Buildings view")
print(f"Room Number: {room.get_room_number()}")
print(f"Room Type: {room.get_room_type()}")
print(f"Room Availability Status: {room.get_availability_status()}")
print(f"Floor Number: {room.get_floor_number()}")
print(f"View Type: {room.get_view_type()}")

class Payment:
    """Class to represent a Payment in the hotel reservation system."""

    def __init__(self, payment_id, payment_amount, payment_method, transaction_date, payment_status): #Constructor to initialize the Guest object with attributes
        self.payment_id = payment_id
        self.payment_amount = payment_amount
        self.payment_method = payment_method
        self.transaction_date = transaction_date
        self.payment_status = payment_status

    # Getter and Setter methods
    def get_payment_id(self):
        return self.payment_id

    def set_payment_id(self, payment_id):
        self.payment_id = payment_id

    def get_payment_amount(self):
        return self.payment_amount

    def set_payment_amount(self, payment_amount):
        self.payment_amount = payment_amount

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def get_transaction_date(self):
        return self.transaction_date

    def set_transaction_date(self, transaction_date):
        self.transaction_date = transaction_date

    def get_payment_status(self):
        return self.payment_status

    def set_payment_status(self, payment_status):
        self.payment_status = payment_status

    # Placeholder methods with pass statement
    def process_payment(self):
        """Process the payment."""
        pass

    def issue_refund(self):
        """Issue a refund for a cancellation."""
        pass

# Create a Payment object and use its methods
payment = Payment(3767, 3000.0, "Credit Card", "2024-07-24", "Completed")
print(f"Payment ID: {payment.get_payment_id()}")
print(f"Payment Amount: {payment.get_payment_amount()}")
print(f"Payment Method: {payment.get_payment_method()}")
print(f"Transaction Date: {payment.get_transaction_date()}")
print(f"Payment Status: {payment.get_payment_status()}")

