class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> leftParentheses = new Stack<>();
        Stack<Integer> stars = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                leftParentheses.push(i);
            } else if (ch == '*') {
                stars.push(i);
            } else if (ch == ')') {
                if (!leftParentheses.isEmpty()) {
                    leftParentheses.pop();
                } else if (!stars.isEmpty()) {
                    stars.pop();
                } else {
                    return false;
                }
            }
        }

        while (!leftParentheses.isEmpty()) {
            if (stars.isEmpty() || leftParentheses.peek() > stars.peek()) {
                return false;
            }
            leftParentheses.pop();
            stars.pop();
        }

        return true;
    }
}