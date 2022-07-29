animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.045/0.045/0.045
animationSystem.cameraSpring.zoomDamping 2.9/2.9/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_deploy.baf
animationManager.looping 0
animationManager.length 1.25

animationSystem.createAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_fire.baf
animationManager.looping 0
animationManager.length 0.333333

animationSystem.createAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_idle1.baf
animationManager.looping 0
animationManager.length 3.79167

animationSystem.createAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_idle2.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0
animationBundle.playForever 1
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_fire.baf


animationSystem.createBundle idle1
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_idle1.baf


animationSystem.createBundle idle2
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_idle2.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_deploy.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/AT_mine/Animations/1p/1p_at_mine_stand.baf


rem *** Triggers ***
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

