animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.05
animationSystem.cameraSpring.zoomDamping 2.9/2.9/0.6
animationSystem.cameraSpring.stiffness 2/2/2
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/20

beginrem
animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.02/0.02/0.02
animationSystem.cameraSpring.zoomDamping 2.9/2.9/2.9
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/600
endrem

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_deploy.baf
animationManager.looping 0
animationManager.length 0.9

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_fire.baf
animationManager.looping 0
animationManager.length 0.35
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_reload.baf
animationManager.looping 0
animationManager.length 4.85

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_run.baf
animationManager.length 0.65

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_tozoom.baf
animationManager.looping 0
animationManager.length 0.95

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_zoom_run.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_zoom_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.1
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.833333


animationSystem.createBundle run
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 1.2
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_zoom_stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/sovat_rpg7/Animations/1p/1p_rpg_tozoom.baf


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

