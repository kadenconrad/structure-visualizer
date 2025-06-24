# Logarithms

## Binary Review
Since transistors exist in either the on (1) or off (0) state, computers use the binary *Base 2* system instead of the decimal, Base 10 system.

Just like in the regular base-10 number system, the 1s (ones) place is the *rightmost* position, so binary numbers are sometimes said to be read from *right* to *left*, but really it's just like our regular system with different place values!

### How are binary numbers calculated?
1. **Understanding Default Place Values**
Let's say *n* = place, i.e., 0 = the rightmost place; default place values are calculated as $2^n$.

Since the rightmost place is 0, it's place value is $2^0=1$. Next to it is $2^1=2$, then $2^2=4$, $2^3=8$, $2^4=16$, $2^5=32$, $2^6=64$, $2^7=128$, and so on... Notice with each place, the number is doubled. 

Looking at the difference between a broken down version of $2^2$ and $2^3$ can explain why:

$2\cdot 2$ vs $(2\cdot 2)\cdot 2$

**With each place, we multiply the last place value by 2.**

*This knowledge comes in handy with logarithms.*

---

2. **Calculating place values given a binary number**
This is done by computers, but a fundamental computer science concept to understand and comprehend.

Given a binary number, starting at the *rightmost* digit, multiply each number's value by it's place value.

Since binary numbers are made of 0s and 1s, each position will equal either *0* or it's default place value.

---

3. **Adding values for final result**
Add the results of each position together. 
 
*(We do this all the time with our regular number system. Think $528 = 500+20+8$)*

**Example**: 110110011
---
```math
|2^8=256|2^7=128|2^6=64|2^5=32|2^4=16|2^3=8|2^2=4|2^1=2|2^0=1|
```
---
```math
|2^8=256|2^7=128|2^6=64|2^5=32|2^4=16|2^3=8|2^2=4|2^1=2|2^0=1|
```
---
```math
(1\cdot256)+(1\cdot128)+(0\cdot64)+(1\cdot32)+(1\cdot16)+(0\cdot8)+(0\cdot4)+(1\cdot2)+(1\cdot1)=435
```
---
```math
110110011 = 435
```
---

### Logarithms in Computer Science
Logarithms ask a question; what do I need to power the base by to get *n*? And answer the question by determining **how many times the number needs to be divided by the base until it reaches 1.**

```math
log_2(8) => 2^3 = 8
```
**8 -> 4 -> 2 -> 1**</br>
*8* must be divided *3* times to get to 1

**If an algorithm's efficiency is determined by how many times something can be divided in half, it's complexity will be $log(n)$**

