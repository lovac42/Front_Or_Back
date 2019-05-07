# -*- coding: utf-8 -*-
# Copyright: (C) 2019 Lovac42
# Support: https://github.com/lovac42/Front_Or_Back
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html


from aqt import mw
from anki.hooks import addHook

def onShowQuestion():
    mw.web.eval("document.getElementById('qa').className='frontSide';");
addHook('showQuestion', onShowQuestion)

def onShowAnswer():
    mw.web.eval("document.getElementById('qa').className='backSide';");
addHook('showAnswer', onShowAnswer)
