import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class EntradaDeDados {
    
    // 1
    public static String processFile(String filePath) throws IOException {
        StringBuilder result = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String previousLineLastWord = "";
            String line;
            while ((line = br.readLine()) != null) {
                if (line.startsWith(".......")) {
                    break;
                }

                if (!previousLineLastWord.isEmpty()) {
                    result.append(" ");
                }
                result.append(previousLineLastWord);

                int lastSpaceIndex = line.lastIndexOf(' ');
                if (lastSpaceIndex != -1) {
                    previousLineLastWord = line.substring(lastSpaceIndex + 1);
                    result.append(line, 0, lastSpaceIndex);
                } else {
                    previousLineLastWord = line;
                }
            }

            if (!previousLineLastWord.isEmpty()) {
                result.append(" ").append(previousLineLastWord);
            }
        }
        return result.toString().trim();
    }

    // 2
    public static List<Integer> findAllOccurrences(String TTT, String PPP) {
        List<Integer> occurrences = new ArrayList<>();
        int index = TTT.indexOf(PPP);

        while (index != -1) {
            occurrences.add(index);
            index = TTT.indexOf(PPP, index + 1);
        }

        if (occurrences.isEmpty()) {
            occurrences.add(-1);
        }

        return occurrences;
    }

    // 3
    public static int[] analyzeCharacters(String TTT) {
        int digitCount = 0;
        int vowelCount = 0;
        int consonantCount = 0;

        for (char c : TTT.toCharArray()) {
            if (Character.isDigit(c)) {
                digitCount++;
            } else if ("aeiou".indexOf(c) != -1) {
                vowelCount++;
            } else if (Character.isLetter(c)) {
                consonantCount++;
            }
        }

        return new int[]{digitCount, vowelCount, consonantCount};
    }

        // 4
        public static String findSmallestLexicographicalToken(String TTT) {
            List<String> tokensList = new ArrayList<>();
            String[] tokens = TTT.toLowerCase().split("[ .]+"); 
            for (String token : tokens) {
                tokensList.add(token);
            }
    
            tokensList.sort(String::compareTo);
    
            if (!tokensList.isEmpty()) {
                return tokensList.get(0);
            } else {
                return "";
            }
        }
    
        public static String[] tokenizeString(String TTT) {
            List<String> tokensList = new ArrayList<>();
            String[] tokens = TTT.toLowerCase().split("[ .]+");
            for (String token : tokens) {
                tokensList.add(token);
            }
    
            return tokensList.toArray(new String[0]);
        }

    // 5
    public static String findMostFrequentWord(String TTT) {
        String[] tokens = TTT.toLowerCase().split("[ .]+");

        Map<String, Integer> wordFrequencies = new HashMap<>();
        for (String token : tokens) {
            wordFrequencies.put(token, wordFrequencies.getOrDefault(token, 0) + 1);
        }

        String mostFrequentWord = "";
        int maxFrequency = 0;
        for (Map.Entry<String, Integer> entry : wordFrequencies.entrySet()) {
            if (entry.getValue() > maxFrequency) {
                mostFrequentWord = entry.getKey();
                maxFrequency = entry.getValue();
            }
        }

        return mostFrequentWord;
    }

    // 6
    public static int countLastLineCharacters(String filePath) throws IOException {
        int charCount = 0;
        String lastLine = "";

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.startsWith(".......")) {
                    break; 
                }
                lastLine = line; 
            }

            while ((line = br.readLine()) != null) {
                lastLine = line; 
            }

            charCount = lastLine.length(); 
        }
        return charCount;
    }
}