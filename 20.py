def palindrome (arr,head,end):
    if head >= end:
        return 1
    else :
        if arr[head] == arr[end]:
            return palindrome(arr,head+1,end-1)
        else:
            return 0
string_pa=input("输入一个字符串测试是否为回文:")
if palindrome(string_pa,0,len(string_pa)-1):
    print(string_pa,"是回文字符串。")
else:
    print(string_pa,"不是回文字符串。")
#如果没定义返回什么会返回None型 等于0等于假