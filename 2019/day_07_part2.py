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
        memory[args[2]] = int(a)+int(b)
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
    def __init__(self, inpt):
        self.stored_input = inpt
    def __call__(self, state, memory, args):
        if len(self.stored_input)>0:
            memory[args[0]] = self.stored_input.pop()
            #print(f"Go t input {memory[args[0]]}")
        else:                   
            memory[args[0]] = int(input("input>"))
        state.ip += self.params

class Outputter():
    optcode = 4
    params = 1
    def __init__(self, outpt):
        self.outpt=outpt
        
    def __call__(self, state, memory, args):
        a = memory[args[0]] if state.param_mode[0] else args[0]
        self.outpt.append(a)
        #print(f"Output {a}")
        #print(type(a))
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


class Computer():
    def __init__(self, memory):
        self.memory = memory
        self.state = State(ip = 0, halted = False)
        self.last_output = None
        
    def run(self, inpt):
        outpt=[]
    
        optcodes = {op.optcode: op() for op in [Adder, Timeser, Halter, JumpIfTrue, JumpIfFalse, LessThan, Equals]}
        optcodes[Inputter.optcode]= Inputter(inpt)
        optcodes[Outputter.optcode]=Outputter(outpt)
             

        for _ in range(0, 10000):
            #print("-"*25)
            #print(self.memory)
            optcode = self.memory[self.state.ip]
            #print(optcode)
            self.state.ip+=1

            operator = optcodes.get(optcode%100)
            self.state.param_mode = get_param_mode(optcode)
            if not operator:
                raise Exception(f"Bad optcode found {optcode}.")

            args = self.memory[self.state.ip:self.state.ip+operator.params]
        
                
            operator(self.state, self.memory, args)
            if outpt:
                self.last_output= outpt.pop()
                return self.last_output
            if self.state.halted:
                return self.last_output
            #print(self.memory) 
            
        raise("didn't finish in 10000 steps")


def main():
    import itertools
    print("Start")
    prog = [3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
    #prog =[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    #prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    #prog = [3,11,3,12,1,11,12,13,4,13,99,0,0,0]
    #prog = [3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
    #prog = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    m=0
    
    
    for p in itertools.permutations([5,6,7,8,9]):
        o=0
        c = [Computer([a for a in prog]) for _ in range(5)]

        for i in range(5):
                    o = c[i].run([o,p[i]])
                    
        while not c[4].state.halted:

            
            
                
                    
                for i in range(5):
                    o = c[i].run([o])
             
        m=max(m,o)
    print(m)
    



if __name__ == "__main__":
    main()



