

import random
import string

class SmartNumberPlateAllocation:
    
    def __init__(self):
        self.allocated_plates = {}
        self.blacklisted_plates = {}
        
    def generate_plate(self):
        while True:
            plate = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=4))
            if plate not in self.allocated_plates and plate not in self.blacklisted_plates:
                return plate
            
    def allocate_plate(self, owner_name, contact, email, vehicle_number=None):
        if not vehicle_number:
            vehicle_number = self.generate_plate()
        if vehicle_number in self.allocated_plates:
            print(f"Vehicle number {vehicle_number} is already allocated to {self.allocated_plates[vehicle_number]['owner_name']}")
        else:
            self.allocated_plates[vehicle_number] = {'owner_name': owner_name, 'contact': contact, 'email': email}
            print(f"Vehicle number {vehicle_number} has been allocated to {owner_name}")
            
    def display_allocations(self):
        if not self.allocated_plates:
            print("No number plate allocated yet")
        else:
            print("Allocated number plates: ")
            for vehicle_number, details in self.allocated_plates.items():
                print(f" * {vehicle_number} : {details['owner_name']} (Contact: {details['contact']},Email: {details['email']})")
                
    def search_owner(self, vehicle_number):
        if vehicle_number in self.allocated_plates:
            details = self.allocated_plates[vehicle_number]
            print(f"Vehicle number '{vehicle_number}' is allocated to {details['owner_name']}(Contact: {details['contact']},Email: {details['email']}).")
            if vehicle_number in self.blacklisted_plates:
                print(f"Note: Vehicle number '{vehicle_number}' is also blacklisted.")
        elif vehicle_number in self.blacklisted_plates:
            details = self.blacklisted_plates[vehicle_number]
            print(f"Vehicle number '{vehicle_number}' is blacklisted. Details: {details['owner_name']}(Contact: {details['contact']}, Email: {details['email']}).")
        else:
            print(f"Vehicle number '{vehicle_number}' is not allocated and not blacklisted.")
    
    def remove_allocations(self, vehicle_number):
        if vehicle_number in self.allocated_plates:
            owner = self.allocated_plates.pop(vehicle_number)
            print(f"Number plate {vehicle_number} allocation removed for {owner['owner_name']}")
        else:
            print(f"Number plate {vehicle_number} is not allocated")
        
    def blacklist_plate(self, vehicle_number):
        if vehicle_number in self.allocated_plates:
            details = self.allocated_plates.pop(vehicle_number)
            self.blacklisted_plates[vehicle_number] = details
            print(f"Number plate '{vehicle_number}' allocation removed for {details['owner_name']} and blacklisted.")
        else:
            if vehicle_number not in self.blacklisted_plates:
                self.blacklisted_plates[vehicle_number] = {"owner_name": "Unknown", "contact": "Unknown", "email": "Unknown"}
            print(f"Number plate '{vehicle_number}' has been blacklisted.")
            
    def display_blacklist(self):
        if not self.blacklisted_plates:
            print("No blacklisted plates.")
        else:
            print("Blacklisted plates:")
            for plate, details in self.blacklisted_plates.items():
                print(f"- {plate}: {details['owner_name']} (Contact: {details['contact']}, Email: {details['email']})")

                
if __name__ == "__main__":
    allocator = SmartNumberPlateAllocation()

    # Allocate plates
    allocator.allocate_plate("Alice", "123-456-7890", "alice@example.com")
    allocator.allocate_plate("Bob", "987-654-3210", "bob@example.com", "XYZ789")

    # Display allocations
    allocator.display_allocations()
    print('')

    # Search for owner
    allocator.search_owner("XYZ789")
    allocator.search_owner("ABC123")
    print('')

    # Blacklist a plate
    allocator.blacklist_plate("XYZ789")
    print('')

    # Display blacklist
    allocator.display_blacklist()
    print('')

    # Search again for blacklisted plate
    allocator.search_owner("XYZ789")
    print('')

    # Display allocations after blacklisting
    allocator.display_allocations()
    print('')
