#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from .base import BaseViewer
import sublime

class Sublime3Viewer(BaseViewer):
	def __str__(self):
		return "Sublime Simple Viewer"

	def load(self):
		if not (sublime.version().startswith('3') or sublime.version().startswith('4')):
			raise Exception("Not Sublime 3 or 4!")

	def view(self,diagram_files):
		for diagram_file in diagram_files:
			if diagram_file:
				sublime.active_window().open_file(diagram_file.name)
