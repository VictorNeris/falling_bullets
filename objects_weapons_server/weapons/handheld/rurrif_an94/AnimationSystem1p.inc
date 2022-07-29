animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 4/2.5/1
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/20

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/changeFirerate.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/deploy.baf
animationManager.looping 0
animationManager.length 0.75

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.20

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/reload.baf
animationManager.looping 0
animationManager.length 3.7

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/run.baf
animationManager.length 0.62

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/tozoom.baf
animationManager.looping 0
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/zoom_fire_iron.baf
animationManager.looping 0
animationManager.length 0.20

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/zoom_run_iron.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/zoom_stand_iron.baf

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/changeFirerate.baf


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.05
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 1.0


animationSystem.createBundle run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.7
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/zoom_fire_iron.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/zoom_run_iron.baf


animationSystem.createBundle zoom_still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/zoom_stand_iron.baf

beginrem

animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/rurrif_an94/Animations/1p/tozoom.baf
endrem

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
animationTrigger.idleTime 5/10

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

animationSystem.createTrigger MessageTrigger changeFirerate
animationTrigger.addBundle changeFirerate
animationTrigger.message 8

animationSystem.createTrigger MessageTrigger reload
animationTrigger.addBundle reload
animationTrigger.message 2

animationSystem.createTrigger Trigger normal
rem animationTrigger.fadeInTime 0.2
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

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

