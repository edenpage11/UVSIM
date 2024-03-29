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
        global accumulator
        word = str(accumulator)
        global memory
        # Replace input with something that calls it from the command line text box in the GUI
        if word.isdigit():
            word = int(word)
            memory[mem] = word
        elif word[0] == '-' and word[1:].isdigit():
            word = int(word)
            memory[mem] = word
        else:
            raise(TypeError)

    # 11 write mem location to screen.
    # in: location in memory int and value at LIM int // out: val at LIM int == to screen
    # takes LIM that was defined with the function call at the beginning and prints the value there
    def write(self, mem):
        global accumulator
        if int(mem) < 0:
            raise AssertionError
        accumulator = memory[mem]

class LSops(command):
    def __init__(self, word):
        command.__init__(self, word)
    
    def run(self):
        if self.operation[1] == "0":
            self.load(self.memLoc)
        elif self.operation[1] == "1":
            self.store(self.memLoc)
        else: 
            return "invalid command"
        return None
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
            error = self.add(self.memLoc)
        elif self.operation[1] == "1":
            error = self.subtract(self.memLoc)
        elif self.operation[1] == "2":
            error = self.divide(self.memLoc)
        elif self.operation[1] == "3":
            error = self.multiply(self.memLoc)
        else: 
            error = "invalid command"
        return error
    # 30 add accumulator and val in memory.
    # in: location in memory int accumulator int // out: word in acc += word from LIM int
    # adds ints from accumulator and location in memory then stores in the accumulator
    def add(self, mem):
        error = None
        global accumulator
        y = memory[mem]
        word = accumulator + y
        # need to handle overflow if word > 9999 here - Eden Barlow
        while word > 9999:
            temp = word - 9999
            word = -9999 + temp
            error = "----- OVERFLOW -----"
        while word < -9999:
            temp = word + 9999
            word = 9999 + temp
            error = "----- UNDERFLOW -----"
        accumulator = word
        return error

    # 31 subtract val in memory from accumulator.
    # in: location in memory int accumulator int // out: word in acc -= word from LIM int
    # subtracts ints from LIM from int in accumulator then stores in the accumulator
    def subtract(self, mem):
        error = None
        global accumulator
        x = accumulator
        y = memory[mem]
        word = x - y
        #need to handle overflow if word < -9999 here - Eden Barlow
        while word > 9999:
            temp = word - 9999
            word = -9999 + temp
            error = "----- OVERFLOW -----"
        while word < -9999:
            temp = word + 9999
            word = 9999 + temp
            error = "----- UNDERFLOW -----"
        accumulator = word
        return error

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
        error = None
        global accumulator
        x = accumulator
        y = memory[mem]
        word = x * y
        # need to handle overflow while word > 9999 here - Eden Barlow
        while word > 9999:
            temp = word - 9999
            word = -9999 + temp
            error = "----- OVERFLOW -----"
        while word < -9999:
            temp = word + 9999
            word = 9999 + temp
            error = "----- UNDERFLOW -----"
        accumulator = word
        return error

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
        else: 
            return "invalid command"
        return None
    # 40 branch to specific location in memory.
    # in: destination int // out: program counter = destination int
    # Go to a specified location in memory (if command is there it will run)
    def branch(self, destination):
        if destination < 0 or destination > 99:
            return "Error: You are trying to branch to a location outside of memory."
            self.halt()
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
        program_running = False
        return "-----Halting Program-----"

# run 1 line at a time
def step_in():
    global program_running
    if program_running:
        curr_command = memory[program_counter]
        curr_command.run()
        program_counter += 1
    return memory
     

# take commands from GUI and load them in memory
def load_commands(commands):
    errors = []
    index_input = 0
    global memory
    for command in commands:
        if (command[0] == "1") and (command[1] == "0" or command[1] == "1"):
            memory[index_input] = IOops(command)
        elif (command[0] == "2") and (command[1] == "0" or command[1] == "1"):
            memory[index_input] = LSops(command)
        elif (command[0] == "3") and (command[1] == "0" or command[1] == "1" or command[1] == "2" or command[1] == "3"):
            memory[index_input] = arithmetic(command)
        elif (command[0] == "4") and (command[1] == "0" or command[1] == "1" or command[1] == "2" or command[1] == "3"):
            memory[index_input] = BRops(command)
        else:
            errors.append(f"Invalid command on line {index_input}. Command ignored\n")
            index_input -= 1
        index_input += 1
    return errors

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