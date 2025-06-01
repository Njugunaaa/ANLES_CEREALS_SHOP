from models import Base, Supplier, Cereal, Customer, Order
from db import engine, SessionLocal
from datetime import datetime

Base.metadata.create_all(bind=engine)
session = SessionLocal()

def add_supplier():
    name = input("Supplier name: ")
    supplier = Supplier(name=name)
    session.add(supplier)
    session.commit()
    print(f"Supplier added: {supplier.name}")

def add_cereal():
    name = input("Cereal name: ")
    price = float(input("Price: "))
    supplier_id = int(input("Supplier ID: "))
    cereal = Cereal(name=name, price=price, supplier_id=supplier_id)
    session.add(cereal)
    session.commit()
    print(f"Cereal added: {cereal.name}")

def update_cereal():
    cereal_id = int(input("Cereal ID to update: "))
    cereal = session.query(Cereal).get(cereal_id)
    if cereal:
        cereal.name = input(f"New name (current: {cereal.name}): ") or cereal.name
        cereal.price = float(input(f"New price (current: {cereal.price}): ") or cereal.price)
        session.commit()
        print("Cereal updated.")
    else:
        print("Cereal not found.")

def delete_cereal():
    cereal_id = int(input("Cereal ID to delete: "))
    cereal = session.query(Cereal).get(cereal_id)
    if cereal:
        session.delete(cereal)
        session.commit()
        print("Cereal deleted.")
    else:
        print("Cereal not found.")

def add_customer():
    username = input("Customer username: ")
    customer = Customer(username=username)
    session.add(customer)
    session.commit()
    print(f"Customer added: {customer.username}")

def place_order():
    customer_id = int(input("Enter Customer ID: "))
    cereal_id = int(input("Enter Cereal ID: "))
    quantity = int(input("Enter Quantity: "))

    cereal = session.query(Cereal).get(cereal_id)
    customer = session.query(Customer).get(customer_id)

    if cereal and customer:
        total = cereal.price * quantity
        order = Order(
            cereal_id=cereal_id,
            customer_id=customer_id,
            quantity=quantity,
            total_price=total,
            status=False 
        )
        session.add(order)
        session.commit()
        print(f"Order placed: {quantity} x {cereal.name} for {customer.username} - Total: ${total}")
    else:
        print("Invalid Customer or Cereal ID.")

def view_cereals():
    cereals = session.query(Cereal).all()
    for cereal in cereals:
        print(f"{cereal.id}: {cereal.name} - {cereal.price}")

def view_orders():
    orders = session.query(Order).all()
    for order in orders:
        cereal = session.query(Cereal).get(order.cereal_id)
        customer = session.query(Customer).get(order.customer_id)
        status = "completed" if order.status else "pending"
        print(f"Order ID: {order.id}, Customer: {customer.username}, Cereal: {cereal.name}, Quantity: {order.quantity}, Total: ${order.total_price}, Status: {status}")

def run_cli():
    while True:
        print("\n1. Add Supplier")
        print("2. Add Cereal")
        print("3. Update Cereal")
        print("4. Delete Cereal")
        print("5. Add Customer")
        print("6. Place Order")
        print("7. View Cereals")
        print("8. View Orders")
        print("9. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_supplier()
        elif choice == '2':
            add_cereal()
        elif choice == '3':
            update_cereal()
        elif choice == '4':
            delete_cereal()
        elif choice == '5':
            add_customer()
        elif choice == '6':
            place_order()
        elif choice == '7':
            view_cereals()
        elif choice == '8':
            view_orders()
        elif choice == '9':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_cli()
