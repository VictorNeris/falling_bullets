animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.045/0.045/0.045
animationSystem.cameraSpring.zoomDamping 2.5/2.5/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_deploy.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_fire.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_Idle1.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_Idle2.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_zoom_stand.baf

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_fire.baf


animationSystem.createBundle idle1
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_Idle2.baf


animationSystem.createBundle Idle2
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_Idle1.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3


animationSystem.createBundle run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_stand.baf


animationSystem.createBundle zoom_changeFirerate
animationBundle.isLooping 0


animationSystem.createBundle zoom_fire
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_zoom_stand.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/Wrench/Animations/1p/1p_Wrench_zoom_stand.baf


rem *** Triggers ***
animationSystem.createTrigger RandomTrigger rnd_idle
animationTrigger.addBundle idle1
animationTrigger.addBundle Idle2

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
animationTrigger.fadeInTime 0.1
animationTrigger.addBundle fire
animationTrigger.message 1

animationSystem.createTrigger Trigger normal
animationTrigger.fadeInTime 0.2
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire

animationSystem.createTrigger Trigger root
animationTrigger.addChild normal

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addBundle zoom_fire
animationTrigger.message 1

animationSystem.createTrigger Trigger zoom_still
animationTrigger.addBundle zoom_still

animationSystem.createTrigger Trigger zoom
animationTrigger.fadeInTime 0.2
animationTrigger.addChild zoom_fire
animationTrigger.addChild zoom_still

