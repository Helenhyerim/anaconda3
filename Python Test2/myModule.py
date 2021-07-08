#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 모듈은 파이썬 코드로 저장해야 함, ipynd 가 아니라 py
# 클래스의 정의
class product : 
    # 생성자
    def __init__(self, c, n, p):
        self.code = c
        self.name = n
        self.price = p
        
    def printProduct(self):
        print('상품명은', self.name, '입니다')
        
    def __str__(self):
        return '코드:' + self.code + '상품명:' + self.name + ' 가격:' + str(self.price)
    
    
# 함수의 정의
def test():
    print('myModule 모듈의 test() 함수 실행됨')
    

