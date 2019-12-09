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
    def __init__(self, inpt=[]):
        self.stored_input = inpt
    def __call__(self, state, memory, args):
        if len(self.stored_input)>0:
            memory[args[0]] = self.stored_input.pop()
        else:                   
            memory[args[0]] = int(input("input>"))
        state.ip += self.params

class Outputter():
    optcode = 4
    params = 1
    def __init__(self, outpt=[]):
        self.outpt=outpt
        
    def __call__(self, state, memory, args):
        a = memory[args[0]] if state.param_mode[0] else args[0]
        self.outpt.append(a)
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
    

def get_param_mode(optcode):
    soptcode = "00000000"+str(optcode)[0:-2]
    #print(soptcode)
    out = []
    for p in range(0,4):
        #print(soptcode[-1-p])
        out.append( soptcode[-1-p] == "0")
    return out


def run(memory, inpt=[]):

    outpt=[]
    
    optcodes = {op.optcode: op() for op in [Adder, Timeser, Halter, JumpIfTrue, JumpIfFalse, LessThan, Equals]}
    optcodes[Inputter.optcode]= Inputter(inpt)
    optcodes[Outputter.optcode]=Outputter(outpt)
             

    
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
            return outpt
    raise("didn't finish in 10000 steps")


def main():
    import itertools
    print("Start")
    prog = [3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
    #prog =[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    m=0
    for p in itertools.permutations([0,1,2,3,4]):
        o = run([a for a in prog], [0,p[0]])[0]
        o = run([a for a in prog], [o,p[1]])[0]
        o = run([a for a in prog], [o,p[2]])[0]
        o = run([a for a in prog], [o,p[3]])[0]
        o = run([a for a in prog], [o,p[4]])[0]
        m=max(o,m)
    print(m)
    



if __name__ == "__main__":
    main()



