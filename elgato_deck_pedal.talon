os: windows
-
# toggle talon wake and sleep
deck(pedal_left): 
    speech.toggle()

# Switch to webex and tackle mute
deck(pedal_middle): 
#	tracking.control_toggle()
    user.switcher_focus("Webex")
	 key(ctrl-shift-m)

# Switch to teams and toggle mute
deck(pedal_right): 
  user.switcher_focus("teams")
    key(ctrl-shift-m)


