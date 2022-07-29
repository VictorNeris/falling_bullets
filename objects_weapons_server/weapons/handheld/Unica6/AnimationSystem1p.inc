animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.035/0.01/0.035
animationSystem.cameraSpring.zoomDamping 2.5/2.5/0
animationSystem.cameraSpring.stiffness 8/8/10
animationSystem.cameraSpring.move 2/1/1
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/10/100

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_deploy.baf
animationManager.looping 0
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_fire.baf
animationManager.looping 0
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_reload.baf
animationManager.length 4.5

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_reload2.baf
animationManager.length 4.5

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_left.baf
animationManager.looping 0
animationManager.length 0.66

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_right.baf
animationManager.looping 0
animationManager.length 0.66

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_backward.baf
animationManager.length 0.66

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_forward.baf
animationManager.looping 0
animationManager.length 0.66

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_sprint.baf
animationManager.length 0.68

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_tozoom.baf
animationManager.looping 0
animationManager.length 0.12

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.5

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_zoom_run.baf
animationManager.length 1.70833

animationSystem.createAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_zoom_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_reload.baf


animationSystem.createBundle reload2
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_reload2.baf


animationSystem.createBundle run
animationBundle.fadeinTime 0.25
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_left.baf
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_right.baf
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_backward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_run_forward.baf
animationBundle.addEvent effect:1


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.4
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.01
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_zoom_stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0 
animationBundle.addAnimation Objects/Weapons/Handheld/unica6/Animations/1p/1p_tozoom.baf


rem *** Triggers ***
animationSystem.createTrigger Trigger zoom_still
animationTrigger.addBundle zoom_still

animationSystem.createTrigger MovementTrigger zoom_move
animationTrigger.addBundle zoom_run
animationTrigger.valueHolder 1p_zoom_move

animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addBundle zoom_fire
animationTrigger.message 1

animationSystem.createTrigger Trigger zoom
animationTrigger.fadeInTime 0.2
animationTrigger.addChild zoom_still
animationTrigger.addChild zoom_move
animationTrigger.addChild zoom_fire

animationSystem.createTrigger RandomTrigger rnd_idle
animationTrigger.addBundle idle1
animationTrigger.addBundle idle2

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
animationTrigger.addBundle fire
animationTrigger.message 1

animationSystem.createTrigger RandomTrigger rnd_Reload
animationTrigger.addBundle reload
animationTrigger.addBundle reload2

animationSystem.createTrigger MessageTrigger reload
animationTrigger.addChild rnd_reload
animationTrigger.message 2

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

animationSystem.createTrigger Trigger specialMoves
animationTrigger.addChild forwardRun
animationTrigger.addChild backwardRun
animationTrigger.addChild leftRun
animationTrigger.addChild rightRun

animationSystem.createTrigger Trigger normal
animationTrigger.fadeInTime 0.2
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire
animationTrigger.addChild reload

animationSystem.createTrigger SwitchMessageTrigger root
animationTrigger.addChild zoom
animationTrigger.addChild normal
animationTrigger.addBundle zoomTransition
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild specialMoves
animationTrigger.addChild startup

