// Define variables
cafe_width = 6; // meters
cafe_length = 10; // meters
cafe_height = 3; // meters
door_width = 1.2; // meters
window_width = 1; // meters
window_height = 1.2; // meters

// Create the cafe building
translate([0,0,cafe_height/2]) cube([cafe_length,cafe_width,cafe_height]);

// Create the door
translate([cafe_length/2-door_width/2,-(cafe_width/2),0]) cube([door_width,0.1,cafe_height]);

// Create the windows
translate([-(cafe_length/2)+window_width/2,0,cafe_height/2]) cube([0.1,cafe_width-window_width,window_height]);
translate([0,(cafe_width/2)-window_width/2,cafe_height/2]) cube([cafe_length-window_width,0.1,window_height]);
