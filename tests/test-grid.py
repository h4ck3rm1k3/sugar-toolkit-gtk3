#!/usr/bin/python
import pygtk
pygtk.require('2.0')

from sugar.session.UITestSession import UITestSession

session = UITestSession()
session.start()

import gtk
import goocanvas

from sugar.graphics.iconcolor import IconColor
from sugar.graphics.IconItem import IconItem
from sugar.graphics.CanvasView import CanvasView
from sugar.graphics.CanvasBox import CanvasBox
from sugar.graphics.Grid import Grid

def _new_icon_clicked_cb(icon):
	box.remove_child(icon)

def _icon_clicked_cb(icon):
	icon = IconItem(color=IconColor(), icon_name='activity-groupchat')
	icon.connect('clicked', _new_icon_clicked_cb)
	box.set_constraints(icon, 3, 3)
	box.add_child(icon, 0)

model = goocanvas.CanvasModelSimple()
root = model.get_root_item()

grid = Grid()

box = CanvasBox(grid, CanvasBox.HORIZONTAL, 1)
grid.set_constraints(box, 3, 3)
root.add_child(box)

rect = goocanvas.Rect(fill_color='red')
box.set_constraints(rect, 3, 3)
box.add_child(rect)

icon = IconItem(color=IconColor(), icon_name='activity-web')
icon.connect('clicked', _icon_clicked_cb)
box.set_constraints(icon, 3, 3)
box.add_child(icon)

icon = IconItem(color=IconColor(), icon_name='activity-groupchat')
box.set_constraints(icon, 3, 3)
box.add_child(icon)

window = gtk.Window()
window.connect("destroy", lambda w: gtk.main_quit())
window.show()

canvas = CanvasView()
canvas.show()
window.add(canvas)
canvas.set_model(model)

gtk.main()
