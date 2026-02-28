/* Internal Working of JavaScript Engine (2 Marks)

Explain briefly:

/*
1)Call Stack
The Call Stack is a data structure that keeps track of function calls in a program. You can think of it like a stack of plates — you add and remove from the top only. This follows the Last-In, First-Out (LIFO) rule.
When a function is called, it gets placed on top of the stack. JavaScript then runs the function that is currently on top. When the function finishes (either returns a value or reaches the end), it is removed from the stack. Control then goes back to the function below it.
JavaScript has only one call stack, which means it can do only one thing at a time. If a function takes a long time to run, it blocks the stack and the application can become slow or unresponsive.

2)Event Loop
The Event Loop is the system that helps JavaScript handle asynchronous tasks without blocking the main thread.
When JavaScript encounters an asynchronous operation like setTimeout, fetch, or a user event, it does not put it directly on the Call Stack. Instead, it sends it to the browser or Node.js to handle in the background.
Once that task is finished, its callback function is placed into a queue.

There are two main types of queues:
a)Microtask Queue 
b)Task Queue 


The Event Loop constantly checks if the Call Stack is empty. If it is, it first runs all tasks in the Microtask Queue. After that, it runs tasks from the Task Queue.
*/