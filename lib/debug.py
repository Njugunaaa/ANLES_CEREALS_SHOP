from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Customer, Cereal, Order, Supplier
from datetime import datetime

engine = create_engine('sqlite:///Anles_Cereals.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# CREATE OPERATIONS

def create_supplier():
    name = input("Enter supplier name: ")
    supplier = Supplier(name=name)
    session.add(supplier)
    session.commit()
    print("Supplier created.")

def create_cereal():
    view_suppliers()
    supplier_id = int(input("Enter supplier ID for this cereal: "))
    name = input("Enter cereal name: ")
    price = float(input("Enter cereal price: "))
    cereal = Cereal(name=name, price=price, supplier_id=supplier_id)
    session.add(cereal)
    session.commit()
    print("Cereal added.")

def create_customer():
    name = input("Enter customer name: ")
    customer = Customer(name=name)
    session.add(customer)
    session.commit()
    print("Customer created.")

def create_order():
    view_customers()
    customer_id = int(input("Enter customer ID: "))
    view_cereals()
    cereal_id = int(input("Enter cereal ID: "))
    quantity = int(input("Enter quantity: "))

    cereal = session.query(Cereal).filter_by(id=cereal_id).first()
    total_price = cereal.price * quantity

    order = Order(
        customer_id=customer_id,
        cereal_id=cereal_id,
        quantity=quantity,
        total_price=total_price,
        status="pending"
    )
    session.add(order)
    session.commit()
    print("Order placed.")

# READ OPERATIONS

def view_suppliers():
    suppliers = session.query(Supplier).all()
    print("\nSuppliers:")
    for s in suppliers:
        print(f"ID: {s.id}, Name: {s.name}")

def view_cereals():
    cereals = session.query(Cereal).all()
    print("\nCereals:")
    for c in cereals:
        print(f"ID: {c.id}, Name: {c.name}, Price: {c.price}, Supplier: {c.supplier.name}")

def view_cereals_by_supplier():
    view_suppliers()
    supplier_id = int(input("Enter supplier ID to see their cereals: "))
    supplier = session.query(Supplier).filter_by(id=supplier_id).first()
    if supplier:
        print(f"\nCereals supplied by {supplier.name}:")
        for c in supplier.cereals:
            print(f"- ID: {c.id}, Name: {c.name}, Price: {c.price}")
    else:
        print("Supplier not found.")

def view_customers():
    customers = session.query(Customer).all()
    print("\nCustomers:")
    for c in customers:
        print(f"ID: {c.id}, Name: {c.name}")

def view_orders():
    orders = session.query(Order).all()
    print("\nOrders:")
    for o in orders:
        print(f"Order ID: {o.id}, Customer: {o.customer.name}, Cereal: {o.cereal.name}, "
              f"Quantity: {o.quantity}, Total: {o.total_price}, Status: {o.status}, Date: {o.created_at}")

def view_order_by_id():
    order_id = int(input("Enter order ID: "))
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        print(f"Order ID: {order.id}")
        print(f"Customer: {order.customer.name}")
        print(f"Cereal: {order.cereal.name}")
        print(f"Quantity: {order.quantity}")
        print(f"Total: {order.total_price}")
        print(f"Status: {order.status}")
    else:
        print("Order not found.")

# UPDATE OPERATIONS

def update_supplier():
    view_suppliers()
    supplier_id = int(input("Enter supplier ID to update: "))
    supplier = session.query(Supplier).filter_by(id=supplier_id).first()
    if supplier:
        new_name = input("Enter new name: ")
        supplier.name = new_name
        session.commit()
        print("Supplier updated.")
    else:
        print("Supplier not found.")

def update_cereal_price():
    view_cereals()
    cereal_id = int(input("Enter cereal ID to update: "))
    cereal = session.query(Cereal).filter_by(id=cereal_id).first()
    if cereal:
        new_price = float(input("Enter new price: "))
        cereal.price = new_price
        session.commit()
        print("Cereal price updated.")
    else:
        print("Cereal not found.")

def update_customer():
    view_customers()
    customer_id = int(input("Enter customer ID to update: "))
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        new_name = input("Enter new name: ")
        customer.name = new_name
        session.commit()
        print("Customer updated.")
    else:
        print("Customer not found.")

def clear_order():
    order_id = int(input("Enter order ID to clear: "))
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        if order.status == "cleared":
            print("Order is already cleared.")
        else:
            order.status = "cleared"
            session.commit()
            print("Order cleared.")
    else:
        print("Order not found.")

# DELETE OPERATIONS

def delete_supplier():
    view_suppliers()
    supplier_id = int(input("Enter supplier ID to delete: "))
    supplier = session.query(Supplier).filter_by(id=supplier_id).first()
    if supplier:
        session.delete(supplier)
        session.commit()
        print("Supplier deleted.")
    else:
        print("Supplier not found.")

def delete_cereal():
    view_cereals()
    cereal_id = int(input("Enter cereal ID to delete: "))
    cereal = session.query(Cereal).filter_by(id=cereal_id).first()
    if cereal:
        session.delete(cereal)
        session.commit()
        print("Cereal deleted.")
    else:
        print("Cereal not found.")

def delete_customer():
    view_customers()
    customer_id = int(input("Enter customer ID to delete: "))
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print("Customer deleted.")
    else:
        print("Customer not found.")

def delete_order():
    view_orders()
    order_id = int(input("Enter order ID to delete: "))
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        session.delete(order)
        session.commit()
        print("Order deleted.")
    else:
        print("Order not found.")

# CLI MAIN MENU

def mainmenu():
    while True:
        print("\n***** Cereal Ordering CLI *****")
        print("1. Create supplier")
        print("2. Create cereal")
        print("3. Create customer")
        print("4. Create order")
        print("5. View suppliers")
        print("6. View cereals")
        print("7. View cereals by supplier")
        print("8. View customers")
        print("9. View all orders")
        print("10. View order by ID")
        print("11. Update supplier")
        print("12. Update cereal price")
        print("13. Update customer")
        print("14. Clear order")
        print("15. Delete supplier")
        print("16. Delete cereal")
        print("17. Delete customer")
        print("18. Delete order")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == "1": create_supplier()
        elif choice == "2": create_cereal()
        elif choice == "3": create_customer()
        elif choice == "4": create_order()
        elif choice == "5": view_suppliers()
        elif choice == "6": view_cereals()
        elif choice == "7": view_cereals_by_supplier()
        elif choice == "8": view_customers()
        elif choice == "9": view_orders()
        elif choice == "10": view_order_by_id()
        elif choice == "11": update_supplier()
        elif choice == "12": update_cereal_price()
        elif choice == "13": update_customer()
        elif choice == "14": clear_order()
        elif choice == "15": delete_supplier()
        elif choice == "16": delete_cereal()
        elif choice == "17": delete_customer()
        elif choice == "18": delete_order()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    mainmenu()
