#include<iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int t; cin>>t;
    long a,b;
    while(t--){
        cin>>a>>b;
        long d=b-a;
        long res=0;
        long f=1;
        for(int i=0;i<32;i++){
        
        if(d>(f<<i))
        continue;
        else
        {
            if((a&(f<<i)) && (b&(f<<i)))
            res+=(f<<i);
        }
    }
    cout<<res<<endl;
}
}
