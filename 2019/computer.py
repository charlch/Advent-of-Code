class State():
    def __init__(self, ip, halted, relative_base):
        self.ip = ip
        self.halted = halted
        self.param_mode = []
        self.relative_base=relative_base


class Adder():
    optcode = 1
    params = 3
    def __call__(self, state, memory, args):
        a = read_with_param(0, memory, state.param_mode, args, state)
        b = read_with_param(1, memory, state.param_mode, args, state)
        
        write_with_param(2, memory, state.param_mode, args, state,  int(a)+int(b))
        state.ip += self.params

class Timeser():
    optcode = 2
    params = 3
    def __call__(self, state, memory, args):
        a = read_with_param(0, memory, state.param_mode, args, state)
        b = read_with_param(1, memory, state.param_mode, args, state)
        
        write_with_param(2, memory, state.param_mode, args, state,  a*b)
        
        state.ip += self.params

class Halter():
    optcode = 99
    params = 0
    def __call__(self, state, memory, args):
        assert len(args) == self.params
        state.halted = True

        
class Inputter():
    optcode = 3
    params = 1
    def __init__(self, inpt):
        self.stored_input = inpt
    def __call__(self, state, memory, args):

        print("Input called", args,state.param_mode, +state.relative_base)
        
        if len(self.stored_input)>0:
            v = self.stored_input.pop(0)
        else:                   
            v = int(input("input>"))
        write_with_param(0, memory, state.param_mode, args, state, v)
        state.ip += self.params

class Outputter():
    optcode = 4
    params = 1
    def __init__(self, outpt):
        self.outpt=outpt
        
    def __call__(self, state, memory, args):
        a = read_with_param(0, memory, state.param_mode, args, state)
        
        self.outpt.append(a)
        state.ip += self.params


class JumpIfTrue():
    optcode = 5
    params = 2
    def __call__(self, state,memory, args):
        a = read_with_param(0, memory, state.param_mode, args, state)
        b = read_with_param(1, memory, state.param_mode, args, state)
        
        if a!=0:
            state.ip = b
        else:
            state.ip += self.params

class JumpIfFalse():
    optcode = 6
    params = 2
    def __call__(self, state,memory, args):
        a = read_with_param(0, memory, state.param_mode, args, state)
        b = read_with_param(1, memory, state.param_mode, args, state)
        if a==0:
            state.ip = b
        else:
            state.ip += self.params

class LessThan():
    optcode = 7
    params = 3
    def __call__(self, state,memory, args):
        a = read_with_param(0, memory, state.param_mode, args, state)
        b = read_with_param(1, memory, state.param_mode, args, state)
        
        write_with_param(2, memory, state.param_mode, args, state, 1 if a<b else 0)
        state.ip += self.params

class Equals():
    optcode = 8
    params = 3
    def __call__(self, state,memory, args):
        a = read_with_param(0, memory, state.param_mode, args, state)
        b = read_with_param(1, memory, state.param_mode, args, state)

        write_with_param(2, memory, state.param_mode, args, state, 1 if a==b else 0)
        
        state.ip += self.params

class SetRelativeBase():
    optcode = 9
    params=1
    def __call__(self, state, memory, args):
        state.relative_base += read_with_param(0, memory, state.param_mode, args, state)
        state.ip += self.params

    
def read_with_param(index, memory, param_mode, args,state):
    if param_mode[index] == "0":
        return memory[args[index]]
    elif param_mode[index] == "1":
        return args[index]
    elif param_mode[index] == "2":
        return memory[args[index] +state.relative_base]
    else:
        raise Exception(f"Bad read param mode {param_mode[index]}")

def write_with_param(index, memory, param_mode, args, state,value):
    
    if param_mode[index] == "0":
        memory[args[index]] = value
    elif param_mode[index]=="1":
        raise Exception("Cant write in relative param mode")
    elif param_mode[index]=="2":
       
        memory[args[index]+state.relative_base] = value
    else:
        raise Exception(f"Bad write param mode {param_mode[index]}")
    
def get_param_mode(optcode):
    soptcode = "00000000"+str(optcode)[0:-2]
    out = []
    for p in range(0,4):
        out.append( soptcode[-1-p])
    return out


