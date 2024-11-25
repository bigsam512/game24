#二十四点
import os
import sys
from time import perf_counter
 

class Game24: 
    def __init__(self):
        self.Goal,self.Count=24,0
        #穷举所有的操作符列表共4x4x4=64种
        ops='+-*/'
        self.op_list=[ops[i]+' '+ops[j]+' '+ops[p] for i in range(4) for j in range(4) for p in range(4)]
     
    def printSatistics(self, times):
        print("一共有{}种方案".format(self.Count))
        print("共耗时{:.3f}ms".format(times*1000))
     
    #得到四个用户输入值
    def getNumbers(self, argv):
        if len(argv) == 1:
            if ' ' in argv[0]:
                argv=argv[0].split()
            else:
                argv=list(argv[0])
        if len(argv) != 4:
            return "参数不对：" + " ".join(argv)

        for i in range(0,4):
            argv[i]=str(argv[i])
            if argv[i] not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','0','j','q','k','a']:
                print("参数不对：", argv)
                sys.exit(0)
            if argv[i] == 'a': argv[i]="1"
            if argv[i] == '0': argv[i]="10"
            if argv[i] == 'j': argv[i]="11"
            if argv[i] == 'q': argv[i]="12"
            if argv[i] == 'k': argv[i]="13"
        return ' '.join(argv)
     
    #穷举所有的数值列表
    #共4！=24种
    def getNumList(self, numbers):
        items=numbers.split()
    #四重循环遍历穷举所有的数值组合
        #data_list = []
        # for i in range(4):
        #     for j in range(4): 
        #         if i!=j:
        #             for p in range(4):
        #                 if p!=i and p!=j:
        #                     for q in range(4):
        #                         if q!=i and q!=j and q!=p:
        #                             data_list.append(items[i]+' '+items[j]+' '+items[p]+' '+items[q])
        data_list = [(items[i]+' '+items[j]+' '+items[p]+' '+items[q]) for i in range(4) for j in range(4) for p in range(4) for q in range(4) if (i != j) &(i != p) &(i != q) &(j != p) &(j != q) &(p != q)]
    #使用set方法排除冗余的数字组合
    #当输入的数字中存在重复数字，则4！=24种排序方案会存在重复，必须排除
        return set(data_list)
     
    #计算24点
    def Calc24(self, argv):
        ret = ''
        numbers=self.getNumbers(argv)
        if numbers[0:2]=="参数": return numbers
        num_list=self.getNumList(numbers)
        for numlist in num_list:
            nums=numlist.split()
            for oplist in self.op_list:
                ops=oplist.split()
                ret1 = self.Cal24(nums,ops)
                if ret1: ret += ret1
        return ret 
     
    #对单种运算符顺序和单种数字顺序进行组合运算
    def Cal24(self, nums,op):
        ret='' 
    #第一种情况 ((num0 op0 num1)op1 num2)op2 num3
        try:
            if round(eval("(("+nums[0]+op[0]+nums[1]+")"+op[1]+nums[2]+")"+op[2]+nums[3]),5) == self.Goal:
                self.Count+=1
                ret += "1. `(({}{}{}){}{}){}{}={}`\n".format(nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], self.Goal)
        except:
            pass
     
    #第二种情况 (num0 op0 num1) op1 (num2 op2 num3)
        try:
            if round(eval("("+nums[0]+op[0]+nums[1]+")"+op[1]+"("+nums[2]+op[2]+nums[3]+")"), 5) == self.Goal:
                self.Count += 1
                ret += "1. `({}{}{}){}({}{}{})={}`\n".format(nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], self.Goal)
        except:
            pass
     
    #第三种情况 ( num0 op0 ( num1 op1 num2 )) op2 num3
        try:
            if round(eval("("+nums[0]+op[0]+"("+nums[1]+op[1]+nums[2]+"))"+op[2]+nums[3]), 5) == self.Goal:
                self.Count += 1
                ret += "1. `({}{}({}{}{})){}{}={}`\n".format(nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], self.Goal)
        except:
            pass
     
    #第四种情况 num0 op0 (( num1 op1 num2 ) op2 num3 )
        try:
            if round(eval(nums[0]+op[0]+"(("+nums[1]+op[1]+nums[2]+")"+op[2]+nums[3]+")"), 5) == self.Goal:
                self.Count += 1
                ret += "1. `{}{}(({}{}{}){}{})={}`\n".format(nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], self.Goal)
        except:
            pass
     
    #第五种情况 num0 op0 ( num1 op1 ( num2 op2 num3 ))
        try:
            if round(eval(nums[0]+op[0]+"("+nums[1]+op[1]+"("+nums[2]+op[2]+nums[3]+"))"), 5) == self.Goal:
                self.Count += 1
                ret += "1. `{}{}({}{}({}{}{}))={}`\n".format(nums[0], op[0], nums[1], op[1], nums[2], op[2], nums[3], self.Goal)
        except:
            pass

        return ret 
 
if __name__ == '__main__':
    game=Game24()
    start=perf_counter()
    print(game.Calc24(sys.argv[1:5]))
    game.printSatistics(perf_counter()-start)
