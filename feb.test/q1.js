/*Promise is an object that is used to handle asyncronous code. 
Promise returns the result in the future.
Insted of writing multiple nasted arrow function which can create callback hell to avoid this we use promise.
It helps to make the program more easier to read  and understand. 
Async and Await is also use to handle asynchronous code.
In Order to convert syncronous code we can use Async and Await.
ADVANTAGES :- 
1) It is used in asynchronous non blocking code.
2) It helps to make the code easier to read and understand.
*/
function payment(status){
    return new Promise(function(resolve,reject){
        setTimeout(()=>{
            if(status){
                resolve("Success...")
            }
            else{
                reject("Failed..")
            }
        },1000)
    })
}
payment(true)
.then(res => console.log(res))
.catch(err => console.log(err))
/*
This is an Example of Promise.
*/