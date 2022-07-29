animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 2/3/4
animationSystem.cameraSpring.stiffness 60/60/60
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/50
rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_forward.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_backward.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_left.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_right.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_changefirerate.baf
animationManager.looping 0
animationManager.length 0.3

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_deploy.baf
animationManager.looping 0
animationManager.length 0.85

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire1.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire2.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire3.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire4.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_reload.baf
animationManager.looping 0
animationManager.length 3.7

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_run.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_tozoom.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire1.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire2.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire3.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire4.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/USRIF_G36C/Animations/1p/1p_g36c_idle1.baf
animationManager.looping 0
animationManager.length 2.08333

animationSystem.createAnimation Objects/Weapons/Handheld/USRIF_G36C/Animations/1p/1p_g36c_idle2.baf
animationManager.looping 0
animationManager.length 2.08333

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_run_prone.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_toprone_rev.baf
animationManager.length 1.2
rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_changefirerate.baf

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_deploy.baf

animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire.baf

animationSystem.createBundle fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire1.baf

animationSystem.createBundle fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire2.baf

animationSystem.createBundle fire3
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire3.baf

animationSystem.createBundle fire4
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_fire4.baf

animationSystem.createBundle idle1
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/USRIF_G36C/Animations/1p/1p_g36c_idle1.baf

animationSystem.createBundle idle2
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/USRIF_G36C/Animations/1p/1p_g36c_idle2.baf

animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_reload.baf

animationSystem.createBundle run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_run.baf

animationSystem.createBundle sprint
animationBundle.fadeInTime 0.32
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_sprint.baf

animationSystem.createBundle still
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_stand.baf

animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire.baf

animationSystem.createBundle zoom_fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire1.baf

animationSystem.createBundle zoom_fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire2.baf

animationSystem.createBundle zoom_fire3
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire3.baf

animationSystem.createBundle zoom_fire4
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.08
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_fire4.baf

animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.35
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_left.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_right.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_backward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_run_forward.baf

animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_zoom_stand.baf

animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_tozoom.baf

animationSystem.createBundle run_prone
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_run_prone.baf

animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_toprone.baf
animationBundle.addEvent effect:8
animationBundle.setEventStartTime effect:8 0

animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_aek971/Animations/1p/1p_aek971_toprone_rev.baf
animationBundle.addEvent effect:9
animationBundle.setEventStartTime effect:9 0
rem *** Triggers ***
animationSystem.createTrigger Trigger zoom_still
animationTrigger.addBundle zoom_still
animationSystem.createTrigger MovementTrigger zoom_move
animationTrigger.addBundle zoom_run
animationTrigger.valueHolder 1p_zoom_move
animationSystem.createTrigger RandomTrigger rnd_zoom_fire
animationTrigger.addBundle zoom_fire
animationTrigger.addBundle zoom_fire1
animationTrigger.addBundle zoom_fire2
animationTrigger.addBundle zoom_fire3
animationTrigger.addBundle zoom_fire4
animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addChild rnd_zoom_fire
animationTrigger.message 1
animationSystem.createTrigger MessageTrigger zoom_changeFirerate
animationTrigger.addBundle zoom_changeFirerate
animationTrigger.message 8
animationSystem.createTrigger Trigger zoom
animationTrigger.addChild zoom_still
animationTrigger.addChild zoom_move
animationTrigger.addChild zoom_fire
animationTrigger.addChild zoom_changeFirerate
animationSystem.createTrigger Trigger still
animationTrigger.addBundle still
animationSystem.createTrigger MovementTrigger move_stand_t
animationTrigger.addBundle run
animationTrigger.valueHolder 1p_move
animationSystem.createTrigger MovementTrigger move_crouch_t
animationTrigger.addBundle run
animationTrigger.valueHolder 1p_move
animationSystem.createTrigger MovementTrigger move_prone_t
animationTrigger.addBundle run_prone
animationTrigger.valueHolder 1p_move
animationSystem.createTrigger PoseTrigger move
animationTrigger.addChild move_stand_t
animationTrigger.addChild move_crouch_t
animationTrigger.addChild move_prone_t
animationTrigger.addChild move_prone_t
animationSystem.createTrigger MovementTrigger sprint
animationTrigger.addBundle sprint
animationTrigger.valueHolder 1p_sprint
animationSystem.createTrigger RandomTrigger rnd_fire
animationTrigger.addBundle fire
animationTrigger.addBundle fire1
animationTrigger.addBundle fire2
animationTrigger.addBundle fire3
animationTrigger.addBundle fire4
animationSystem.createTrigger MessageTrigger fire
animationTrigger.addChild rnd_fire
animationTrigger.message 1
animationSystem.createTrigger MessageTrigger changeFirerate
animationTrigger.addBundle changeFirerate
animationTrigger.message 8
animationSystem.createTrigger MessageTrigger reload
animationTrigger.addBundle reload
animationTrigger.message 2
animationSystem.createTrigger Trigger normal
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire
animationTrigger.addChild changeFirerate
animationTrigger.addChild reload
animationSystem.createTrigger SwitchMessageTrigger root
animationTrigger.addChild zoom
animationTrigger.addChild normal
animationTrigger.addBundle zoomTransition
animationTrigger.message 4
animationSystem.createTrigger Trigger fromProne_zoom
animationTrigger.addBundle zoom_still
animationSystem.createTrigger Trigger fromProne_normal
animationTrigger.addBundle toProneReverse
animationSystem.createTrigger SwitchMessageTrigger fromProne
animationTrigger.addChild fromProne_zoom
animationTrigger.addChild fromProne_normal
animationTrigger.message 4
animationSystem.createTrigger Trigger stillToProne_zoom
animationTrigger.addBundle zoom_still
animationSystem.createTrigger Trigger stillToProne_normal
animationTrigger.addBundle toProne
animationSystem.createTrigger SwitchMessageTrigger stillToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4
animationSystem.createTrigger SwitchMessageTrigger forwardToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4
animationSystem.createTrigger SwitchMessageTrigger backwardToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4
animationSystem.createTrigger SwitchMessageTrigger leftToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4
animationSystem.createTrigger SwitchMessageTrigger rightToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4
animationSystem.createTrigger Trigger specialMoves
animationTrigger.addChild fromProne
animationTrigger.addChild stillToProne
animationTrigger.addChild forwardToProne
animationTrigger.addChild backwardToProne
animationTrigger.addChild leftToProne
animationTrigger.addChild rightToProne
animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy
animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup
animationTrigger.addChild specialMoves
