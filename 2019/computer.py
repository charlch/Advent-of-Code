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

if __name__ == "__main2__":
    test_day2()
    test_day5()
    test_day7p1()
    test_day7p2()
    test_day9()



