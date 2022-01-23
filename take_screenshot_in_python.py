import PIL.ImageGrab
image = PIL.ImageGrab.grab()
name="screenshot"+".jpg"
image.save(name)
