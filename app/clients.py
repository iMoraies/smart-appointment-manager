# app/clients.py
from app.storage import load_data, save_data


def add_client(name, phone):
    data = load_data()

    client = {
        "name": name,
        "phone": phone
    }

    data["clients"].append(client)
    save_data(data)


def list_clients():
    data = load_data()
    return data["clients"]
