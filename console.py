#!/usr/bin/python3
"""
Interior Health app console powered by Django ORM.
"""

import os
import django
import cmd

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interior_health.settings")
django.setup()

from app.models import (
    User,
    Product,
    Order,
    Payment,
    Tracking,
    ChatbotInteraction,
    Teleconsultation,
)


class InteriorHealthConsole(cmd.Cmd):
    prompt = "(interior_health) "
    intro = "Welcome to the InteriorHealth App Console. Type help or ? to list commands."

    def do_create_user(self, args):
        """Create a new user."""
        try:
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            phone = input("Enter phone: ")
            address = input("Enter address: ")

            user = User(name=name, email=email, password=password, phone=phone, address=address)
            user.save()
            print("User created successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def do_search_medication(self, args):
        """Search for a medication by name."""
        try:
            name = input("Enter medication name: ")
            medications = Product.objects.filter(name__icontains=name)
            if medications.exists():
                for med in medications:
                    print(f"ID: {med.id}, Name: {med.name}, Price: {med.price}, Stock: {med.stock}")
            else:
                print("No medications found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_order_medication(self, args):
        """Create an order for a medication."""
        try:
            user_id = input("Enter user ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))

            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)

            if product.stock >= quantity:
                order = Order(user=user, product=product, quantity=quantity)
                order.save()
                product.stock -= quantity
                product.save()
                print("Order placed successfully.")
            else:
                print("Not enough stock available.")
        except User.DoesNotExist:
            print("User not found.")
        except Product.DoesNotExist:
            print("Product not found.")
        except Exception as e:
            print(f"Error: {e}")

    def do_view_orders(self, args):
        """View all orders."""
        try:
            orders = Order.objects.all()
            for order in orders:
                print(f"Order ID: {order.id}, User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}")
        except Exception as e:
            print(f"Error: {e}")

    def do_track_delivery(self, args):
        """Track the delivery status of an order."""
        try:
            order_id = input("Enter order ID: ")
            tracking = Tracking.objects.filter(order_id=order_id)
            if tracking.exists():
                for record in tracking:
                    print(f"Order ID: {record.order.id}, Status: {record.status}, Last Updated: {record.updated_at}")
            else:
                print("No tracking information found for this order.")
        except Exception as e:
            print(f"Error: {e}")

    def do_exit(self, args):
        """Exit the console."""
        print("Exiting InteriorHealth Console. Goodbye!")
        return True


if __name__ == "__main__":
    InteriorHealthConsole().cmdloop()

