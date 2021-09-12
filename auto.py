#!/usr/bin/env python3

# To get list of QQ group members by loop over all the personal infos

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

for i in range(0,1):
  # Move to next member in memeber list window
  op.moveTo(309,520)
  op.scroll(-34)
  # Open personal info
  op.click(button='right')
  op.moveRel(50,50,duration=0.1)
  op.click()
  # Move to info window and copy QQ number
  op.moveTo(862,659,duration=0.25)
  op.doubleClick()
  op.click()
  copy()
  # Switch to notepad and paste
  switchNext2(INITIAL) 
  op.click()
  paste()
  op.press('enter')
  # Close personal info and move back to group member list
  switchNext()
  op.moveTo(1130,196,duration=0.25)
  delay()
  op.click()
  switchNext()
  INITIAL = False
