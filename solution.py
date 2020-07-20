# Problem Statement
# Write a function solution that :
# Given a string S of length N, returns the length of the shortest unique
# substring of S, i.e. the length of the shortest word, which ocuurs in S exactly once. 
# Example:
# 1. Given S = "abaaba" the function should return 2. The shortest unique substring of S is aa.
# 2. Given S="zyzyzyz" the function should return 5. he shortest unique substring of S is "yzyzy"

# Note that there are shortest words, like yzy, occurences of which overlap 
# but they still count as mulitple occurences.

# 3. Given S = "aabbbabaaa" the func should return 3. all substring of size ocuurs in S 
# atleast twice.

# CODE

void t(String s){
    for(int l=0,i=0,t=s.length(),q=0;l++<t&q<1;i=0)
        for(String b;i<=t-l;)
            if(s.indexOf(b=s.substring(i,i++ +l),s.indexOf(b)+1)<0){
                System.out.println(b);
                q++;
            }
}
