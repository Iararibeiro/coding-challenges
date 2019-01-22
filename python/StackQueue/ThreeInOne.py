# Problem: use one array to implement three stacks
class ThreeInOneStack:

    def __init__(self, number_of_stacks, stack_capacity):
        self.number_of_stacks = number_of_stacks
        self.stack_capacity = stack_capacity
        self.values = [None] * (self.stack_capacity * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks

    def isFull(self, stack_number):
        if stack_number > self.number_of_stacks:
            return "Index out of range"
        if self.sizes[(stack_number)] < self.stack_capacity:
            return False
        return True

    def indexOfTop(self, stack_number):
        offset = stack_number * self.stack_capacity
        size = sizes[stack_number]

        return offset + size

    def push(self, value):
        #include the value in the stack with more space
        #if the stack number isnt given, if the stack choose is full
        #the value is added to the one with more space
        smaller_stack = self.sizes.index(min(self.sizes))

        if isFull(smaller_stack):
            return False

        self.values[indexOfTop(smaller_stack)] = value;
        self.sizes[smaller_stack] += 1;

    def pop(self):
        #remove the value from the bigger stack
        return None
