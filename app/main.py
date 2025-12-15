from app.clients import add_client, list_clients
from app.services import add_service, list_services

def show_menu():
    print("\n>>>Smart Appointment Manager<<<")
    print("1. Add Client")
    print("2. List Clients")   
    print("3. Add Service")
    print("4. List Services")
    print("5. Exit")

def main():
    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == '1':
            name = input("Enter client name: ")
            phone = input("Enter client phone: ")
            add_client(name, phone)
            print("Client added successfully.")

        elif option == '2':
            clients = list_clients()
            print("\n--- Clients ---")
            for client in clients:
                print(f"Name: {client['name']}, Phone: {client['phone']}")
        
        elif option == '3':
            name = input("Enter service name: ")
            price = input("Enter service price: ")
            add_service(name, price)
            print("Service added successfully.")

        elif option == '4':
            services = list_services()
            print("\nServices")
            for service in services:
                print(f"- {service['name']} | ${service['price']}")

        elif option == '0':
            print("Goddbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()