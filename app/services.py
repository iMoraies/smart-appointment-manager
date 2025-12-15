from app. storage import load_data, save_data

def add_service(name, price):
    data = load_data()
    
    service = {
        "name": name,
        "price": price
    }

    data["services"].append(service)
    save_data(data)

def list_services():
    data = load_data()
    return data["services"]