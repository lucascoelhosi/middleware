package com.mid;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;
import org.zeromq.ZMQ;
import org.zeromq.ZMsg;
import org.zeromq.ZContext;

public class hwserver
{
	private static Random rand = new Random(System.nanoTime());
	
    public static void main(String[] args) throws Exception
    {	
    	
    	try (ZContext context = new ZContext()) {
            // Socket to talk to clients
            ZMQ.Socket socket = context.createSocket(ZMQ.DEALER);
            String identity = String.format(
                    "%04X-%04X", rand.nextInt(), rand.nextInt()
                );
                socket.setIdentity(identity.getBytes(ZMQ.CHARSET));
            socket.connect("tcp://localhost:5570");
            

//            while (!Thread.currentThread().isInterrupted()) {
               

            	// Send a response
                String response = "Texto a ser tratado";
                socket.send(response.getBytes(ZMQ.CHARSET), 0);
                
                ZMsg msg = ZMsg.recvMsg(socket);
                
                msg.getLast().print(identity);
                msg.destroy();


                
//            }
        }
    	
        
    }
}