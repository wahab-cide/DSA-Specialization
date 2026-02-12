/* 
 * CS237 Lab 1: Bitpuzzles
 * 
 * <Please put your name and userid here>
 * 
 * bits.c - Source file with your solutions to the Lab.
 *          This is the file you will hand in to your instructor.
 *
 * WARNING: Do not include the <stdio.h> header; it confuses the dlc
 * compiler. You can still use printf for debugging without including
 * <stdio.h>, although you might get a compiler warning. In general,
 * it's not good practice to ignore compiler warnings, but in this
 * case it's OK.  
 */

#if 0 // This is called a "preprocessor directive". All code between
      // this "#if 0" and the "#endif" will be ignored.
/*
 * Instructions to Students:
 *
 * STEP 1: Read the following instructions carefully.
 */

You will provide your solution to the Data Lab by
editing the collection of functions in this source file.

INTEGER CODING RULES:
 
  Replace the "return" statement in each function with one
  or more lines of C code that implements the function. Your code 
  must conform to the following style:
 
  int Funct(arg1, arg2, ...) {
      /* brief description of how your implementation works */
      int var1 = Expr1;
      ...
      int varM = ExprM;

      varJ = ExprJ;
      ...
      varN = ExprN;
      return ExprR;
  }

  Each "Expr" is an expression using ONLY the following:
  1. Integer constants 0 through 255 (0xFF), inclusive. You are
      not allowed to use big constants such as 0xffffffff.
  2. Function arguments and local variables (no global variables).
  3. Unary integer operations ! ~
  4. Binary integer operations & ^ | + << >>
    
  Some of the problems restrict the set of allowed operators even further.
  Each "Expr" may consist of multiple operators. You are not restricted to
  one operator per line.

  You are expressly forbidden to:
  1. Use any control constructs such as if, do, while, for, switch, etc.
  2. Define or use any macros.
  3. Define any additional functions in this file.
  4. Call any functions.
  5. Use any other operations, such as &&, ||, -, or ?:
  6. Use any form of casting.
  7. Use any data type other than int.  This implies that you
     cannot use arrays, structs, or unions.

 
  You may assume that your machine:
  1. Uses 2s complement, 32-bit representations of integers.
  2. Performs right shifts arithmetically.
  3. Has unpredictable behavior when shifting an integer by more
     than the word size.

EXAMPLES OF ACCEPTABLE CODING STYLE:
  /*
   * pow_2_plus_1 - returns 2^x + 1, where 0 <= x <= 31
   */
  int pow_2_plus_1(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     return (1 << x) + 1;
  }

  /*
   * pow_2_plus_4 - returns 2^x + 4, where 0 <= x <= 31
   */
  int pow_2_plus_4(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     int result = (1 << x);
     result += 4;
     return result;
  }

FLOATING POINT CODING RULES

For the problems that require you to implent floating-point operations,
the coding rules are less strict.  You are allowed to use looping and
conditional control.  You are allowed to use both ints and unsigneds.
You can use arbitrary integer and unsigned constants.

You are expressly forbidden to:
  1. Define or use any macros.
  2. Define any additional functions in this file.
  3. Call any functions.
  4. Use any form of casting.
  5. Use any data type other than int or unsigned.  This means that you
     cannot use arrays, structs, or unions.
  6. Use any floating point data types, operations, or constants.


NOTES:
  1. Use the dlc (data lab checker) compiler (described in the handout) to 
     check the legality of your solutions.
  2. Each function has a maximum number of operators (! ~ & ^ | + << >>)
     that you are allowed to use for your implementation of the function. 
     The max operator count is checked by dlc. Note that '=' is not 
     counted; you may use as many of these as you want without penalty.
  3. Use the btest test harness to check your functions for correctness.
  4. Use the BDD checker to formally verify your functions
  5. The maximum number of ops for each function is given in the
     header comment for each function. If there are any inconsistencies 
     between the maximum ops in the writeup and in this file, consider
     this file the authoritative source.

/*
 * STEP 2: Modify the functions below, according the coding rules.
 * 
 *   IMPORTANT. TO AVOID GRADING SURPRISES:
 *   1. Use the dlc compiler to check that your solutions conform
 *      to the coding rules.
 *   2. Use the BDD checker to formally verify that your solutions produce 
 *      the correct answers.
 */


