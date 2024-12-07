from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'  # This specifies the name of your app. Make sure it matches the directory name of your app.

    def ready(self):
        # This is where you'd put any code that needs to run when the app is ready.
        # Since you're not using signals, we can leave this empty for now.
        pass


