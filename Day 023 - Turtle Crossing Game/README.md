A frogger type game created using turtle library

I wanted to clean up "cars" that were off-screen. I originally attempted this by using a deque in the car manager for 
O(1) deletion. You can't delete from a deque while iterating, so for each loop through current cars I tracked indices of 
the off-screen cars in a queue. While I could remove from both of these data structures, there is something about turtle
where the object still remains even after deleting. Probably the screen or something is still referencing the object. I 
have not been able to find a way around this yet, but will keep a lookout for one. 

So, I did not end up implementing the cleanup like I wanted to. Unfortunately th abundance of extra objects that are 
off-screen but still being processed causes a slow-down around level 5 (on my pc).