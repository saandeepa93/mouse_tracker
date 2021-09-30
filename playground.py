from pynput import mouse
from logger import Logger
import pyautogui
import time
from sys import exit as e


def on_move(x, y):
  print(x, y)
  logger.log_moves(round(x, 2), round(y, 2), "Move", time.time() - start_time)

def on_click(x, y, button, pressed):
  if pressed:
    logger.log_moves(round(x, 2), round(y, 2), "Pressed", time.time() - start_time)
    logger.drag = True
  if not pressed:
    logger.drag = False
    logger.log_moves(round(x, 2), round(y, 2), "Released", time.time() - start_time)
    logger.save()

def on_scroll(x, y, dx, dy):
    logger.log_moves(round(x, 2), round(y, 2), "Scroll", time.time() - start_time)


if __name__ == "__main__":
  print(f"Screen size: {pyautogui.size()}")
  start_time = time.time()

  #Replace filename with actual userID during tasks
  logger = Logger("./logs", "u_3")
  
  listener = mouse.Listener(
      on_move=on_move,
      on_click=on_click,
      on_scroll=on_scroll)

  listener.start()
  listener.join()
