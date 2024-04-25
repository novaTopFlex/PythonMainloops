import gi
gi.require_version("Gtk", "4.0")
import gi.repository
import gi.repository.Gtk
def on_activate(app):
    # Create window
    win = gi.repository.Gtk.ApplicationWindow(application=app)
    win.present()
  
# Create a new application
app = gi.repository.Gtk.Application(application_id='com.example.App')
app.connect('activate', on_activate)

# Run the application
app.run(None)
