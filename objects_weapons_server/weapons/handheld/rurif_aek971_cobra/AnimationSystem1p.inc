animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 2/3/0.8
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/50

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_changefirerate.baf
animationManager.looping 0
animationManager.length 0.7

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_deploy.baf
animationManager.looping 0
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_fire.baf
animationManager.looping 0
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_fire1.baf
animationManager.looping 0
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_fire2.baf
animationManager.looping 0
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_reload.baf
animationManager.looping 0
animationManager.length 3.7

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_run.baf
animationManager.length 1.4

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_sprint.baf
animationManager.length 0.7

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_stand.baf
animationManager.length 2.2

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_tozoom.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_changefirerate.baf
animationManager.looping 0
animationManager.length 0.5

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire1.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire2.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire3.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_sprint_toprone.baf
animationManager.length 1.7

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_toprone.baf
animationManager.length 0.7

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_toprone_rev.baf
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_toprone.baf
animationManager.length 1.1

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_toprone_rev.baf
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_forward.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_backward.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_right.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_left.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_forward.baf
animationManager.length 3

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_backward.baf
animationManager.length 3

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_left.baf
animationManager.length 3

animationSystem.createAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_right.baf
animationManager.length 3

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_changefirerate.baf


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.9
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_fire.baf

beginrem

animationSystem.createBundle fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_fire1.baf


animationSystem.createBundle fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_fire2.baf
endrem


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_reload.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.4
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.8
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.4
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_stand.baf

beginrem

animationSystem.createBundle zoom_changefirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.15
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_changefirerate.baf
endrem


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire.baf


animationSystem.createBundle zoom_fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire1.baf


animationSystem.createBundle zoom_fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire2.baf


animationSystem.createBundle zoom_fire3
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_fire3.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_stand.baf


animationSystem.createBundle zoom_toprone
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_toprone.baf


animationSystem.createBundle zoom_toprone_rev
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_toprone_rev.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_tozoom.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 1
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_left.baf
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_right.baf
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_backward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_zoom_run_forward.baf


animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_toprone.baf
animationBundle.addEvent effect:8
animationBundle.setEventStartTime effect:8 0


animationSystem.createBundle sprinttoprone
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_sprint_toprone.baf


animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_toprone_rev.baf
animationBundle.addEvent effect:9
animationBundle.setEventStartTime effect:9 0


animationSystem.createBundle prone_move
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_left.baf
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_right.baf
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_backward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/rurif_aek971_cobra/Animations/1p/1p_aek971_prone_forward.baf
animationBundle.addEvent effect:1

rem *** Triggers ***
animationSystem.createTrigger MessageTrigger zoom_changeFirerate
animationTrigger.addBundle zoom_changefirerate
animationTrigger.message 8

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

animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addChild rnd_zoom_fire
animationTrigger.message 1

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

beginrem

animationSystem.createTrigger MovementTrigger move_prone_t
animationTrigger.addBundle prone_move
animationTrigger.valueHolder 1p_move

endrem

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

beginrem

animationSystem.createTrigger Trigger fromProne_zoom
animationTrigger.addBundle zoom_toprone_rev

animationSystem.createTrigger Trigger fromProne_normal
animationTrigger.addBundle toProneReverse

animationSystem.createTrigger SwitchMessageTrigger fromProne
animationTrigger.addChild fromProne_zoom
animationTrigger.addChild fromProne_normal
animationTrigger.message 4

animationSystem.createTrigger Trigger stillToProne_zoom
animationTrigger.addBundle zoom_toprone

animationSystem.createTrigger Trigger stillToProne_normal
animationTrigger.addBundle toProne

animationSystem.createTrigger SwitchMessageTrigger stillToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4

animationSystem.createTrigger Trigger sprintToProne
animationTrigger.addBundle sprinttoprone

animationSystem.createTrigger SwitchMessageTrigger forwardToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild sprinttoprone
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger backwardToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild sprinttoprone
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger leftToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild sprinttoprone
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger rightToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild sprinttoprone
animationTrigger.message 4

animationSystem.createTrigger Trigger specialMoves
animationTrigger.addChild fromProne
animationTrigger.addChild stillToProne
animationTrigger.addChild forwardToProne
animationTrigger.addChild backwardToProne
animationTrigger.addChild leftToProne
animationTrigger.addChild rightToProne

endrem

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup
animationTrigger.addChild specialMoves

