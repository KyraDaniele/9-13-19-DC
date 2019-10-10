# Big O Time Complexity Quiz 2


# Determine the time complexity for the following function 
1. function logUpTo(n) {
2.     for (var i = 1; i <= n; i++) {
3.         console.log(i);
4.     }
5. }

# Determine the time complexity for the following function 
1. function logAtMost10(n) {
2.     for (var i = 1; i <= Math.min(n, 10); i++) {
3.         console.log(i);
4.     }
5. }

# Determine the time complexity for the following function
1. function logAtLeast10(n) {
2.     for (var i = 1; i <= Math.max(n, 10); i++) {
3.         console.log(i);
4.     }
5. }

# Determine the time complexity for the following function
1. function onlyElementsAtEvenIndex(array) {
2.     var newArray = Array(Math.ceil(array.length / 2));
3.     for (var i = 0; i < array.length; i++) {
4.         if (i % 2 === 0) {
5.             newArray[i / 2] = array[i];
6.         }
7.     }
8.     return newArray;
9. }

# Determine the time complexity for the following function
1. function subtotals(array) {
2.     var subtotalArray = Array(array.length);
3.     for (var i = 0; i < array.length; i++) {
4.         var subtotal = 0;
5.         for (var j = 0; j <= i; j++) {
6.             subtotal += array[j];
7.         }
8.         subtotalArray[i] = subtotal;
9.     }
10.     return subtotalArray;
11. }
