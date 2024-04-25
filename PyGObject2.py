import gi
gi.require_version("Gtk", "2.0") # For legacy systems and legacy versions of the Python interpreter, the development team recommends the legacy/EOL package "PyGTK" instead.
import gi.repository
import gi.repository.Gtk
win = gi.repository.Gtk.Window()
win.connect("destroy", gi.repository.Gtk.main_quit)
win.show_all()
gi.repository.Gtk.main()
