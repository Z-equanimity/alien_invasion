import sys
import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        # Pygame 库全局初始化，一次性启动 Pygame 所有内置模块
        pygame.init()

        self.settings = Settings()

        # 全屏运行
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # .display = Pygame 里专门管窗口 / 画面的模块
        pygame.display.set_caption("Alien Invasion")
        
        self.clock = pygame.time.Clock()        
        # self.screen = pygame.display.set_mode(
        #      (self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            # 控制游戏帧率为 60 FPS
            self.clock.tick(60)

    def _check_events(self):   
            """响应按键和鼠标事件"""
            # 侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()                
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self,event):
            """响应按下"""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                 self.ship.moving_left = True
            elif event.key == pygame.K_ESCAPE:
                 sys.exit()

    def _check_keyup_events(self,event):
            """响应释放"""                
            if  event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
         #每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
