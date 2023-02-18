#include<stdio.h> 
  
//Structure for Item which store weight and corresponding  
//value of Item  
typedef struct Item 
{ 
    int value, weight; 
  
    //constructor for Item 
    Item(int value, int weight) : value(value), weight(weight) 
    {} 
}; 
  
//Comparator function to sort Item according to val/weight ratio 
bool cmp(struct Item a, struct Item b) 
{ 
    double r1 = (double)a.value / a.weight; 
    double r2 = (double)b.value / b.weight; 
    return r1 > r2; 
} 
  
// Main greedy
double fractionalKnapsack(int W, struct Item arr[], int n) 
{ 
    //sorting Item on basis of ratio 
    sort(arr, arr + n, cmp); 
  
    // Initialize result
    int curWeight = 0;  // Current weight in knapsack 
    double finalvalue = 0.0; // Result (value in Knapsack) 
  
    // Looping through all Items 
    for (int i = 0; i < n; i++) 
    { 
        // If adding Item won't overflow, add it completely 
        if (curWeight + arr[i].weight <= W) 
        { 
            curWeight += arr[i].weight; 
            finalvalue += arr[i].value; 
        } 
  
        // If we can't add current Item, add fractional part of it 
        else
        { 
            int remain = W - curWeight; 
            finalvalue += arr[i].value * ((double) remain / arr[i].weight); 
            break; 
        } 
        
         } 
  
    // Returning final value 
    return finalvalue; 
}
 }

// This function is used to increment the value
function incrementValue(val) {
    // Increment the value by 1
    val++;
    
    // Return the incremented value
    return val;
}

        
