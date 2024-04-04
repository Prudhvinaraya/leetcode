class Solution {
    public int maxDepth(String s) {
        char arr[]=s.toCharArray();
        int max=0;
        int max_depth=0;
        //Stack stk=new Stack<>();
        for (int i=0;i<arr.length;i++)
        {
            if(arr[i] =='(')
            {
                max_depth++;
                
            }
            if(arr[i]==')')
            {
                max_depth--;
            }
            if(max_depth>max)
            {
                max=max_depth;
            }
        }
        
        

        //System.out.println(arr);
       return max;
    }
}