#endif
/* Copyright (C) 1991-2024 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <https://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 10.0.0.  Version 10.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2017, fifth edition, plus
   the following additions from Amendment 1 to the fifth edition:
   - 56 emoji characters
   - 285 hentaigana
   - 3 additional Zanabazar Square characters  */

    

/*****************************************
 ********* BEGIN STUDENT CODE ************
 *****************************************/
		      
// bit puzzles

/* 
 * bitwise_and - x&y using only ~ and | 
 *   Example: bitwise_and(6, 5) = 4
 *   Legal ops: ~ |
 *   Max ops: 8
 *   Rating: 1
 */
int bitwise_and(int x, int y) {
  /*
   * DE MORGAN'S LAW from boolean algebra:
   *   A AND B  =  NOT( NOT(A) OR NOT(B) )
   *
   * Proof with a truth table (for each pair of bits):
   *   x  y  | ~x  ~y  | ~x|~y  | ~(~x|~y) | x&y
   *   0  0  |  1   1  |   1    |    0      |  0
   *   0  1  |  1   0  |   1    |    0      |  0
   *   1  0  |  0   1  |   1    |    0      |  0
   *   1  1  |  0   0  |   0    |    1      |  1
   *
   * Last two columns match! So ~(~x | ~y) == x & y.
   * This works bitwise — each of the 32 bit positions is independent.
   */
  return ~(~x | ~y);
}

/* 
 * set_third_bits - return word with every third bit (starting from the LSB) set to 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 8
 *   Rating: 1
 */
int set_third_bits(void) {
  /*
   * We need a 1 at every 3rd bit position: bits 0, 3, 6, 9, ..., 30.
   * The full 32-bit pattern looks like:
   *   01001001 00100100 10010010 01001001
   *   bit 31                          bit 0
   *
   * We can't use big constants (max 0xFF), so we build it in pieces.
   *
   * Step 1: Start with 0x49 = 01001001 in binary.
   *         This has 1s at bit positions 0, 3, 6 — the first 3 hits.
   *
   * Step 2: x | (x << 9)
   *         Shifting left by 9 copies our pattern to positions 9, 12, 15.
   *         OR combines both, giving us bits 0,3,6,9,12,15.
   *
   *         Why 9? Because we have 3 bits set (at 0,3,6), and the next
   *         one we need is at 9 — exactly 9 positions up from bit 0.
   *
   * Step 3: x | (x << 18)
   *         Now x covers bits 0-15. Shifting by 18 copies them to 18-33.
   *         OR gives us bits 0,3,6,9,12,15,18,21,24,27,30. Done!
   *         (Bits above 31 just fall off the top — no problem.)
   */
  int x = 0x49;
  x = x | (x << 9);
  x = x | (x << 18);
  return x;
}

/* 
 * is_any_even_bit_set - return 1 if any even-numbered bit in word set to 1
 *   Examples is_any_even_bit_set(0xA) = 0, is_any_even_bit_set(0xE) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 12
 *   Rating: 2
 */
int is_any_even_bit_set(int x) {
  /*
   * Even-numbered bits are positions 0, 2, 4, 6, 8, ..., 30.
   * We need a mask with 1s at all even positions: 0101 0101 ... = 0x55555555
   *
   * Building the mask (can't use constants bigger than 0xFF):
   *   0x55           = 01010101                           (8 bits)
   *   0x55 | (0x55 << 8)  = 01010101 01010101             (16 bits)
   *   that | (that << 16) = 01010101 01010101 01010101 01010101  (32 bits)
   *
   * Then: x & mask
   *   This zeros out all ODD bits, keeping only even bits.
   *   If ANY even bit was set, the result is non-zero.
   *
   * Then: !!(x & mask)
   *   ! (logical NOT) turns non-zero into 0, and 0 into 1.
   *   !! (double NOT) turns non-zero into 1, and 0 stays 0.
   *   This is the standard trick to convert any value to 0 or 1.
   */
  int mask = 0x55;
  mask = mask | (mask << 8);
  mask = mask | (mask << 16);
  return !!(x & mask);
}

