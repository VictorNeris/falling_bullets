animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 10/10/10
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/60

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_deploy.baf
animationManager.looping 0
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_reload.baf
animationManager.length 4.45

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_run.baf
animationManager.length 1.4

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_shift.baf
animationManager.looping 0
animationManager.length 1.35

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_sprint.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_stand.baf
animationManager.length 2.2

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_idle.baf
animationManager.length 2.2

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_tozoom.baf
animationManager.looping 0
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_m14ebr_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.23

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_m14ebr_zoom_run.baf
animationManager.length 1.58

animationSystem.createAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_m14ebr_zoom_stand.baf
animationManager.looping 0
animationManager.length 2.16667

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.9
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.08
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_fire.baf


animationSystem.createBundle idle1
animationBundle.isLooping 1
animationBundle.fadeInTime 0.4
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_idle.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.37


animationSystem.createBundle run
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_run.baf


animationSystem.createBundle shift
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_shift.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.48


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.9
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_m14ebr_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_m14ebr_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_m14ebr_zoom_stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/L96/animations/1p/1p_l115_tozoom.baf



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

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup