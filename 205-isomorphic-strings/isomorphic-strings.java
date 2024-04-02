class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Character> charMap = new HashMap<>();
        HashMap<Character, Boolean> mappedChars = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char charS = s.charAt(i);
            char charT = t.charAt(i);

            if (!charMap.containsKey(charS)) {
                if (mappedChars.containsKey(charT) && mappedChars.get(charT)) {
                    return false;
                }
                charMap.put(charS, charT);
                mappedChars.put(charT, true);
            } else {
                if (charMap.get(charS) != charT) {
                    return false;
                }
            }
        }

        return true;
    }
}
