animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.045/0.045/0.045
animationSystem.cameraSpring.zoomDamping 2.9/2.9/0
animationSystem.cameraSpring.stiffness 60/60/60
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_deploy.baf
animationManager.length 2.08333

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_fire.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_reload1.baf
animationManager.length 4.58333

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_reload2.baf
animationManager.length 6.66667

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_run.baf
animationManager.length 0.708333

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_tozoom.baf
animationManager.looping 0
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_zoom_fire.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_zoom_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 1
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.7
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_reload1.baf


animationSystem.createBundle reload_0
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.05
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_reload2.baf


animationSystem.createBundle run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.9
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_sprint.baf


animationSystem.createBundle still
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_zoom_stand.baf


animationSystem.createBundle zoom_transitions
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/SR_M82A3/Animations/1p_m82a3_tozoom.baf


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
animationTrigger.addBundle reload_0
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
animationTrigger.addBundle zoom_transitions
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

