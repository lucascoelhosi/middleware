package com.mid;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;


/**
 *
 * @author LaecioRodrigues
 */
public class EnviarResposta {
    public void enviar(String res){
        String resp = res;
        try{
            Socket s = new Socket("10.180.53.49",7412);
            PrintWriter pw = new PrintWriter(s.getOutputStream());
            pw.write(resp);
            pw.flush();
            pw.close();
            s.close();    
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