/* 
 * rotate_left - Rotate x to the left by n
 *   Can assume that 0 <= n <= 31
 *   Examples: rotate_left(0x87654321,4) = 0x76543218
 *   Legal ops: ~ & ^ | + << >> !
 *   Max ops: 25
 *   Rating: 3 
 */
int rotate_left(int x, int n) {
  /*
   * Rotation means bits that fall off the left end wrap to the right.
   * Example: rotate_left(0x87654321, 4) = 0x76543218
   *   The top 4 bits (0x8 = 1000) wrap around to become the bottom 4 bits.
   *
   * We split this into two parts and OR them together:
   *
   *   LEFT PART:  x << n
   *     Shifts everything left by n. The bottom n bits become 0.
   *     The top n bits are lost (that's what we recover in the right part).
   *
   *   RIGHT PART: the top n bits of original x, moved to the bottom
   *     We need to shift right by (32 - n) to move them down.
   *
   *     Computing 32 - n without minus:
   *       In two's complement: -n = ~n + 1
   *       So: 32 - n = 32 + ~n + 1 = 33 + ~n
   *
   *     Problem: x >> (32-n) on a signed int does ARITHMETIC right shift,
   *     which copies the sign bit into the vacated positions.
   *     Example: 0x87654321 >> 28 = 0xFFFFFFF8 (not 0x00000008!)
   *
   *     Fix: mask off the junk with ~(~0 << n)
   *       ~0         = 0xFFFFFFFF (all 1s)
   *       ~0 << n    = 1s in top (32-n) bits, 0s in bottom n bits
   *       ~(~0 << n) = 0s in top, 1s in bottom n bits (keeps only bottom n)
   *
   *     Edge case n=0: ~(~0 << 0) = ~(~0) = 0, so right part = 0. Correct!
   *     (Also avoids shifting by 32, which is undefined behavior in C.)
   */
  int shift = 33 + ~n;
  int left = x << n;
  int right = (x >> shift) & ~(~0 << n);
  return left | right;
}

/*
 * bitwise_parity - returns 1 if x contains an odd number of 0's
 *   Examples: bitwise_parity(5) = 0, bitwise_parity(7) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 20
 *   Rating: 4
 */
int bitwise_parity(int x) {
  /*
   * Parity = 1 if there's an odd number of 1-bits in x.
   * (Odd number of 0s <=> odd number of 1s, since 32 is even.)
   *
   * Key insight: XOR preserves parity.
   *   XOR of two bits = 1 if they differ, 0 if same.
   *   So a ^ b has the same parity (odd/even count of 1s) as
   *   the combined bits of a and b together.
   *
   * We "fold" the number in half repeatedly using XOR:
   *
   *   Step 1: x ^ (x >> 16)
   *     XOR the top 16 bits with the bottom 16 bits.
   *     Now the parity of all 32 bits is captured in the bottom 16.
   *
   *   Step 2: x ^ (x >> 8)
   *     Fold 16 bits into 8. Parity now in bottom 8 bits.
   *
   *   Step 3: x ^ (x >> 4)   -> parity in bottom 4 bits
   *   Step 4: x ^ (x >> 2)   -> parity in bottom 2 bits
   *   Step 5: x ^ (x >> 1)   -> parity in bottom 1 bit
   *
   * Example with 8 bits: x = 01101001 (four 1s -> even parity -> answer 0)
   *   Fold by 4: 0110 ^ 1001 = 1111
   *   Fold by 2: 11 ^ 11 = 00
   *   Fold by 1: 0 ^ 0 = 0
   *   Result: 0 (even parity). Correct!
   *
   * Finally: x & 1 extracts just bit 0, which holds the answer.
   */
  x = x ^ (x >> 16);
  x = x ^ (x >> 8);
  x = x ^ (x >> 4);
  x = x ^ (x >> 2);
  x = x ^ (x >> 1);
  return x & 1;
}


// twos complement puzzles

/*
 * is_tcomp_max - returns 1 if x is the maximum, two's complement number,
 *     and 0 otherwise 
 *   Legal ops: ! ~ & ^ | +
 *   Max ops: 10
 *   Rating: 1
 */
