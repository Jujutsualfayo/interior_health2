from django.db import connection
from django.core.management import call_command
from django.db.utils import OperationalError
from app.models import User, Teleconsultation  # Adjust the import as per your structure

def reset_test_db():
    """Reset the database for testing."""
    try:
        # Drop all tables and recreate the schema
        print("Dropping all tables...")
        with connection.schema_editor(collect_sql=True) as editor:
            editor.delete_model(User)  # Drop User model table
            editor.delete_model(Teleconsultation)  # Drop Teleconsultation model table
        print("Creating new tables...")
        call_command('migrate')  # Apply all migrations to recreate the schema
        populate_test_data()
    except OperationalError as e:
        print(f"Error resetting the test database: {e}")

def populate_test_data():
    """Insert initial data into the test database."""
    try:
        # Create users and a teleconsultation entry
        user1 = User.objects.create(id=1, name="Alice", email="alice@example.com")
        user2 = User.objects.create(id=2, name="Bob", email="bob@example.com")

        teleconsultation = Teleconsultation.objects.create(user=user1, time_slot="2024-12-05T10:00")

        print("Test data populated successfully.")
    except Exception as e:
        print(f"Error populating test data: {e}")