class Process():
    def __init__(self, memory, inpt=[]):
        self.memory = memory.copy()
        self.memory.extend([0]*10000)
        self.state = State(ip = 0, halted = False, relative_base=0)
        self.output = []
        self.input = []
        self.input.extend(inpt)
        
    def run(self, inpt=[], until_halted= False):
        self.input.extend(inpt)

        optcodes = {op.optcode: op() for op in [Adder, Timeser, Halter, JumpIfTrue, JumpIfFalse, LessThan, Equals, SetRelativeBase]}
        optcodes[Inputter.optcode]= Inputter(self.input)
        optcodes[Outputter.optcode]=Outputter(self.output)
             

        while not self.state.halted:
            optcode = self.memory[self.state.ip]
  
            self.state.ip+=1

            operator = optcodes.get(optcode%100)
            self.state.param_mode = get_param_mode(optcode)
            if not operator:
                raise Exception(f"Bad optcode found {optcode}.")

            args = self.memory[self.state.ip:self.state.ip+operator.params]
        
                
            operator(self.state, self.memory, args)

            if isinstance(operator, Outputter) and not until_halted:
                return self

        return self


def assert_memory_before_after(before, after):
    Process(before).run().memory == after


def test_day2():
    assert_memory_before_after([1,0,0,0,99], [2,0,0,0,99])
    assert_memory_before_after([2,3,0,3,99], [2,3,0,6,99])
    assert_memory_before_after([2,4,4,5,99,0], [2,4,4,5,99,9801])
    assert_memory_before_after([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])


def assert_input_ouput(prog, inpt, outpt):
    assert Process(prog).run([inpt]).output == [outpt]
    
        
def test_day5():
    #position mode equals
    assert_input_ouput([3,9,8,9,10,9,4,9,99,-1,8], 7,0)
    assert_input_ouput([3,9,8,9,10,9,4,9,99,-1,8], 8,1)
    assert_input_ouput([3,9,8,9,10,9,4,9,99,-1,8], 9,0)
    #position mode less than
    assert_input_ouput([3,9,7,9,10,9,4,9,99,-1,8], 7,1)
    assert_input_ouput([3,9,7,9,10,9,4,9,99,-1,8], 8,0)
    assert_input_ouput([3,9,7,9,10,9,4,9,99,-1,8], 9,0)
    #immediate mode equals
    assert_input_ouput([3,3,1108,-1,8,3,4,3,99],7,0)
    assert_input_ouput([3,3,1108,-1,8,3,4,3,99],8,1)
    assert_input_ouput([3,3,1108,-1,8,3,4,3,99],9,0)
    #immediate mode less than
    assert_input_ouput([3,3,1107,-1,8,3,4,3,99],7,1)
    assert_input_ouput([3,3,1107,-1,8,3,4,3,99],8,0)
    assert_input_ouput([3,3,1107,-1,8,3,4,3,99],9,0)


    #positon mode jump
    assert_input_ouput([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],0,0)
    assert_input_ouput([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],1,1)
    assert_input_ouput([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9],2,1)
    #immediate mode jump
    assert_input_ouput([3,3,1105,-1,9,1101,0,0,12,4,12,99,1],0,0)
    assert_input_ouput([3,3,1105,-1,9,1101,0,0,12,4,12,99,1],1,1)
    assert_input_ouput([3,3,1105,-1,9,1101,0,0,12,4,12,99,1],2,1)

    #largerexample
    assert_input_ouput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],7,999)
    assert_input_ouput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],8,1000)
    assert_input_ouput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],9,1001)
    

def test_day7p1():
    c=[Process([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]) for _ in range(5)]
    o = c[0].run([4,0]).output[-1]
    o = c[1].run([3,o]).output[-1]
    o = c[2].run([2,o]).output[-1]
    o = c[3].run([1,o]).output[-1]
    o = c[4].run([0,o]).output[-1]
    assert o == 43210
    
def test_day7p2():

    c=[Process([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],[p]) for p in [9,8,7,6,5]]
    o=0
    while not c[4].state.halted:
        for i in range(5):
            o = c[i].run([o]).output[-1]

    assert o ==139629729


