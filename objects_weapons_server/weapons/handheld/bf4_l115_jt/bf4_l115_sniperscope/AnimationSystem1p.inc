animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.02/0.02/0.02
animationSystem.cameraSpring.zoomDamping 10/10/1
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 0/0/0.0001
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/20

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_deploy.baf
animationManager.looping 0
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_reload.baf
animationManager.length 4.45

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_run.baf
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_shift.baf
animationManager.looping 0
animationManager.length 1.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_sprint.baf
animationManager.length 0.7

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_stand.baf
animationManager.length 2.2

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_idle.baf
animationManager.length 2.2

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_tozoom.baf
animationManager.looping 0
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_fire.baf
animationManager.length 0.2
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_shift.baf
animationManager.looping 0
animationManager.length 1.35

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_run.baf
animationManager.length 1.7

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_toprone.baf
animationManager.length 1.1

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_toprone_rev.baf
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_sprint_toprone.baf
animationManager.length 1.7

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_toprone.baf
animationManager.length 1.1

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_toprone_rev.baf
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_forward.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_backward.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_right.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_left.baf
animationManager.length 0.6

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.08
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_fire.baf


animationSystem.createBundle idle1
animationBundle.isLooping 1
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_idle.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.37


animationSystem.createBundle run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_run.baf


animationSystem.createBundle shift
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_shift.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.48


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.1
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.01
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_fire.baf


animationSystem.createBundle zoom_shift
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.1
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_shift.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_stand.baf


animationSystem.createBundle zoom_toprone
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_toprone.baf


animationSystem.createBundle zoom_toprone_rev
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_zoom_toprone_rev.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_tozoom.baf


animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_toprone.baf
animationBundle.addEvent effect:8
animationBundle.setEventStartTime effect:8 0


animationSystem.createBundle sprinttoprone
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_sprint_toprone.baf


animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_toprone_rev.baf
animationBundle.addEvent effect:9
animationBundle.setEventStartTime effect:9 0


animationSystem.createBundle prone_move
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_left.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_right.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_backward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_l115_jt/bf4_l115_sniperscope/animations/1p/1p_l115_prone_forward.baf
animationBundle.addEvent effect:1

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
animationTrigger.addBundle prone_move
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
animationTrigger.addChild sprintToProne
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger backwardToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild sprintToProne
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger leftToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild sprintToProne
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger rightToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild sprintToProne
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

