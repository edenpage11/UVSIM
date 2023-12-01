program_running = True
user_inputing = True
memory = { i : None for i in range(100) }
program_counter = 0
accumulator = None

class command:
    def __init__(self, word):
        self.operation = word[:2]
        self.memLoc = int(word[2:])


class IOops(command):
    def __init__(self, word):
        command.__init__(self, word)
    
    def run(self):
        if self.operation[1] == "0":
            self.read(self.memLoc)
        elif self.operation[1] == "1":
            self.write(self.memLoc)
    # 10 read keyboard input into mem location. all function parameters are int's.
    # in: location in memory int  user input string // out: val at LIM == user input int 
    # prompts user to input a number then stores at LIM defined with function call from main
    def read(self, mem):
        word = input(f"enter value to store in memory location {str(mem)}: ")
        global memory
        # Replace input with something that calls it from the command line text box in the GUI

        if word.isdigit():
            word = int(word)
            memory[mem] = word
        elif word[0] == '-' and word[1:].isdigit():
            word = int(word)
            memory[mem] = word
        else:
            print('-----Error:Only input numbers, Try again.-----')
            IOops.read(self, mem)

    # 11 write mem location to screen.
    # in: location in memory int and value at LIM int // out: val at LIM int == to screen
    # takes LIM that was defined with the function call at the beginning and prints the value there
    def write(self, mem):
        if int(mem) < 0:
            raise AssertionError
        word = memory[mem]
        print(word)
        #change from print to send to GUI

class LSops(command):
    def __init__(self, word):
        command.__init__(self, word)
    
    def run(self):
        if self.operation[1] == "0":
            self.load(self.memLoc)
        elif self.operation[1] == "1":
            self.store(self.memLoc)
    # 20 load from mem location into accumulator.
    # in: location in memory int and value at location int // out: accumulator == word from that LIM int
    # accesses memory at location specified with function call and sets accumulator to hold it
    def load(self, mem):
        global accumulator
        global memory
        word = memory[mem]
        accumulator = word

    # 21 store accumulator val into memory.
    # in: location in memory int accumulator int// out: value at LIM == word from accumulator int
    # sets memory at location specified with function call to hold word from accumulator
    def store(self, mem):
        global accumulator
        global memory
        word = accumulator
        memory[mem] = word

class arithmetic(command):
    def __init__(self, word):
        command.__init__(self, word)

    def run(self):
        if self.operation[1] == "0":
            self.add(self.memLoc)
        elif self.operation[1] == "1":
            self.subtract(self.memLoc)
        elif self.operation[1] == "2":
            self.divide(self.memLoc)
        elif self.operation[1] == "3":
            self.multiply(self.memLoc)
    # 30 add accumulator and val in memory.
    # in: location in memory int accumulator int // out: word in acc += word from LIM int
    # adds ints from accumulator and location in memory then stores in the accumulator
    def add(self, mem):
        global accumulator
        y = memory[mem]
        word = accumulator + y
        # need to handle overflow if word > 9999 here - Eden Barlow
        if word > 9999:
            temp = word - 9999
            word = -9999 + temp
        accumulator = word

    # 31 subtract val in memory from accumulator.
    # in: location in memory int accumulator int // out: word in acc -= word from LIM int
    # subtracts ints from LIM from int in accumulator then stores in the accumulator
    def substract(self, mem):
        global accumulator
        x = accumulator
        y = memory[mem]
        word = x - y
        #need to handle overflow if word < -9999 here - Eden Barlow
        if word < -9999:
            temp = word + 9999
            word = 9999 + temp
        accumulator = word

    # 32 divide accumulator by value in memory.
    # in: location in memory int accumulator int // out: word in acc /= word from LIM int
    # divides int in accumulator by ints from LIM then stores in the accumulator
    def divide(self, mem):
        global accumulator
        x = accumulator
        y = memory[mem]
        word = x // y
        accumulator = word

    # 33 multiply memory value with accumulator.
    # in: location in memory int accumulator int // out: word in acc *= word from LIM int
    # multiplies ints from accumulator and location in memory then stores in the accumulator
    def multiply(self, mem):
        global accumulator
        x = accumulator
        y = memory[mem]
        word = x * y
        # need to handle overflow while word > 9999 here - Eden Barlow
        while word > 9999:
            temp = word - 9999
            word = -9999 + temp
        #need to handle overflow while word < -9999 here - Eden Barlow
        while word < -9999:
            temp = word + 9999
            word = 9999 + temp
        accumulator = word

class BRops(command):
    def __init__(self, word):
        command.__init__(self, word)

    def run(self):
        if self.operation[1] == "0":
            self.branch(self.memLoc)
        elif self.operation[1] == "1":
            self.branchneg(self.memLoc)
        elif self.operation[1] == "2":
            self.branchzero(self.memLoc)
        elif self.operation[1] == "3":
            self.halt()
    # 40 branch to specific location in memory.
    # in: destination int // out: program counter = destination int
    # Go to a specified location in memory (if command is there it will run)
    def branch(self, destination):
        if destination < 0 or destination > 99:
            # print("Error: You are trying to branch to a location outside of memory.")
            # halt()
            pass
        else:
            global program_counter
            program_counter = destination

    # 41 Branch to location if accumulator is negative. 
    # in: destination int accumulator int // out: program counter = destination int
    # Go to a specified location in memory (if command is there it will run) but only if val in acc is negative
    def branchneg(self, destination):
        global program_counter, accumulator
        if accumulator < 0:
            program_counter = destination

    # 42 Branch to location if accumulator is 0.
    # in: destination int accumulator int// out: program counter = destination int
    # Go to a specified location in memory (if command is there it will run) but only if val in acc is 0
    def branchzero(self, destination):
        global program_counter, accumulator
        if accumulator == 0:
            program_counter = destination

    # 43 Pause the program. no parameter.
    # in: program_running = true bool// out: program_running = false bool
    # when called, the program pauses running because variable is set to false
    def halt(self):
        global program_running
        print('-----Halting Program-----')
        program_running = False

# run 1 line at a time
def step_in():
    global program_counter 
    global memory
    global accumulator
    command = memory[program_counter]
    accumulator = command.run()
    program_counter += 1
    return accumulator

def run_all():
    global program_counter
    global program_running
    global memory
    global accumulator
    while program_running:
        memory[program_counter].run()
        program_counter += 1        
        if memory[program_counter] == None:
            program_running = False
    return memory
     

# take commands from GUI and load them in memory
def load_commands(commands):
    index_input = 0
    global memory
    for command in commands:
        if command[0] == "1":
            memory[index_input] = IOops(command)
        elif command[0] == "2":
            memory[index_input] = LSops(command)
        elif command[0] == "3":
            memory[index_input] = arithmetic(command)
        elif command[0] == "4":
            memory[index_input] = BRops(command)
        index_input += 1
    return memory

def main():
    pass
    # inputs = ["1010","1110", "1011", "2010", "3010", "2112", "1112"]
    # load_commands(inputs)
    # run_all()
    # should ask for input 2 times then print those values added
    # results: 
    #     enter value to store in memory location 10: 1111
    #     enter value to store in memory location 11: 1111
    #     2222

    # implemented 2 memories to handle 
    # memory2 = {0: 00}
    # memory1 = {0: None}
    # memory1[0] = 1234
    # memory2[0] = 23
    # print(int(str(memory2[0]) + str(memory1[0])))
    
        
main()