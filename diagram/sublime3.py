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

	def view(self, diagram_files):
		for diagram_file in diagram_files:
			if diagram_file:
				window = sublime.active_window()
				if window.num_groups() < 2:
					window.set_layout({
						"cols": [0.0, 0.5, 1.0],
						"rows": [0.0, 1.0],
						"cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
						})
				
				window.focus_group(1)
				window.open_file(diagram_file.name)
				window.focus_group(0)
