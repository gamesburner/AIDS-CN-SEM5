import java.net.*;

public class UDPServer 
{
    public static void main(String[] args) throws Exception 
{
        DatagramSocket ds = new DatagramSocket(8080);
        System.out.println("UDP Server started. Waiting for client...");

        byte[] buf = new byte[1024];
        DatagramPacket dp = new DatagramPacket(buf, buf.length);
        ds.receive(dp); 

        String msg = new String(dp.getData(), 0, dp.getLength());
        System.out.println("Client: " + msg);

        String reply = "Hello from UDP Server";
        DatagramPacket dpSend = new DatagramPacket(reply.getBytes(), reply.length(), dp.getAddress(), dp.getPort());
        ds.send(dpSend);

        ds.close();
    }
}