import java.util.Random;

public class ByteHelpers {
    public static void reverseBytes(byte[] bytes) {
        String bitString = "";
        for (byte b: bytes){
            bitString += String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
        }
        System.out.println("Original Bits: " + bitString);
        String reversed = "";
        for (int i=bitString.length()-1; i>=0; i--){
            reversed += bitString.toCharArray()[i];
        }
        System.out.println("Reversed Bits: " + reversed);
    }
    /**
     * Compile: javac ByteHelpers.java
     * Usage: java ByteHelpers [number of random bytes]
     * @param args First element should be an integer>0
     */
    public static void main (String[] args){
        byte[] b = new byte[Integer.parseInt(args[0])];
        new Random().nextBytes(b);
        reverseBytes(b);
    }
}
 