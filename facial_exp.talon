#Remove the previous macOS face expression system. If you depend on it, you may want to wait to upgrade until the new system is more polished.
#Fix calling actions from the ready callback, defined in the same module, after Talon was already ready.
#Add cross-platform webcam-based face expression system.
#Match face expressions like this in a .talon file:
#face(smile): ...
#face(smile:start): ...
#face(smile:stop): ...
#face(smile:repeat): ...
#Useful pseudo expressions combining left/right sides:
#blink
#smile
#frown
#squint
#dimple
#These alternate names remain for compatibility with the old macOS face expression system:
#open_mouth
#raise_eyebrows
#eye_blink
#pucker_lips_outwards
#pucker_lips_left
#pucker_lips_right
#All raw expressions: brow_down_left, brow_down_right, brow_inner_up, brow_outer_up_left, brow_outer_up_right, blink_left, blink_right, gaze_down_left, gaze_down_right, gaze_in_left, gaze_in_right, #gaze_out_left, gaze_out_right, gaze_up_left, gaze_up_right, squint_left, squint_right, eye_wide_left, eye_wide_right, jaw_open, jaw_left, jaw_right, mouth_close, dimple_left, dimple_right, frown_left, #frown_right, mouth_funnel, mouth_lower_down_left, mouth_lower_down_right, mouth_press_left, mouth_press_right, mouth_pucker, mouth_right, mouth_left, mouth_roll_lower, mouth_roll_upper, mouth_shrug_lower, #mouth_shrug_upper, smile_left, smile_right, mouth_stretch_left, mouth_stretch_right, mouth_upper_up_left, mouth_upper_up_right

os: windows
-
#face(pucker_lips_left): speech.toggle()
#face(pucker_lips_right): user.switcher_focus("teams")
    key(ctrl-shift-m)
