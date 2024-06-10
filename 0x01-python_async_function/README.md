# Python Async Function Project

## Project Overview

This project delves into asynchronous programming in Python, focusing primarily on utilizing asyncio for handling asynchronous I/O operations. It covers essential concepts such as async and await syntax, executing async programs with asyncio, running concurrent coroutines, creating asyncio tasks, and leveraging the random module for asynchronous tasks.

## Learning Objectives

Upon completion of this project, participants will gain a deep understanding of the following topics, enabling them to explain them to others without relying on external resources:

- async and await syntax in Python.
- Execution of async programs using asyncio.
- Running concurrent coroutines for improved efficiency.
- Creation and management of asyncio tasks.
- Utilization of the random module within asynchronous programming contexts.

## Requirements

- Code must follow the PEP8 coding style and include type annotations.
- Each module and function should be documented thoroughly.

## Tasks

### Task 0: The Basics of Async

Implement an asynchronous coroutine named `wait_random` that introduces a random delay between 0 and a specified maximum delay time, returning the result.

### Task 1: Executing Multiple Coroutines Concurrently

Create an async routine, `wait_n`, that spawns multiple instances of `wait_random` concurrently, returning a list of delay times in ascending order.

### Task 2: Measuring Runtime

Develop a function, `measure_time`, to measure the total execution time of `wait_n` for a given number of iterations and maximum delay, returning the average time per iteration.

### Task 3: Tasks

Write a regular function, `task_wait_random`, that takes an integer `max_delay` and returns an asyncio.Task for asynchronous execution.

### Task 4: Tasks

Transform the code from `wait_n` into a new function, `task_wait_n`, which calls `task_wait_random` to achieve similar functionality.
