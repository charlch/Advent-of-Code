from computer import Process

assert Process([1101,1,2,5,99,0]).run().memory == [1101,1,2,5,99,3]
