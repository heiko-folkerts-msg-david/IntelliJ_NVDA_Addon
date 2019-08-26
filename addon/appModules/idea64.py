# IntelliJ Support App Module for NVDA

import appModuleHandler
import tones
import controlTypes
from editableText import EditableText
from scriptHandler import script
import ui
import api

class EnhancedEditableText(EditableText):
	__gestures = {
		# these IntelliJ commands change caret position, so they should trigger reading new line position
		"kb:alt+downArrow" : "caret_moveByLine",
		"kb:alt+upArrow" : "caret_moveByLine",
		"kb:control+leftBracket" : "caret_moveByLine",
		"kb:control+rightBracket" : "caret_moveByLine",
		"kb:f2" : "caret_moveByLine",
		"kb:shift+f2" : "caret_moveByLine",
		"kb:control+b" : "caret_moveByLine",
		"kb:control+alt+leftArrow" : "caret_moveByLine",
		"kb:control+alt+rightArrow" : "caret_moveByLine",
		"kb:control+y" : "caret_moveByLine",
		"kb:f3" : "caret_moveByLine",
		"kb:shift+f3" : "caret_moveByLine",
	}

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_EDITABLETEXT:
			clsList.insert(0, EnhancedEditableText)
	
	@script(gesture = 'kb:NVDA+i')
	def script_readStatusBar(self, gesture):
		obj = api.getForegroundObject().simpleFirstChild
		tones.beep(550,50)
		while obj is not None:
			if obj.role is controlTypes.ROLE_STATUSBAR:
				msg = obj.simpleFirstChild.name
				ui.message(msg)
				return
			obj = obj.simpleNext
		ui.message('couldnt find status bar')