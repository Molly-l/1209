from bll import GameCoreController
from model import DirectionModel
import os

#控制台界面
class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self.__start()
        self.__update()

    #开始
    def __start(self):
        # 产生两个数字
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.__draw_map()# 绘制界面

    #绘制界面
    def __draw_map(self):
        os.system("clear")# 清空控制台
        for line in self.__controller.map:
            for item in line:
                print(item,end = " ")
            print()

    #更新
    def __update(self):
        while True:# 循环
            # 判断玩家的输入　--> 移动地图
            self.__move_map_for_input()
            # 产生新数字
            self.__controller.generate_new_number()
            # 绘制界面
            self.__draw_map()
            # 游戏结束判断 --> 提示
            if self.__controller.is_game_over():
                print("游戏结束")
                break

    # 判断玩家的输入　--> 移动地图
    def __move_map_for_input(self):
        dir = input("请输入方向(wsas)")
        dict_dir = {
            "w":DirectionModel.UP,
            "s":DirectionModel.DOWN,
            "a":DirectionModel.LEFT,
            "d":DirectionModel.RIGHT,
        }
        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])

# -----------
if __name__ =="__main__":
    view = GameConsoleView()
    view.main()

