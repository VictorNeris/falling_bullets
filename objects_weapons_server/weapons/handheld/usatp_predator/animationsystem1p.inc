animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 2/3/4
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_deploy.baf
animationManager.looping 0
animationManager.length 1.2

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_fire.baf
animationManager.looping 0
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_reload.baf
animationManager.looping 0
animationManager.length 3

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_sprint.baf
animationManager.looping 0
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_tozoom.baf
animationManager.looping 0
animationManager.length 0.95

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_zoom_Fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.833333

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_zoom_Run.baf

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_zoom_Stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_run_prone.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_toprone_rev.baf
animationManager.length 1.2

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_fire.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.5


animationSystem.createBundle idle1
animationBundle.isLooping 0
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_idle1.baf


animationSystem.createBundle idle2
animationBundle.isLooping 0
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_idle2.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_reload.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.8
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_stand.baf


animationSystem.createBundle zoom_changeFirerate
animationBundle.isLooping 0


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_zoom_Fire.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.5


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_zoom_Run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_zoom_Stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_tozoom.baf


animationSystem.createBundle run_prone
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_run_prone.baf


animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_toprone.baf
animationBundle.addEvent effect:8
animationBundle.setEventStartTime effect:8 0


animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/usatp_predator/Animations/1p/1p_predator_toprone_rev.baf
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

animationSystem.createTrigger Trigger zoom
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

animationSystem.createTrigger MessageTrigger reload
animationTrigger.addBundle reload
animationTrigger.message 2

animationSystem.createTrigger Trigger normal
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
animationTrigger.addChild startup

