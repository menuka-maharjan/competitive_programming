#include<iostream>
#include<vector>
#include <bits/stdc++.h> 
using namespace std;
int main(){
    int l,r,i,j;
    vector <int> a;
    cin>>l;
    cin>>r;
    for (i=l;i<=r;i++){
        for (j=i;j<=r;j++){
            a.push_back(i^j);
        }
    }
    cout << *max_element(a.begin(), a.end()); 
    return 0;
}
