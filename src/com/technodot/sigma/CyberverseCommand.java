package com.technodot.sigma;

import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Creeper;
import org.bukkit.entity.Damageable;
import org.bukkit.entity.Entity;
import org.bukkit.entity.Skeleton;
import org.bukkit.entity.Zombie;

public class CyberverseCommand implements CommandExecutor {
	@Override
	public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
		
		if (command.getName().equals("ledon")) {
			CyberAPI.get("led_on");
			return true;
		} else if (command.getName().equals("ledoff")) {
			CyberAPI.get("led_off");
			return true;
		} else if (command.getName().equals("camera")) {
			CyberAPI.get("camera");
			return true;
		} else if (command.getName().equals("check_door")) {
			int resp = CyberAPI.get("check_door");
			World world = Bukkit.getWorlds().get(0);
			Location loc1 = new Location(world, 8.0, 64.0, -16.0);
			Location loc2 = new Location(world, 7.0, 64.0, -16.0);
			
			if (resp == 200) {
				loc1.getBlock().setType(Material.REDSTONE_BLOCK);
				loc2.getBlock().setType(Material.REDSTONE_BLOCK);
			} else if (resp == 500) {
				loc1.getBlock().setType(Material.GRASS_BLOCK);
				loc2.getBlock().setType(Material.GRASS_BLOCK);
			}
			return true;
		} else if (command.getName().equals("antivirus")) {
			World world = Bukkit.getWorlds().get(0);
			for (Entity entity : world.getEntities()) {
				if ((entity instanceof Creeper) || (entity instanceof Skeleton) || (entity instanceof Zombie)) {
					Location loc = entity.getLocation();
					if (loc.getX() > 4.0 && loc.getZ() < 11.0 && loc.getZ() > -17.0 && loc.getZ() < -4.0) {
						world.strikeLightningEffect(loc);
						((Damageable) entity).damage(69420.0);
						CyberAPI.get("siren");
					}
				}
			}
		} else if (command.getName().equals("shutdown")) {
			CyberAPI.get("shutdown");
			return true;
		}
		
		return true;
	}
}