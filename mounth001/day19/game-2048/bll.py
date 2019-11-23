class GameCoreControllerl:
    # 从右向左接受数据
    def __init__(self):
        self.__game_map = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]

    import numbers
    def fun(self,proportion):
        self.proportion=(9:1)
        self.list01=[2,4,0]
        random_num =proportion(self.list01[0]:self.list01[1])
        self.__game_map.append(random_num)
    @property
    def game_map(self):
        return self.__game_map
    def zero_to_end(self):
        # 休息+练习14:48~15:05
        # 思路 从后向前 如果发现0 删除 再追加0
        # for item in list_target:
        #     if item == 0:
        #         list_target.remove(item)
        #         list_target.append(item)
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] == 0:
                del list_target[i]
                list_target.append(0)
    def merge(self):
        # [0,2,0,2]  -- > [4,0,0,0]
        # 0 1 2
        # [2,2,0,0]  -- > [4,0,0,0]
        # [4,2,0,0]
        # [4,0,0,0]
        # [2,2,2,2]  -- > [4,4,0,0]
        # [2,0,4,0]  -- > [2,4,0,0]
        # 先将0元素移动到末尾
        self.zero_to_end()
        for i in range(len(list_target) - 1):
            if list_target[i] == list_target[i + 1]:
                # 合并  将后面的元素累加到前面的元素上
                list_target[i] += list_target[i + 1]
                # 删除后面的元素
                del list_target[i + 1]
                # 补零
                list_target.append(0)
    def move_left(self):
        for line in self.game_map:
            global list_target
            list_target = line
            self.merge()
    def move_right(self):
        for line in self.game_map:
            global list_target
            list_target = line[::-1]
            self.merge()
            line[::-1] = list_target
            #
            # line = list_target[::-1]

    #上下移动

    def square_matrix(self,list01):
        for c in range(1,len(list01)):  # 123
            for i in range(c,len(list01)):
                list01[i][c - 1], list01[c - 1][i] = list01[c - 1][i], list01[i][c - 1]

    def move_up(self):
        self.square_matrix(self.game_map)
        self.move_left()
        self.square_matrix(self.game_map)

    def move_down(self):
        self.square_matrix(self.game_map)
        self.move_right()
        self.square_matrix(self.game_map)

if __name__=='__main__':
    w01=GameCoreControllerl()
    w01.move_down()
    print(w01.game_map)



# def generate_new_number(self):
#         # 思路:选出所有的空白位置(行／列),再随机挑选一个.
#         list_empty_location = []
#
#         for r in range(len(self.__map)):#0 1 2 3
#             for c in range(len(self.__map[r])):
#                 if self.__map[r][c] == 0:
#                     # 记录r  c  --> 元组
#                     list_empty_location.append((r,c))
#      　　# 确定哪个空白位置1 0
#         loc = random.choice(list_empty_location)
#     　  　#　产生随机数
#     　　if random.randint(1,10) == 1:
#             self.__map[loc[0]][loc[1]] = 4
#         else:
#             self.__map[loc[0]][loc[1]] = 2

    def generate_new_number(self):
        """
            生成新数字
        """
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        # if random.randint(1, 10) == 1:
        #     self.__map[loc.r_index][loc.c_index] = 4
        # else:
        #     self.__map[loc.r_index][loc.c_index] = 2
        self.__map[loc.r_index][loc.c_index] = self.__select_random_number()
        # 因为在该位置生成了新数字，所以该位置就不是空位置了．
        self.__list_empty_location.remove(loc)

    def __select_random_number(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        # 每次统计空位置，都先清空之前的数据，避免影响本次数据．
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        """
            游戏是否结束
        :return: False表示没有结束 True 表示结束
        """
        # 是否具有空位置
        if len(self.__list_empty_location) > 0:
            return False

        # # 判断横向有没有相同的元素
        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map[r]) - 1):  # 0 1 2
        #         if self.__map[r][c] == self.__map[r][c + 1]:
        #             return False
        #
        # # 判断竖向有没有相同的元素
        # for c in range(4):
        #     for r in range(3):
        #         if self.__map[r][c] == self.__map[r + 1][c]:
        #             return False

        for r in range(len(self.__map)):#0
            for c in range(len(self.__map[r]) - 1):  # 0 1 2
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c+1][r]:
                    return False

        return True

