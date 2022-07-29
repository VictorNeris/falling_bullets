animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.045/0.045/0.045
animationSystem.cameraSpring.zoomDamping 2.9/2.9/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_deploy.baf
animationManager.looping 0

animationSystem.createAnimation objects/weapons/handheld/c4_explosives/animations/1p/1p_c4_fire_throw.baf
animationManager.looping 0
animationManager.length 0.45

animationSystem.createAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_run.baf
animationManager.length 0.666667

animationSystem.createAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_sprint.baf

animationSystem.createAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0
animationBundle.addAnimation objects/weapons/handheld/c4_explosives/animations/1p/1p_c4_fire_throw.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_deploy.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation objects/weapons/handheld/c4_explosives/Animations/1p/1p_c4_stand.baf


rem *** Triggers ***
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
animationTrigger.addChild normal
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