int is_tcomp_max(int x) {
  /*
   * Tmax (maximum 32-bit two's complement) = 0x7FFFFFFF = 2,147,483,647
   *   In binary: 0 followed by 31 ones = 01111111...1111
   *
   * Key property of Tmax:
   *   Tmax + 1 = Tmin = 0x80000000 (overflows to most negative number)
   *   Tmax + Tmax + 1 = 0x7FFFFFFF + 0x80000000 = 0xFFFFFFFF = all 1s = ~0
   *
   * So if x is Tmax, then (x + x + 1) should be ~0 (all 1s).
   * We check: ~(x + x + 1) should be 0, so !(~(x+x+1)) should be 1.
   *
   * BUT there's a trap: x = -1 = 0xFFFFFFFF also passes this test!
   *   -1 + -1 + 1 = -1 = 0xFFFFFFFF = ~0. That also gives !(~sum) = 1.
   *
   * To exclude -1: if x = -1, then ~x = 0. So !!(~x) = 0.
   *   For Tmax: ~x = 0x80000000 (non-zero), so !!(~x) = 1.
   *
   * Final: !(~sum) & not_neg1
   *   Both must be 1. Only Tmax satisfies both conditions.
   *
   *   x = Tmax:  sum = ~0, !(~sum) = 1, !!(~x) = 1 -> 1 & 1 = 1
   *   x = -1:    sum = ~0, !(~sum) = 1, !!(~x) = 0 -> 1 & 0 = 0
   *   x = other: sum != ~0, !(~sum) = 0             -> 0 & ? = 0
   */
  int sum = x + x + 1;
  int not_neg1 = !!(~x);
  return !(~sum) & not_neg1;
}

/* 
 * get_sign - return 1 if positive, 0 if zero, and -1 if negative
 *  Examples: get_sign(130) = 1
 *            get_sign(-23) = -1
 *  Legal ops: ! ~ & ^ | + << >>
 *  Max ops: 10
 *  Rating: 2
 */
int get_sign(int x) {
    /*
     * We need: positive -> 1, zero -> 0, negative -> -1
     *
     * Two building blocks:
     *
     *   (x >> 31) — ARITHMETIC right shift by 31:
     *     Copies the sign bit (bit 31) into ALL 32 positions.
     *     If x is negative: sign bit = 1, so x >> 31 = 0xFFFFFFFF = -1
     *     If x is zero or positive: sign bit = 0, so x >> 31 = 0x00000000 = 0
     *
     *   !!x — double logical NOT:
     *     !x  = 1 if x is 0, else 0
     *     !!x = 0 if x is 0, else 1
     *     So: non-zero -> 1, zero -> 0
     *
     * Combining with OR:
     *   Negative: (x >> 31) | (!!x) = (-1) | 1
     *     -1 = 0xFFFFFFFF, 1 = 0x00000001
     *     0xFFFFFFFF | 0x00000001 = 0xFFFFFFFF = -1
     *
     *   Positive: 0 | 1 = 1
     *
     *   Zero:     0 | 0 = 0
     */
    return (x >> 31) | (!!x);
}

/* 
 * negate - return -x 
 *   Example: negate(1) = -1.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int negate(int x) {
  /*
   * Two's complement negation: -x = ~x + 1 (flip all bits, add 1)
   *
   * Why this works mathematically:
   *   ~x flips every bit. For any integer: x + ~x = 0xFFFFFFFF = -1
   *   (every bit position has one 0 and one 1, so OR/addition gives all 1s)
   *
   *   So: x + ~x = -1
   *       ~x = -1 - x
   *       ~x + 1 = -x
   *
   * Example with 8 bits:
   *   x  =  5 = 00000101
   *   ~x     = 11111010
   *   ~x + 1 = 11111011 = -5 in two's complement
   *
   * Verify: 00000101 + 11111011 = 100000000 (the 1 overflows, leaving 0)
   */
  return ~x + 1;
}

/* 
 * is_sub_ok - Determine if can compute x-y without overflow
 *   Example: is_sub_ok(0x80000000,0x80000000) = 1,
 *            is_sub_ok(0x80000000,0x70000000) = 0, 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 20
 *   Rating: 3
 */
