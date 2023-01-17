package bj_10816;

public class StringBuilder_ex {
    
    public static void main(String[] args) {
        
        // String 객체끼리 더하는 방법은
        // 메모리 할당/해제를 발생시켜 성능적으로 좋지 않다.
        // https://onlyfor-me-blog.tistory.com/317
        String str1 = "자바";
        String str2 = " 프로그래밍";
        String str3 = " - 안드로이드 "; 
        String result = str1 + str2;
        System.out.println(result);
        result += str3;
        System.out.println(result);

        // 자바에서 String 객체는 변경 불가능하다.
        // 새 문자열이 생성되면 이전 문자열은 가비지 컬렉터로 들어간다.

        StringBuilder sb = new StringBuilder();
        sb.append("샐러드 ").append(" 주스");

        String str = sb.toString();
        System.out.println(sb);
        System.out.println(str);
    }
}