def test_day9():
    assert Process([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]).run(until_halted=True).output ==[109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert Process([1102,34915192,34915192,7,4,7,99,]).run().output == [1219070632396864]
    assert Process([104,1125899906842624,99]).run().output == [1125899906842624]



BOOST_PROD =[1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,0,1,1020,1102,1,38,1015,1102,37,1,1003,1102,21,1,1002,1102,34,1,1017,1101,39,0,1008,1102,1,20,1007,1101,851,0,1022,1102,1,1,1021,1101,24,0,1009,1101,0,26,1005,1101,29,0,1019,1101,0,866,1027,1101,0,260,1025,1102,33,1,1014,1101,0,36,1006,1102,1,25,1018,1102,1,669,1028,1101,0,27,1016,1101,0,23,1012,1102,35,1,1004,1102,1,31,1011,1101,0,664,1029,1101,32,0,1010,1101,0,22,1000,1102,873,1,1026,1102,1,848,1023,1102,265,1,1024,1101,0,28,1013,1101,30,0,1001,109,6,2107,31,-5,63,1005,63,201,1001,64,1,64,1106,0,203,4,187,1002,64,2,64,109,4,21107,40,39,1,1005,1011,219,1106,0,225,4,209,1001,64,1,64,1002,64,2,64,109,-1,2102,1,0,63,1008,63,24,63,1005,63,247,4,231,1106,0,251,1001,64,1,64,1002,64,2,64,109,9,2105,1,6,4,257,1105,1,269,1001,64,1,64,1002,64,2,64,109,-18,2108,19,2,63,1005,63,289,1001,64,1,64,1106,0,291,4,275,1002,64,2,64,109,23,21108,41,41,-8,1005,1015,313,4,297,1001,64,1,64,1106,0,313,1002,64,2,64,109,-19,2101,0,-4,63,1008,63,23,63,1005,63,333,1106,0,339,4,319,1001,64,1,64,1002,64,2,64,109,9,1206,7,357,4,345,1001,64,1,64,1105,1,357,1002,64,2,64,109,-15,2108,22,2,63,1005,63,375,4,363,1105,1,379,1001,64,1,64,1002,64,2,64,109,10,1208,-7,30,63,1005,63,397,4,385,1106,0,401,1001,64,1,64,1002,64,2,64,109,-7,1201,8,0,63,1008,63,27,63,1005,63,421,1106,0,427,4,407,1001,64,1,64,1002,64,2,64,109,-4,1202,3,1,63,1008,63,22,63,1005,63,449,4,433,1105,1,453,1001,64,1,64,1002,64,2,64,109,15,21108,42,40,4,1005,1016,469,1105,1,475,4,459,1001,64,1,64,1002,64,2,64,109,1,21101,43,0,0,1008,1013,43,63,1005,63,501,4,481,1001,64,1,64,1105,1,501,1002,64,2,64,109,-17,1207,10,35,63,1005,63,521,1001,64,1,64,1105,1,523,4,507,1002,64,2,64,109,7,2107,23,6,63,1005,63,545,4,529,1001,64,1,64,1105,1,545,1002,64,2,64,109,3,1201,0,0,63,1008,63,36,63,1005,63,571,4,551,1001,64,1,64,1105,1,571,1002,64,2,64,109,1,21107,44,45,7,1005,1014,593,4,577,1001,64,1,64,1106,0,593,1002,64,2,64,109,7,1205,6,609,1001,64,1,64,1106,0,611,4,599,1002,64,2,64,109,-14,1202,4,1,63,1008,63,32,63,1005,63,635,1001,64,1,64,1106,0,637,4,617,1002,64,2,64,109,30,1205,-9,651,4,643,1105,1,655,1001,64,1,64,1002,64,2,64,109,-4,2106,0,2,4,661,1106,0,673,1001,64,1,64,1002,64,2,64,109,-5,21101,45,0,-8,1008,1013,42,63,1005,63,697,1001,64,1,64,1106,0,699,4,679,1002,64,2,64,109,-10,1207,-6,27,63,1005,63,721,4,705,1001,64,1,64,1105,1,721,1002,64,2,64,109,-11,2101,0,6,63,1008,63,36,63,1005,63,743,4,727,1106,0,747,1001,64,1,64,1002,64,2,64,109,3,2102,1,-2,63,1008,63,33,63,1005,63,767,1105,1,773,4,753,1001,64,1,64,1002,64,2,64,109,18,1206,0,789,1001,64,1,64,1106,0,791,4,779,1002,64,2,64,109,-11,1208,-5,23,63,1005,63,807,1106,0,813,4,797,1001,64,1,64,1002,64,2,64,109,-5,21102,46,1,10,1008,1015,46,63,1005,63,835,4,819,1105,1,839,1001,64,1,64,1002,64,2,64,109,11,2105,1,7,1106,0,857,4,845,1001,64,1,64,1002,64,2,64,109,14,2106,0,-3,1001,64,1,64,1106,0,875,4,863,1002,64,2,64,109,-22,21102,47,1,5,1008,1013,48,63,1005,63,899,1001,64,1,64,1106,0,901,4,881,4,64,99,21102,1,27,1,21102,915,1,0,1105,1,922,21201,1,65718,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,1,942,0,1105,1,922,22101,0,1,-1,21201,-2,-3,1,21102,957,1,0,1106,0,922,22201,1,-1,-2,1105,1,968,21201,-2,0,-2,109,-3,2105,1,0]

print(Process(BOOST_PROD).run(inpt=[2], until_halted=True).output)

if __name__ == "__main2__":
    test_day2()
    test_day5()
    test_day7p1()
    test_day7p2()
    test_day9()



