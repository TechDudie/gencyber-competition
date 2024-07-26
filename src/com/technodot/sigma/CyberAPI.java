package com.technodot.sigma;

import java.net.HttpURLConnection;
import java.net.URL;

public class CyberAPI {
	
	public static final String API_URL = "http://raspberrypi.local/";
	
	public static int get(String request) {
        try {
            URL url = new URL(API_URL + request);
            HttpURLConnection con = (HttpURLConnection) url.openConnection();
            con.setRequestMethod("GET");       
            con.setDoOutput(true);
            int resp = con.getResponseCode(); 
            con.disconnect();
            
            return resp;
        }
        catch (java.io.IOException e) {
    		BloodlineLogger.chat("uh oh " + e.getMessage());
        }
		return 200;
    }
}
