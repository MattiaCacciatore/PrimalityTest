# PrimalityTest

A python implementation of the randomized (MonteCarlo version) Miller-Rabin primality test.
Its upper bound error is 1/(4^k) where k is the number of runs:
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test (section Accuracy)

## Usage

<details><summary><b>Show instructions</b></summary>

1. Download and compile:
  ```sh
  $ python MCPrimalityTest.py
  ```
 
</details>

## Motivation

I was studying this algorithm in one of my university courses to understand why it's so
efficient and important for so many applications like security protocols.

## Why

So i (and you) can check if a number is prime or not with a small error rate in
human time.

## Problem solved

Checking big prime numbers with a normal computer.

## Knowledge

Finding an efficient way to check if a positive odd number is prime, in details.
Understading Fermat's Little Theorem, Miller-Rabin test and its effectiveness,
Carmichael numbers and so on.

## Improvable

Yes, some optimization can be done.
