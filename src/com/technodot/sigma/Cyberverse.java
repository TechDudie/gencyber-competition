package com.technodot.sigma;

import org.bukkit.plugin.java.JavaPlugin;

public class Cyberverse extends JavaPlugin {
	
	@Override
	public void onEnable() {
		// Register commands
		
		getCommand("ledon").setExecutor(new CyberverseCommand());
		getCommand("ledoff").setExecutor(new CyberverseCommand());
		getCommand("camera").setExecutor(new CyberverseCommand());
		getCommand("check_door").setExecutor(new CyberverseCommand());
		getCommand("antivirus").setExecutor(new CyberverseCommand());
		getCommand("shutdown").setExecutor(new CyberverseCommand());
		
		BloodlineLogger.info("Cyberverse");
		BloodlineLogger.info("");
		BloodlineLogger.info("================================================================================");
		BloodlineLogger.info("");
		BloodlineLogger.info("Copyright TechnoDot 2023. All rights reserved.");
		BloodlineLogger.info("For help, contact \"technodot\" on Discord, or @TechDudie on GitHub.");
		BloodlineLogger.info("Cyberverse v1.0 loaded!");
	}
	
	@Override
	public void onDisable() {
		BloodlineLogger.info("Cyberverse v1.0 unloaded!");
	}
}