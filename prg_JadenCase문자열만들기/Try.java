package prg_JadenCase문자열만들기;

class Solution {
    
    static String Jaden(String s){
        
        String [] jadenArray = new String [s.length()];
        jadenArray = s.split(" ");
        
        String jaden = "";
        String first = "";
        
        System.out.println(jadenArray[0].length()-1);
        
            for(int i=0;i<jadenArray.length;i++){
                first = String.valueOf(jadenArray[i].charAt(0));
                jaden = jaden + first.toUpperCase() + jadenArray[i].substring(1,jadenArray[i].length()).toLowerCase();
                if (i!=jadenArray.length-1){
                    jaden += " ";
                }
                
            }
        
        
        return jaden;
    }
    
    public String solution(String s) {
        
        String jaden = Jaden(s);
        
        return jaden;
    }
}