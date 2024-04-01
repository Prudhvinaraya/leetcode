class Solution {
    public int lengthOfLastWord(String s) {
        //lets convert the given string into array using toArray menthod
        //then traverssing from last until space comes lets find the length of the word
        //int len=s.length();
        String [] arr=s.split(" ");
        int len=arr.length;
        int length=arr[len-1].length();

        return length;
    }
}