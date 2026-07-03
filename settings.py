class Settings:
    """存储游戏中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.bg_color = (230,230,230)
        self.screen_width = 900
        self.screen_height = 675
        # 飞船的设置
        self.ship_speed = 1.5
        # 子弹的设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        # 允许同时出现的子弹的数量
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
