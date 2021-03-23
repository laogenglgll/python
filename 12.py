
#需求:

   #低级密码要求：
   #1. 密码由单纯的数字或字母组成
  # 2. 密码长度小于等于8位

   #中级密码要求：
   #1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
  #2. 密码长度不能低于8位

   #高级密码要求：
   #1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
  #2. 密码只能由字母开头
   #3. 密码长度不能低于16位 
symbols="~!@#$%^&*()_=-/,.?<>;:[]{}\|"
chars='asdfghjklzxcvbnmqwertyuiop'
nums='0987654321'
t='y'
n=0
while t =='y':
   if n==0:
      print('请你输入新的密码')
      passwd=input()
      n=1
   else :
      passwd = input('你输入的密码为空(或有空格)，请您重新输入：')
   length=len(passwd)
   #长度判断
   while (passwd.isspace()==0 and length <=4):
      passwd = input('你输入的密码为空(或有空格/太少)，请您重新输入：')
      length = len(passwd)
   if length <8:
      flag_len = 1
   elif 8<length<16:
      flag_len = 2
   else:
      flag_len =3
   flag_con = 0
   #判断是否包含特服字符
   for each in passwd:
      if each in symbols:
         flag_con+=1
         break
   #判断是否包含数字
   for each in passwd:
      if each in chars:
         flag_con+=1
         break
   for each in passwd:
      if each in passwd:
         flag_con+=1
         break
   #打印结果
   while 1:
      print('您的密码安全等级为：')
      if flag_len==1 or flag_con==1:
         print('低')
      elif flag_len==2 or flag_con==2:
         print('中')
      else :

         print('高')
      print("""可以按以下方式提高密码安全度
      1.密码必须由数字、字母及特殊字符三种组合
      2.密码只能由字母开头
      3.密码长度不能低于16位""")
      t=input("还要继续测试")