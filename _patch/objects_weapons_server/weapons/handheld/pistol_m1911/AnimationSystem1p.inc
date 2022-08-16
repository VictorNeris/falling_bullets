animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.035/0.01/0.035
animationSystem.cameraSpring.zoomDamping 2.5/2.5/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/60

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_deploy.baf
animationManager.looping 0
animationManager.length 1.25

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_reload.baf
animationManager.looping 0
animationManager.length 2.7

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_run.baf
animationManager.length 0.625

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_sprint.baf
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_tozoom.baf
animationManager.looping 0
animationManager.length 0.15

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_zoom_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_reload.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_zoom_stand.baf


animationSystem.createBundle zoomTransitions
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_m1911/Animations/1p/1p_M1911_tozoom.baf


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

animationSystem.createTrigger Trigger still
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
animationTrigger.fadeInTime 0.2
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire
animationTrigger.addChild reload

animationSystem.createTrigger SwitchMessageTrigger root
animationTrigger.addChild zoom
animationTrigger.addChild normal
animationTrigger.addBundle zoomTransitions
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

