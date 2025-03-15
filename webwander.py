import sys
import random
from cefpython3 import cefpython as cef
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QTimer


class WebWanderBrowser:
    def __init__(self):
        self.window_title = "WebWander"
        self.tabs = []
        self.logged_in = False
        self.sync_complete = False
        self.theme_css = ""
        self.themes = {
            "Cyberpunk": self.cyberpunk_theme(),
            "Dark Mode": self.dark_mode_theme(),
            "Retro": self.retro_theme(),
            "Minimalistic": self.minimalistic_theme(),
            "Gamer": self.gamer_theme(),
            "Neon": self.neon_theme()
        }
        self.current_theme = self.themes["Cyberpunk"]  # Default theme

    def cyberpunk_theme(self):
        return """
        body {
            background: linear-gradient(135deg, #0f0f0f, #2b2b2b);
            color: #00ff00;
            font-family: 'Press Start 2P', cursive;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 50px;
            color: #ff00ff;
            text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
        }
        .btn {
            background-color: #333;
            border: 2px solid #00ff00;
            color: #00ff00;
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
            box-shadow: 0 0 5px #00ff00;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #444;
            box-shadow: 0 0 10px #ff00ff;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #ff00ff;
            font-size: 14px;
            text-shadow: 0 0 5px #ff00ff;
        }
        """
    
    def dark_mode_theme(self):
        return """
        body {
            background-color: #1a1a1a;
            color: #dcdcdc;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 50px;
            color: #ff6347;
        }
        .btn {
            background-color: #333;
            border: none;
            color: #dcdcdc;
            font-size: 20px;
            margin: 10px;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 0 5px #ff6347;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #444;
            box-shadow: 0 0 10px #ff6347;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #dcdcdc;
            font-size: 14px;
        }
        """

    def retro_theme(self):
        return """
        body {
            background-color: #ffcc00;
            color: #000;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 50px;
            color: #ff0080;
        }
        .btn {
            background-color: #ff0080;
            border: none;
            color: #fff;
            font-size: 18px;
            padding: 20px;
            border-radius: 10px;
            cursor: pointer;
            margin: 10px;
            box-shadow: 0 0 5px #ff0080;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #ff3399;
            box-shadow: 0 0 10px #ff0080;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #000;
            font-size: 14px;
        }
        """
    
    def minimalistic_theme(self):
        return """
        body {
            background-color: #f0f0f0;
            color: #333;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 50px;
            color: #333;
        }
        .btn {
            background-color: #007bff;
            border: none;
            color: #fff;
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #0056b3;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #333;
            font-size: 14px;
        }
        """
    
    def gamer_theme(self):
        return """
        body {
            background: linear-gradient(135deg, #1e1e1e, #3c3c3c);
            color: #00ff00;
            font-family: 'Press Start 2P', cursive;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 50px;
            color: #00ff00;
            text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
        }
        .btn {
            background-color: #333;
            border: none;
            color: #00ff00;
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
            box-shadow: 0 0 5px #00ff00;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #444;
            box-shadow: 0 0 10px #ff00ff;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #ff00ff;
            font-size: 14px;
            text-shadow: 0 0 5px #ff00ff;
        }
        """

    def neon_theme(self):
        return """
        body {
            background-color: #000;
            color: #39ff14;
            font-family: 'Arial', sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 50px;
            color: #39ff14;
            text-shadow: 0 0 10px #39ff14, 0 0 20px #39ff14;
        }
        .btn {
            background-color: #333;
            border: none;
            color: #39ff14;
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
            box-shadow: 0 0 5px #39ff14;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #444;
            box-shadow: 0 0 10px #39ff14;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #39ff14;
            font-size: 14px;
            text-shadow: 0 0 5px #39ff14;
        }
        """

    def set_theme(self, theme_name):
        """Set the theme based on user choice."""
        if theme_name in self.themes:
            self.current_theme = self.themes[theme_name]

    def create_browser(self, url):
        """Create a new browser with a given URL."""
        browser = cef.CreateBrowserSync(url=url, window_title=self.window_title)
        self.tabs.append(browser)

    def login_dialog(self):
        """Display a login dialog for the user to log in to Google."""
        dialog = QDialog()
        dialog.setWindowTitle("Login to WebWander")
        dialog.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        label = QLabel("Login to WebWander (Optional Google Login)")
        layout.addWidget(label)
        
        username_input = QLineEdit()
        username_input.setPlaceholderText("Enter your email (Optional)")
        layout.addWidget(username_input)
        
        password_input = QLineEdit()
        password_input.setPlaceholderText("Enter your password (Optional)")
        password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_input)
        
        login_button = QPushButton("Login")
        skip_button = QPushButton("Skip Login")
        layout.addWidget(login_button)
        layout.addWidget(skip_button)
        
        login_button.clicked.connect(lambda: self.handle_login(username_input.text(), password_input.text(), dialog))
        skip_button.clicked.connect(lambda: self.skip_login(dialog))
        
        dialog.setLayout(layout)
        dialog.exec_()

    def handle_login(self, email, password, dialog):
        """Simulate handling login and syncing."""
        if email and password:
            self.logged_in = True
            self.sync_complete = True  # Simulate syncing extensions and bookmarks
            dialog.accept()
            print(f"Logged in as {email}. Syncing your settings...")

    def skip_login(self, dialog):
        """Skip the login process."""
        self.logged_in = False
        self.sync_complete = False
        dialog.accept()
        print("Skipping login, starting the browser with default settings.")

    def startup_wizard(self):
        """Simulate a startup wizard with funny messages."""
        print("Starting WebWander setup...")
        self.show_loading_message()  # Show a funny loading message

    def show_loading_message(self):
        """Show a random funny loading message while the app loads."""
        random_message = random.choice(self.loading_messages)
        print(random_message)  # This would show on the console/log. For GUI, you could add a QLabel widget.

        # Simulating the delay of loading for 3 seconds before proceeding
        QTimer.singleShot(3000, self.run_browser)

    def choose_theme(self):
        """Allow the user to select a custom theme file (CSS)."""
        options = QFileDialog.Options()
        theme_file, _ = QFileDialog.getOpenFileName(None, "Choose a Theme", "", "CSS Files (*.css);;All Files (*)", options=options)
        if theme_file:
            with open(theme_file, 'r') as file:
                self.theme_css = file.read()
            print(f"Theme applied from {theme_file}")

    def install_extension(self, extension_path):
        """Install a Chrome extension from a given path."""
        if os.path.exists(extension_path):
            cef.AddExtension(extension_path)
            print(f"Installed extension from {extension_path}")
        else:
            print(f"Extension not found at {extension_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = WebWanderBrowser()
    browser.startup_wizard()  # Show startup wizard first
    sys.exit(app.exec_())
