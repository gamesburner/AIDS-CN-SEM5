import java.io.*;
import java.net.*;
public class TCPClient
{
  public static void main(String[]args)throws Exception
{
  Socket s =new Socket("127.0.0.1",8080);
  System.out.println("Coonected to TCP Server");
  BufferedReader in=new BufferedReader(new InputStreamReader(s.getInputStream()));
  PrintWriter out=new PrintWriter(s.getOutputStream(),true);
  out.println("Hello from TCP Client");
  String reply=in.readLine();
  System.out.println("Server:" +reply);
  s.close();
}
}