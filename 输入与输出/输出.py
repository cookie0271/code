# 输出
# 看用例 如果每次输入的是一个用例 那就输出一个
# 主要使用
print(" ".join(result)) #这里要求result必须是字符串

# 如果是多个用例（T个用例） 那就要
#ans = [] *T 
#for i in range(T):  
#   ans.append(result)
print(" ".join(ans)) #这里要求ans是字符串数组 也就是要要求result是str

#所以要注意将result转为str