class ListHelper:
    @staticmethod
    def find(list,func_condition):
        for item in list:
            if func_condition(item):
                return item
    @staticmethod
    def sum(list,func_condition):
        sum = 0
        for i in list:
            sum += func_condition(i)
            yield i

    @staticmethod
    def name_atk(list, func_condition):
        for i in list:
            yield func_condition(i)

    @staticmethod
    def find03(list,func_condition):
        max_skill = list[0]
        for i in range(1,len(list)):
            if func_condition(max_skill)<func_condition(list[i]):
                max_skill=list[i]
            return max_skill

    @staticmethod
    def order(list,func_condition):
        for i in range(len(list)-1):
            for c in range(i+1,len(list)):
                if func_condition(list[i])>func_condition(list[c]):
                    list[i],list[c]=list[c],list[i]

    @staticmethod
    def min_skill(list,func_condition):
        min_skill=list[0]
        for i in range(1,len(list)):
            if func_condition(min_skill)>func_condition(list[i]):
                min_skill = list[i]
            return min_skill

    @staticmethod
    def pour_order(list,func_condition):
        for i in range(len(list) - 1):
            for c in range(i + 1, len(list)):
                if func_condition(list[i]) < func_condition(list[c]):
                    list[i], list[c] = list[c], list[i]

    # @staticmethod
    # def delete_atk(list,func_condition):
    #     for i in list[::-1]:
    #         if func_condition(i)<10:
    #             list.remove(i)

    @staticmethod
    def delete_atk(list, func_condition):
        for i in range(len(list)-1,-1,-1):
            if func_condition(list[i]) < 10:
                del list[i]
