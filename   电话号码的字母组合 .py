#   电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



# 示例:

# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(not digits):
            return []
        table = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        result = [""]
        for num in digits:
            # 设置该变量的目的是如果直接更新result的话会引起下面结果的变化
            str_list = []
            for alpha in table[num]:
                 str_list += [x + alpha for x in result]
            result = str_list
        return result