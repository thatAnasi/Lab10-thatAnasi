# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))

            return stack.pop()


def decode_string(s):
    # Outline:
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)

        elif char == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0

        elif char == "]":
            previous_string, repeat_count = stack.pop()
            current_string = previous_string + current_string * repeat_count

        else:
            current_string += char

        return current_string


def daily_temperatures(temps):
    # Outline:
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
