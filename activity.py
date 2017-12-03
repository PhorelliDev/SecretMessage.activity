import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gettext import gettext as _

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem


class SecretMessageActivity(activity.Activity):
    
   

    def __init__(self, handle):
        
        activity.Activity.__init__(self, handle)
        # we do not have collaboration features
        # make the share option insensitive
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

       

        # Main layout setup
        layout = Gtk.Grid()
        self.msg = Gtk.Label("This is a secret message!")
        sbutton = Gtk.Button("Show message")
        sbutton.connect("clicked", self._show)
        hbutton = Gtk.Button("Hide Message")
        hbutton.connect("clicked", self._hide)
        layout.attach(self.msg, 0, 0, 2, 1)
        layout.attach_next_to(sbutton, self.msg, Gtk.PositionType.BOTTOM, 1, 1)
        layout.attach_next_to(hbutton, sbutton, Gtk.PositionType.RIGHT, 1, 1)
        self.set_canvas(layout)
        self.show_all()
    # Show and hide secret message
    def _show(self, button):
        self.msg.set_text("This is a secret message!")

    def _hide(self, button):
        self.msg.set_text("")

