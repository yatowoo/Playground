#!/usr/bin/env python3

import pyautogui as op
import time

OPERATION_DELAY = 0.1
def delay():
  time.sleep(OPERATION_DELAY)

def switchNext():
  op.hotkey('altleft','tab')
  time.sleep(OPERATION_DELAY)

def switchNext2(more = False):
  op.keyDown('altleft')
  op.press('tab')
  op.press('tab')
  if(more):
    op.press('tab')
  op.keyUp('altleft')
  time.sleep(OPERATION_DELAY)

def copy():
  op.hotkey('ctrlleft','c')

def paste():
  op.hotkey('ctrlleft','v')

INITIAL = True

for i in range(0,555):
  op.moveTo(309,520)
  op.scroll(-34)

  op.click(button='right')
  op.moveRel(50,50,duration=0.1)
  op.click()

  op.moveTo(862,659,duration=0.25)
  op.doubleClick()
  op.click()
  copy()
  switchNext2(INITIAL)

  op.click()
  paste()
  op.press('enter')

  switchNext()
  op.moveTo(1130,196,duration=0.25)
  delay()
  op.click()

  switchNext()

  INITIAL = False
