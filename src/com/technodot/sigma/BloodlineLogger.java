package com.technodot.sigma;

import java.util.logging.Level;

import org.bukkit.Bukkit;

public class BloodlineLogger {
	
	public static final String namespace = "Cyberverse";
	
	private static String format(String message) {
		return "[" + namespace + "] " + message;
	}
	
	public static void info(String message) {
		Bukkit.getServer().getLogger().log(Level.INFO, format(message));
	}
	
	public static void warn(String message) {
		Bukkit.getServer().getLogger().log(Level.WARNING, format(message));
	}
	
	public static void error(String message) {
		Bukkit.getServer().getLogger().log(Level.SEVERE, format(message));
	}
	
	public static void chat(String message) {
		Bukkit.broadcastMessage(message);
	}
	
	public static void shout(String message) {
		chat(message);
		info(message);
	}
	
}