### Asynchronous Python Comprehensions

This repository contains Python code implementing asynchronous generators and comprehensions as part of the ALX Back-end Python curriculum. These exercises are designed to familiarize learners with asynchronous programming concepts in Python.
Project Structure

The project is organized into the following files:

    0-async_generator.py: Defines a coroutine async_generator that yields random numbers asynchronously after waiting for 1 second in each iteration.

    1-async_comprehension.py: Implements a coroutine async_comprehension that collects 10 random numbers using an async comprehension over async_generator.

    2-measure_runtime.py: Contains a coroutine measure_runtime which executes async_comprehension four times in parallel using asyncio.gather and measures the total runtime.

Learning Objectives

By completing these exercises, learners are expected to:

    Understand how to write asynchronous generators and comprehensions in Python.
    Learn to use asyncio for parallel execution of asynchronous tasks.
    Gain familiarity with type annotations for asynchronous functions and generators.
