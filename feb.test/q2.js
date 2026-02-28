/*a) Closure occured when we want to access the variable from the outer function variable
 in the inner function. this process is called Closure.
 It is used  in nasted Function.
 Advantages:-
 a)It helps to access the variable from the outer function.
 b) The lower most function can access  all the variable that is declared in the outer function. 
 
example :

*/
function first(){
    let a = 5;
    function secound(){
        console.log(a)
        b = 7
        function third(){
            console.log(a+b)
        }
        third()
    }
    secound()
}
first()

/* Here i have made a function first in that i have decleared 
a variable a = 5, and in the same function i have made another
 function secound and i am calling the variable that is in the first 
function like that i am addin both the variable in the third function 
and i get the out which is 12. this process is called Closure. */

// b)
// The output of the given program will be 10. 
// Because it return the value that is declared in the outer function.