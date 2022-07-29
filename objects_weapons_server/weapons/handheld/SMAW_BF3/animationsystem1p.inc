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
animationSystem.cameraSpring.zoomDamping 2.9/2.9/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/600
endrem

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_deploy.baf
animationManager.looping 0
animationManager.length 1.66667

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_fire.baf
animationManager.looping 0
animationManager.length 0.416667

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_reload.baf
animationManager.looping 0
animationManager.length 3.54167

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_run.baf
animationManager.length 0.65

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_tozoom.baf
animationManager.looping 0
animationManager.length 0.95

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.416667

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_zoom_run.baf
animationManager.looping 0
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_zoom_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.9
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.833333


animationSystem.createBundle run
animationBundle.fadeOutTime 0.9
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 1.0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/Animations/1p/1p_smaw_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_zoom_stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/SMAW_BF3/animations/1p/1p_smaw_tozoom.baf


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

