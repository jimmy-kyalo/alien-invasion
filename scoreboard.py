import pygame.font

class Scoreboard():
	#class to report scoring info
	def __init__(self, ai_settings, screen, stats):
		self.screen = screen
		self.screen_rect  = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		#font settings for scoring info
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		#prepare the initial score image
		self.prep_score()
		self.prep_high_score()
		self.prep_level()

	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

		#position the level below the score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_high_score(self):
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

		#center high score at top of screen
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_score(self):
		#turn score into a rendered image
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		#display score at top right of screen
		self.score_rect = self.score_image.get_rect()
		self.screen_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)