int is_sub_ok(int x, int y) {
  /*
   * Subtraction overflow can ONLY happen when x and y have DIFFERENT signs.
   *   - positive - negative = could overflow to negative (too large)
   *   - negative - positive = could overflow to positive (too small)
   *   - same signs: the difference is always smaller than either operand, safe.
   *
   * When overflow DOES happen, the result has the WRONG sign:
   *   - positive - negative overflows: result is negative (should be positive)
   *   - negative - positive overflows: result is positive (should be negative)
   *   So the result's sign differs from x's sign.
   *
   * Algorithm:
   *   1. Compute x - y as x + (~y + 1) since we can't use the minus operator.
   *      This works because -y = ~y + 1 (two's complement negation).
   *
   *   2. diff_signs = (x ^ y) >> 31
   *      XOR: bit 31 is 1 if x and y have different sign bits.
   *      >> 31: spreads that bit to all 32 positions (0x00000000 or 0xFFFFFFFF).
   *
   *   3. result_bad = (x ^ diff) >> 31
   *      XOR: bit 31 is 1 if x and the result have different sign bits.
   *      >> 31: spreads it (0x00000000 or 0xFFFFFFFF).
   *
   *   4. Overflow = diff_signs AND result_bad (both must be true).
   *      We want to return 1 when there's NO overflow: !(overflow)
   *
   * Example: is_sub_ok(0x80000000, 0x70000000)
   *   x = Tmin (negative), y = positive -> different signs
   *   diff = Tmin + (~0x70000000 + 1) = Tmin + 0x90000000 = 0x10000000 (positive!)
   *   Result is positive but x is negative -> overflow! Returns 0.
   */
  int diff = x + ~y + 1;
  int diff_signs = (x ^ y) >> 31;
  int result_bad = (x ^ diff) >> 31;
  return !(diff_signs & result_bad);
}

/*
 * is_pow_2 - returns 1 if x is a power of 2, and 0 otherwise
 *   Examples: is_pow_2(5) = 0, is_pow_2(8) = 1, is_pow_2(0) = 0
 *   Note that no negative number is a power of 2.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 20
 *   Rating: 4
 */
int is_pow_2(int x) {
  /*
   * A power of 2 in binary has EXACTLY one bit set:
   *   1 = 00000001,  2 = 00000010,  4 = 00000100,  8 = 00001000, etc.
   *
   * The classic trick: x & (x - 1) == 0 means exactly one bit is set.
   *
   * Why? Subtracting 1 flips the lowest set bit and all bits below it:
   *   x     = 00001000  (8)
   *   x - 1 = 00000111  (7)
   *   x & (x-1) = 00000000   -> power of 2!
   *
   *   x     = 00001010  (10, not a power of 2)
   *   x - 1 = 00001001  (9)
   *   x & (x-1) = 00001000   -> non-zero, NOT a power of 2.
   *
   * In this lab we can't use minus, so: x - 1 = x + (~1 + 1) = x + ~0
   *   Because ~0 = 0xFFFFFFFF = -1, and x + (-1) = x - 1.
   *
   * Three conditions (all must be true):
   *   1. not_zero: !!x     -> 0 is not a power of 2
   *   2. one_bit:  !(x & (x + ~0))  -> the x & (x-1) trick
   *   3. positive: !(x >> 31)  -> negative numbers are not powers of 2
   *      (e.g. 0x80000000 has one bit set but is -2147483648, not 2^31)
   *
   * Since each condition is 0 or 1, we can use & (bitwise AND) to
   * combine them — it works like && when both sides are single bits.
   */
  int not_zero = !!x;
  int one_bit = !(x & (x + ~0));
  int positive = !(x >> 31);
  return not_zero & one_bit & positive;
}


// floating point puzzles

/* 
 * float_abs_val - Return bit-level equivalent of absolute value of f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representations of
 *   single-precision floating point values.
 *   When argument is NaN, return argument..
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 10
 *   Rating: 2
 */
