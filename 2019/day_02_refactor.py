

class State():
    def __init__(self, ip, halted):
        self.ip = ip
        self.halted = halted


class Adder():
    optcode = 1
    params = 3
    def __call__(self, state, memory, args):
        assert len(args) == self.params
        memory[args[2]] = memory[args[0]] + memory[args[1]]
        state.ip += self.params

class Timeser():
    optcode = 2
    params = 3
    def __call__(self, state, memory, args):
        assert len(args) == self.params
        memory[args[2]] = memory[args[0]] * memory[args[1]]
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
        state.ip = memory[args[0]]
        

optcodes = {op.optcode: op() for op in [Adder, Timeser, Halter, Jump]}



def run(memory):

    state = State(ip = 0, halted = False)
    
    for _ in range(0, 10000):
        optcode = memory[state.ip]
        state.ip+=1

        operator = optcodes.get(optcode)
        if not operator:
            raise Exception(f"Bad optcode found {optcode}.")
        operator(state, memory, memory[state.ip:state.ip+operator.params])
        if state.halted:
            return memory
    raise("didn't finish in 10000 steps")




def test():
    prog_1 = [1,9,10,3,2,3,11,0,99,30,40,50]
    assert run(prog_1) == [3500,9,10,70,2,3,11,0,99,30,40,50]

    assert run([1,0,0,0,99]) == [2,0,0,0,99]
    assert run([2,3,0,3,99]) == [2,3,0,6,99]
    assert run([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert run([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

    
    
  
def part1():
    real_tape = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
    real_tape[1] = 12
    real_tape[2] = 2
    return run(real_tape)[0]
    
def part2():
    for noun in range(0,100):
        for verb in range(0,100):
            real_tape = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
            real_tape[1]=noun
            real_tape[2] =verb
            answer = run(real_tape)
            if answer[0] == 19690720:
                return (noun, verb)
                
if __name__ == "__main__":

    assert run([3,2,7,-1,-1,-1,-1,1,0,1,2,99]) == [3, 2, 5 , -1, -1, -1, -1, 1, 0, 1, 2, 99]
    test()
    
    print(part1())
    print(part2())
