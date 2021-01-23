#include<iostream>
#include <bits/stdc++.h>
using namespace std;
int setBits(unsigned long long int n )
{
    int count=0;
    while(n){
        n&=(n-1);
        count++;
    }
    return count;
 } 
int main(){
    int t;
    cin>>t;
    while(t--){
        unsigned long long int n ;
        cin>>n;
        if (setBits(n-1) & 1) 
        cout<<("Louise\n") ;
        else 
        cout<<("Richard\n") ;
    }
    return 0;
    
}
