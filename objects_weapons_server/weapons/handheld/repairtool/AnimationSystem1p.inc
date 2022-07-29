animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.045/0.045/0.045
animationSystem.cameraSpring.zoomDamping 2.5/2.5/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_deploy.baf
animationManager.length 0.85

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_repair.baf
animationManager.length 3.3

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_Idle1.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_left.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_right.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_backward.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_forward.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_sprint.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_stand.baf

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_repair.baf


animationSystem.createBundle idle1
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_Idle1.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.2


animationSystem.createBundle run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_left.baf
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_right.baf
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_backward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_run_forward.baf
animationBundle.addEvent effect:1


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_stand.baf


animationSystem.createBundle zoom_changeFirerate
animationBundle.isLooping 0


animationSystem.createBundle zoom_fire
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_repair.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/REPAIRTOOL/Animations/1p/1p_repairtool_stand.baf


rem *** Triggers ***
animationSystem.createTrigger RandomTrigger rnd_idle
animationTrigger.addBundle idle1
animationTrigger.addBundle Idle2

animationSystem.createTrigger IdleTrigger idle
animationTrigger.addChild rnd_idle
animationTrigger.idleTime 5/15

animationSystem.createTrigger Trigger still
animationTrigger.addChild idle
animationTrigger.addBundle still

animationSystem.createTrigger MovementTrigger move
animationTrigger.addBundle run
animationTrigger.valueHolder 1p_move

animationSystem.createTrigger MovementTrigger sprint
animationTrigger.addBundle sprint
animationTrigger.valueHolder 1p_sprint

animationSystem.createTrigger MessageTrigger fire
animationTrigger.fadeInTime 0.1
animationTrigger.addBundle fire
animationTrigger.message 1

animationSystem.createTrigger PoseTrigger move
animationTrigger.addChild stand_move
animationTrigger.addChild crouch_move
animationTrigger.addChild prone_move

animationSystem.createTrigger SwitchMessageTrigger forwardRun
animationTrigger.addChild st_run
animationTrigger.addChild run
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger backwardRun
animationTrigger.addChild st_run
animationTrigger.addChild run
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger leftRun
animationTrigger.addChild st_run
animationTrigger.addChild run
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger rightRun
animationTrigger.addChild st_run
animationTrigger.addChild run
animationTrigger.message 4

animationSystem.createTrigger Trigger normal
animationTrigger.fadeInTime 0.2
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire

animationSystem.createTrigger Trigger root
animationTrigger.addChild normal

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addBundle zoom_fire
animationTrigger.message 1

animationSystem.createTrigger Trigger zoom_still
animationTrigger.addBundle zoom_still

animationSystem.createTrigger Trigger zoom
animationTrigger.fadeInTime 0.2
animationTrigger.addChild zoom_fire
animationTrigger.addChild zoom_still

animationSystem.createTrigger Trigger specialMoves
animationTrigger.addChild forwardRun
animationTrigger.addChild backwardRun
animationTrigger.addChild leftRun
animationTrigger.addChild rightRun

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild specialMoves