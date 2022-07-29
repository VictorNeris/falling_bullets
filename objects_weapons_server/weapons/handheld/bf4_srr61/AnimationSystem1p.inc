animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.02/0.02/0.02
animationSystem.cameraSpring.zoomDamping 10/10/1
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 0/0/0.0001
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/20

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_forward.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_backward.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_left.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_right.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_deploy.baf
animationManager.looping 0
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_reload.baf
animationManager.length 4.91667

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_run.baf
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_shift.baf
animationManager.looping 0
animationManager.length 1.667

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_sprint.baf
animationManager.length 0.625

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_tozoom.baf
animationManager.looping 0
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_fire.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_shift.baf
animationManager.looping 0
animationManager.length 1.667

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_run_prone.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_toprone_rev.baf
animationManager.length 1.2

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.7
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 4.05


animationSystem.createBundle run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_run.baf


animationSystem.createBundle shift
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_shift.baf
animationBundle.addEvent effect:1
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.73


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.35
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.05
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_fire.baf


animationSystem.createBundle zoom_shift
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.05
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_shift.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.35
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_left.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_right.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_backward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_run_forward.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_zoom_stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_tozoom.baf



animationSystem.createBundle run_prone
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_run_prone.baf


animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_toprone.baf
animationBundle.addEvent effect:8
animationBundle.setEventStartTime effect:8 0


animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_srr61/animations/1p/1p_srr61_toprone_rev.baf
animationBundle.addEvent effect:9
animationBundle.setEventStartTime effect:9 0

rem *** Triggers ***
animationSystem.createTrigger Trigger zoom_still
animationTrigger.addBundle zoom_still

animationSystem.createTrigger MovementTrigger zoom_move
animationTrigger.addBundle zoom_run
animationTrigger.valueHolder 1p_zoom_move

animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addBundle zoom_fire
animationTrigger.message 1

animationSystem.createTrigger MessageTrigger zoom_shift
animationTrigger.addBundle zoom_shift
animationTrigger.message 32

animationSystem.createTrigger Trigger zoom
animationTrigger.addChild zoom_still
animationTrigger.addChild zoom_move
animationTrigger.addChild zoom_fire
animationTrigger.addChild zoom_shift

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

animationSystem.createTrigger MessageTrigger fire
animationTrigger.addBundle fire
animationTrigger.message 1

animationSystem.createTrigger MessageTrigger reload
animationTrigger.addBundle reload
animationTrigger.message 2

animationSystem.createTrigger MessageTrigger shift
animationTrigger.addBundle shift
animationTrigger.message 32

animationSystem.createTrigger Trigger normal
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire
animationTrigger.addChild reload
animationTrigger.addChild shift

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

