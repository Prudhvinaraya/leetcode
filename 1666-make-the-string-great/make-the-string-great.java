class Solution {
    public String makeGood(String s) {
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (sb.length() > 0 && Math.abs(sb.charAt(sb.length() - 1) - c) == 32) {
                sb.deleteCharAt(sb.length() - 1); // Remove the last character from the StringBuilder
            } else {
                sb.append(c); // Append the current character to the StringBuilder
            }
        }
        
        return sb.toString();
    }
}