unsigned float_abs_val(unsigned uf) {
  /*
   * IEEE 754 single-precision float layout (32 bits):
   *   [1 sign] [8 exponent] [23 mantissa/fraction]
   *   bit 31   bits 30-23   bits 22-0
   *
   * Absolute value = just clear the sign bit (bit 31).
   *   0x7FFFFFFF = 0 followed by 31 ones
   *   uf & 0x7FFFFFFF zeroes bit 31, keeps everything else.
   *
   * Special case: NaN (Not a Number)
   *   NaN has exponent = all 1s (0xFF) AND mantissa != 0.
   *   In bit terms: bits 30-23 are all 1, and at least one of bits 22-0 is 1.
   *   The spec says: if NaN, return the original argument unchanged.
   *
   *   0x7F800000 = 0 11111111 00000000000000000000000 = +infinity
   *   Anything with cleared sign bit GREATER than 0x7F800000 has
   *   exponent=0xFF and non-zero mantissa, which means it's NaN.
   *
   * So: clear sign bit first. If the result > 0x7F800000, it was NaN —
   * return the original (with sign bit intact).
   */
  unsigned result = uf & 0x7FFFFFFF;
  if (result > 0x7F800000)
    return uf;
  return result;
}

/* 
 * float_div_2 - Return bit-level equivalent of expression 0.5*f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representation of
 *   single-precision floating point values.
 *   When argument is NaN, return argument
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 30
 *   Rating: 4
 */
unsigned float_div_2(unsigned uf) {
  /*
   * IEEE 754 float recap:
   *   [sign 1 bit] [exponent 8 bits] [fraction 23 bits]
   *
   *   Normalized (exp 1-254): value = (-1)^sign * 1.fraction * 2^(exp-127)
   *   Denormalized (exp = 0): value = (-1)^sign * 0.fraction * 2^(-126)
   *   Special (exp = 255):    infinity (frac=0) or NaN (frac!=0)
   *
   * Dividing by 2 = multiplying by 0.5 = subtracting 1 from the exponent
   * (since the exponent is a power of 2).
   *
   * EXTRACTING THE FIELDS with bit manipulation:
   *   sign = uf & 0x80000000   -> keeps only bit 31
   *   exp  = (uf >> 23) & 0xFF -> shifts bits 30-23 down, masks to 8 bits
   *   frac = uf & 0x7FFFFF     -> keeps only bits 22-0 (23 bits)
   *
   * CASE 1: exp == 0xFF (infinity or NaN)
   *   Return unchanged. You can't halve infinity, and NaN stays NaN.
   *
   * CASE 2: exp > 1 (normal, stays normal after halving)
   *   Just subtract 1 from exponent. Reassemble: sign | ((exp-1) << 23) | frac
   *   The << 23 puts the exponent back into bits 30-23.
   *   The | combines sign + exponent + fraction back into one 32-bit value.
   *
   * CASE 3: exp == 1 (normal -> becomes denormalized)
   *   Exp goes from 1 to 0, which changes the meaning of the fraction.
   *   Normalized has an implicit leading 1: value uses 1.fraction
   *   Denormalized has no implicit 1: value uses 0.fraction
   *   So we must put that implicit 1 back into the fraction before shifting:
   *     frac = frac | 0x800000 (set bit 23, the implicit leading 1)
   *   Now frac is 24 bits. We shift right by 1 (below) to divide by 2.
   *
   * CASE 4: exp == 0 (already denormalized)
   *   Can't decrement exponent (already 0). Instead, shift fraction right by 1.
   *   This divides the value by 2 but may lose the lowest bit (precision loss).
   *
   * ROUNDING (cases 3 & 4):
   *   When we shift frac right by 1, we lose the lowest bit.
   *   IEEE 754 uses "round to even": if the lost bit is 1 AND the new lowest
   *   bit is also 1 (i.e., the bottom 2 bits before shifting are "11"),
   *   we round up by adding 1 after the shift.
   *     (frac & 3) == 3 checks if bottom 2 bits are both 1.
   */
  unsigned sign = uf & 0x80000000;
  unsigned exp  = (uf >> 23) & 0xFF;
  unsigned frac = uf & 0x7FFFFF;

  if (exp == 0xFF)
    return uf;

  if (exp > 1)
    return sign | ((exp - 1) << 23) | frac;

  if (exp == 1)
    frac = frac | 0x800000;

  unsigned round = (frac & 3) == 3;
  frac = (frac >> 1) + round;

  return sign | frac;
}
