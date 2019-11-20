import java.util.*;
public class Javaq
{
	public static boolean docheck(int n)
	{
        	int prev=-1;
        	while(n>0)
        	{
        		int current=n%10;
        		if(prev!=-1)
        		{
        			if(Math.abs(current-prev)!=1)
        				return false;	
        		}
        		n=n/10;
        		prev=current;
        	}
        	return true;
        }
	
	
	void collectnum(int arr[])
	{
		for(int j=0;j<arr.length;j++)
		{
			if(docheck(arr[j]))
			{
				System.out.println(arr[j]);
			}
		}
	}
    public static void main(String args[])
    {
    	int arr[]={12, 36, 98, 2456, 6512, 1234};
    	Javaq jq = new Javaq();
    	jq.collectnum(arr);
}
}
