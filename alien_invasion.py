import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        # Pygame 库全局初始化，一次性启动 Pygame 所有内置模块
        pygame.init()

        self.settings = Settings()

        # # 全屏运行
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        # .display = Pygame 里专门管窗口 / 画面的模块
        pygame.display.set_caption("Alien Invasion") 
        
        self.clock = pygame.time.Clock()         
        self.screen = pygame.display.set_mode(
             (self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """响应释放"""                
        if  event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet= Bullet(self)
            self.bullets.add(new_bullet)
 
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
         #每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _update_bullets(self):
        """更新子弹的位置并删除已经消失的子弹"""
        # 更新子弹位置
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                # # 验证子弹确实被删除
                # print(len(self.bullets))

    def _create_fleet(self):
        """创建一个外星人舰队"""
        # 创建一个外星人
        alien = Alien(self)
        alien_width = alien.rect.width
        # 再不断添加，直到没有空间添加外星人位置，外星人的间距为外星人的宽度
        current_x = alien_width
        while current_x < (self.settings.screen_width - 2*alien_width):
            self._creat_alien(current_x)
            current_x += 2 * alien_width

    def _creat_alien(self,x_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
