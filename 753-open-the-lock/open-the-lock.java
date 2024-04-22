import java.util.*;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");
        visited.add("0000");
        int level = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String current = queue.poll();
                if (deadSet.contains(current)) continue;
                if (current.equals(target)) return level;
                
                for (int j = 0; j < 4; j++) {
                    for (int k = -1; k <= 1; k += 2) {
                        char[] chars = current.toCharArray();
                        chars[j] = (char)(((chars[j] - '0' + k + 10) % 10) + '0');
                        String next = new String(chars);
                        if (!visited.contains(next)) {
                            queue.offer(next);
                            visited.add(next);
                        }
                    }
                }
            }
            level++;
        }
        
        return -1; // If target cannot be reached
    }
}
