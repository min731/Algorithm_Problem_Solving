package prg_JadenCase문자열만들기;

class Solution {
    
    static String Jaden(String s){
                
        String jaden = "";
        Boolean nextToBlank = true;
        
        for(int i=0;i<s.length();i++){
            
            if(String.valueOf(s.charAt(i)).equals(" ")){
                nextToBlank = true;
                jaden += s.charAt(i);
                continue;
            }
            else if (nextToBlank){
                jaden += String.valueOf(s.charAt(i)).toUpperCase();
            }
            else{
                jaden += String.valueOf(s.charAt(i)).toLowerCase();
            }
            nextToBlank = false;
        }
        
        
        return jaden;
    }
    
    public String solution(String s) {
        
        String answer = Jaden(s);
        
        return answer;
    }
}