# Advanced-math-calculator-Python-
## An advanced mathematical calculator made using newton api and python.
# Instructions:
On running python file, it will ask for 2 inputs, **operation** and **expression**.  
**Operation**: Enter the operation you want to perform.  
**Expression**: Enter the expression which should is to be evaluated.  

| Operation |    API Endpoint   |       Result      |
|:---------:|:-----------------:|:-----------------:|
| Simplify  | /simplify/2^2+2(2)| 8                 |
| Factor    | /factor/x^2 + 2x  | x (x + 2)         |
| Derive    | /derive/x^2+2x    | 2 x + 2           |
| Integrate | /integrate/x^2+2x | 1/3 x^3 + x^2 + C |
| Find 0's  | /zeroes/x^2+2x    | [-2, 0]           |
| Find Tangent| /tangent/2lx^3  | 12 x + -16        |
| Area Under Curve| /area/2:4lx^3| 60               |
| Cosine    | /cos/pi            | -1                 |
| Sine      | /sin/0            | 0                 |
| Tangent   | /tan/0            | 0                 |
| Inverse Cosine    | /arccos/1            | 0                 |
| Inverse Sine    | /arcsin/0            | 0                 |
| Inverse Tangent    | /arctan/0            | 0                 |
| Absolute Value    | /abs/-1            | 1                 |  
| Logarithm | /log/2l8           | 3               |

### Character note:
1. In **find tangent** and **logarithm** vertical bar is used "|" (the character above backslash in keyboard).(Read special note for find tangent and log)
2. In ** area under curve** vertical bar "|" and colon ":" both are used.(Read special note for more info on area under curve)

### Special Note:
1. To find the **tangent line** of a function at a certain x value, enter expression as c|f(x) where c is the given x value and f(x) is the function expression, the separator is a vertical bar '|'. See the table above for an example request.
2. To find the **area under a function**, enter expression as c:d|f(x) where c is the starting x value, d is the ending x value, and f(x) is the function under which you want the curve between the two x values.
3. To compute **fractions**, enter expression as numerator(over)denominator. For example, to process 2/4 you must send in your expression as 2(over)4. The result expression will be in standard math notation (1/2, 3/4).  
4. To compute **logarithms**, enter base and value to be calculated separated by vertical bar "|". Expression should be of the form base|value.
# API:
[Newton API](https://github.com/aunyks/newton-api)
