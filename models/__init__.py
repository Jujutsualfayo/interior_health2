from .user import User
from .product import Product
from .order import Order
from .payment import Payment
from .tracking import Tracking
from .chatbot_interaction import ChatbotInteraction
from .teleconsultation import Teleconsultation

# Exporting models for easier imports
__all__ = [
    "User",
    "Product",
    "Order",
    "Payment",
    "Tracking",
    "ChatbotInteraction",
    "Teleconsultation",
]

