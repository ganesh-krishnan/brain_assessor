import pyglet
from classifier.utils.draw import RectangularButton


class GameOver():

	def __init__(self, title, score, width=600, height=500, highscore = 0):

		self.window = pyglet.window.Window(width, height, caption = title)
		self.heading = pyglet.text.Label(title, font_size=30, x = width // 2, y = height - 60, anchor_x = 'center')

		self.score = pyglet.text.Label(str(score), font_size=26, font_name='Verdana', x = width // 2, y = self.heading.y - 100, anchor_x = 'center')
		self.highest = pyglet.text.Label('Best : ' + str(highscore), font_size = 16, x = width // 2, y = self.score.y - 50, anchor_x = 'center', color = [79,79,79,255])
		self.againBtn = RectangularButton('Play Again', 1, x = width // 2 - 75, y = self.highest.y - 60, w = 150, h = 60, color = [0,172,101], textsize = 18)
		self.backBtn = RectangularButton('Exit', 2, x = width // 2 - 75, y = self.againBtn.y - 70, w = 150, h= 60, color = [233,102,44], textsize = 18)

		self.clickables = [self.againBtn, self.backBtn]
		self.retCode = 0


		@self.window.event
		def on_draw():
			self.window.clear()
			self.heading.draw()
			self.score.draw()
			self.highest.draw()
			self.againBtn.draw()
			self.backBtn.draw()


		@self.window.event
		def on_close():
			self.retCode = 0


		@self.window.event
		def on_mouse_release(x, y, button, modifiers):
			if button != pyglet.window.mouse.LEFT:
				return
			for i in self.clickables:
				if x < i.x or x > (i.x + i.w):
					continue
				if y > i.y or y < (i.y - i.h):
					continue
				self.click_event(i.value)
				break


	def start(self):
		pyglet.app.run()
		# self.againBtn.figure.delete()
		# self.backBtn.figure.delete()
		self.window.pop_handlers()
		return self.retCode


	def click_event(self, value):
		'''
		Responds to click on elements
		'''
		if value == 1:
			self.retCode = 1
		elif value == 2:
			self.retCode = 0
		self.window.close()
		pyglet.app.exit()
