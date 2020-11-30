def run(tape):
    i = 0 # op start point
    while range(0,10000):
        if tape[i] == 1:
            tape[tape[i+3]] = tape[tape[i+2]] + tape[tape[i+1]]
        elif tape[i] == 2:
            tape[tape[i+3]] = tape[tape[i+2]] * tape[tape[i+1]]
        elif tape[i] == 99:
            return tape
        else:
            raise("Error bad optcode")
        i+=4
    raise("didn't finish")


def example1():
    prog_1 = [1,9,10,3,2,3,11,0,99,30,40,50]
    return run(prog_1)
    
  
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
    print(part1())
    print(part2())