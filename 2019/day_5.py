

class State():
    def __init__(self, ip, halted):
        self.ip = ip
        self.halted = halted
        self.param_mode = []


class Adder():
    optcode = 1
    params = 3
    def __call__(self, state, memory, args):
        #print(state.param_mode)
        #print(args)
        assert len(args) == self.params
        a = memory[args[0]] if state.param_mode[0] else args[0]
        b = memory[args[1]] if state.param_mode[1] else args[1]
        memory[args[2]] = a+b
        state.ip += self.params

class Timeser():
    optcode = 2
    params = 3
    def __call__(self, state, memory, args):
        #print(state)
        a = memory[args[0]] if state.param_mode[0] else args[0]
        b = memory[args[1]] if state.param_mode[1] else args[1]
        memory[args[2]] = a*b
        state.ip += self.params

class Halter():
    optcode = 99
    params = 0
    def __call__(self, state, memory, args):
        assert len(args) == self.params
        state.halted = True


class Jump():
    optcode = 3
    params = 1
    def __call__(self, state, memory, args):
        state.ip = args[0]
        
class Inputter():
    optcode = 3
    params = 1
    def __call__(self, state, memory, args):
        memory[args[0]] = int(input("input>"))
        state.ip += self.params

class Outputter():
    optcode = 4
    params = 1
    def __call__(self, state, memory, args):
        a = memory[args[0]] if state.param_mode[0] else args[0]
        print(f"Output {a}")
        state.ip += self.params


class JumpIfTrue():
    optcode = 5
    params = 2
    def __call__(self, state,memory, args):
        a = memory[args[0]] if state.param_mode[0] else args[0]
        b = memory[args[1]] if state.param_mode[1] else args[1]
        if a!=0:
            state.ip = b
        else:
            state.ip += self.params

class JumpIfFalse():
    optcode = 6
    params = 2
    def __call__(self, state,memory, args):
        a = memory[args[0]] if state.param_mode[0] else args[0]
        b = memory[args[1]] if state.param_mode[1] else args[1]
        if a==0:
            state.ip = b
        else:
            state.ip += self.params

class LessThan():
    optcode = 7
    params = 3
    def __call__(self, state,memory, args):
        a = memory[args[0]] if state.param_mode[0] else args[0]
        b = memory[args[1]] if state.param_mode[1] else args[1]
        
        memory[args[2]] = 1 if a<b else 0
        state.ip += self.params

class Equals():
    optcode = 8
    params = 3
    def __call__(self, state,memory, args):
        a = memory[args[0]] if state.param_mode[0] else args[0]
        b = memory[args[1]] if state.param_mode[1] else args[1]
        
        memory[args[2]] = 1 if a==b else 0
        state.ip += self.params 
    
optcodes = {op.optcode: op() for op in [Adder, Timeser, Halter, Inputter, Outputter ,JumpIfTrue, JumpIfFalse, LessThan, Equals]}

def get_param_mode(optcode):
    soptcode = "00000000"+str(optcode)[0:-2]
    #print(soptcode)
    out = []
    for p in range(0,4):
        #print(soptcode[-1-p])
        out.append( soptcode[-1-p] == "0")
    return out


def run(memory):

    state = State(ip = 0, halted = False)
    
    for _ in range(0, 10000):
       
        optcode = memory[state.ip]
        state.ip+=1

        operator = optcodes.get(optcode%100)
        state.param_mode = get_param_mode(optcode)
        if not operator:
            raise Exception(f"Bad optcode found {optcode}.")

        args = memory[state.ip:state.ip+operator.params]
        
                
        operator(state, memory, args)
        if state.halted:
            return memory
    raise("didn't finish in 10000 steps")

#print(run([1001,1,10,3,99]))
#assert run([1001,1,10,3,99]) == [1001,1,10,11,99]

#print(get_param_mode(1002))     
(run([3,225,1,225,6,6,1100,1,238,225,104,0,1101,90,60,224,1001,224,-150,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1,57,83,224,1001,224,-99,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1102,92,88,225,101,41,187,224,1001,224,-82,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,7,20,225,1101,82,64,225,1002,183,42,224,101,-1554,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1102,70,30,224,101,-2100,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,2,87,214,224,1001,224,-2460,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,102,36,180,224,1001,224,-1368,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1102,50,38,225,1102,37,14,225,1101,41,20,225,1001,217,7,224,101,-25,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,7,30,225,1102,18,16,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1006,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,359,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,108,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1008,677,677,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,464,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,494,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,509,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,569,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]))
