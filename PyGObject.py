import gi
gi.require_version("Gtk", "3.0")
import gi.repository
import gi.repository.Gtk
win = gi.repository.Gtk.Window()
win.connect("destroy", gi.repository.Gtk.main_quit)
win.show_all()
gi.repository.Gtk.main()
