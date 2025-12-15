# app/main.py
from app.clients import add_client, list_clients
from app.services import add_service, list_services


def show_menu():
    print("\n=== Smart Appointment Manager ===")
    print("1 - Add client")
    print("2 - List clients")
    print("3 - Add service")
    print("4 - List services")
    print("0 - Exit")


def main():
    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            name = input("Client name: ")
            phone = input("Client phone: ")
            add_client(name, phone)
            print("Client added successfully.")

        elif option == "2":
            clients = list_clients()
            print("\nClients:")
            for client in clients:
                print(f"- {client['name']} ({client['phone']})")

        elif option == "3":
            name = input("Service name: ")
            price = float(input("Service price: "))
            add_service(name, price)
            print("Service added successfully.")

        elif option == "4":
            services = list_services()
            print("\nServices:")
            for service in services:
                print(f"- {service['name']} | ${service['price']}")

        elif option == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
