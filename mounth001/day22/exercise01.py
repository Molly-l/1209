"""
编写一个接口程序,去判断一段文字中括号的匹配是否正确,如果正确则告知,如果不正确则需要提示大概第多少个字符出现了匹配不正确的情况

思路: 左括号入栈,遇到右括号弹栈进行匹配
     出错情况: 不匹配,缺少左括号,缺少右括号
"""



from mounth001.day21.exercise03 import LStack

text = """Ope)n source (software) [is made better when {users} can easily (contribute) code and documentation to fix 
bugs and add features. ([Python] strongly) encourages community {involvement in (improving) the software}. Learn more about how to make Python better for everyone."""

# 将验证条件提前定义
parens = "()[]{}"
left_parens = "([{"
opposite = {')':'(',']':'[','}':'{'} # 配对字典

st = LStack() # 用于存储左括号

def ver(text):
    n = 0
    for i in text:
        if i in parens:
            if i in left_parens:
                # 遇到左括号入栈
                st.push(n)
            elif st.is_empty():
                # 右括号多了
                print("Error in",n)
                return
            else:
                # 匹配错了
                val = st.pop()
                if text[val]!= opposite[i]:
                    print("Error in",val)
                    return
        n += 1

    if st.is_empty():
        print("OK")
    else:
        # 左括号多了
        val = st.pop()
        print("Error in",val[1])


ver(text)
